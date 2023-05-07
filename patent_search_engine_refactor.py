import os
import numpy as np
import pandas as pd
import faiss
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import openai
import configparser
import logging
import redis
import hnswlib

# os.environ["TOKENIZERS_PARALLELISM"] = "false"
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config['OpenAI']['api_key']
# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PatentSearchEngineConfig:
    def __init__(self):
        self.max_question_tokens = 200
        self.max_patent_info_tokens = 1500
        self.max_search_results = 20
        self.title_weight = 10000
        self.abstract_weight = 9000


class PatentSearchEngine:
    def __init__(self, data_path, config):
        self.config = config
        self.patents = self.load_data(data_path)
        logging.info("数据加载完成")
        print(self.patents.head())
        self.tokenizer, self.model = self.load_transformer_model()
        logging.info("Transformer模型加载完成")
        logging.info("连接到Redis server 6379...")
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)  # Connect to your Redis server
        logging.info("专利向量计算...")
        self.patent_vectors = self.compute_patent_vectors()
        logging.info("专利向量计算完成")
        # self.index = self.create_hnsw_index()
        # logging.info("Faiss hnsw索引创建完成")

        self.index = self.create_faiss_index()
        logging.info("Faiss 索引创建完成")

    def generate_gpt3_query(self,question):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"在苹果专利数据集中,根据以下问题生成一个关键词查询: {question}"}],
            max_tokens=self.config.max_patent_info_tokens,
            n=1,
            stop=None,
            temperature=0,
        )
        return response.choices[0]['message']['content'].strip()
    
    def truncate_text(self, text, max_tokens):
        text = str(text)  # 将输入转换为字符串
        tokens = text.split()
        truncated_tokens = tokens[:max_tokens]
        return " ".join(truncated_tokens)

    
    def extract_relevant_part(self, question, text):
        truncated_question = self.truncate_text(question, self.config.max_question_tokens)
        truncated_text = self.truncate_text(text, self.config.max_patent_info_tokens)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"从以下文本中提取与问题相关的部分:\n问题: {truncated_question}\n文本: {truncated_text}\n相关部分:"}],
            max_tokens=self.config.max_patent_info_tokens,
            n=1,
            stop=None,
            temperature=0
        )
        return response.choices[0]['message']['content'].strip()



    def get_gpt3_answer(self, question, patent_info):
   
        truncated_question = self.truncate_text(question, self.config.max_question_tokens)
        truncated_patent_info = self.truncate_text(patent_info, self.config.max_patent_info_tokens)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"根据以下问题和专利信息生成一个答案,回复需用中文：\n问题：{truncated_question}\n专利信息：{truncated_patent_info}\n答案："}],
            max_tokens=self.config.max_patent_info_tokens,
            n=1,
            stop=None,
            temperature=0
        )
        return response.choices[0]['message']['content'].strip()



    def load_data(self, data_path):
        data = pd.read_csv(data_path)
        patents = data[['invention_title', 'abstract', 'descriptionText', 'assignee']]
        return patents

    def load_transformer_model(self):
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        model = AutoModel.from_pretrained("distilbert-base-uncased")
        return tokenizer, model
    
    def patent_to_text(self, patent):
        title = patent['invention_title']
        abstract = patent['abstract']
        weighted_title = ' '.join([title] * self.config.title_weight)
        weighted_abstract = ' '.join([abstract] * self.config.abstract_weight)
        print(title)
        return f"{weighted_title} {weighted_abstract} {patent['descriptionText']} {patent['assignee']}"

    def distilbert_text_to_vector(self, text):
        # Check if the text vector is already in Redis
        vector = self.redis_client.get(text)
        if vector is not None:
            # If the vector is in Redis, deserialize and return it
            return np.frombuffer(vector, dtype=np.float32)

        # If the vector is not in Redis, calculate it and store it in Redis
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        vector = outputs.last_hidden_state.mean(dim=1).detach().numpy().squeeze()
        
        # Serialize the vector and store it in Redis
        self.redis_client.set(text, vector.tobytes())
        
        return vector
    def create_hnsw_index(self):
        dimension = self.patent_vectors.shape[1]
        index = hnswlib.Index(space='l2', dim=dimension)
        index.init_index(max_elements=self.patents.shape[0], ef_construction=800, M=32)
        index.set_ef(100)
        index.add_items(self.patent_vectors)
        return index
    def create_faiss_index(self):
        dimension = self.patent_vectors.shape[1]
        quantizer = faiss.IndexFlatL2(dimension)
        nlist = 5
        index = faiss.IndexIVFFlat(quantizer, dimension, nlist)
        index.train(self.patent_vectors)
        index.add(self.patent_vectors)
        return index

    def compute_patent_vectors(self):
        return np.array([self.distilbert_text_to_vector(self.patent_to_text(patent)) for _, patent in self.patents.iterrows()])
    
    def search(self, query, k=20, skip_set=None):
        if skip_set is None:
            skip_set = set()

        query_vector = self.distilbert_text_to_vector(query)
        _, indices = self.index.search(np.array([query_vector]), k * 2)

        filtered_indices = [idx for idx in indices[0] if idx not in skip_set]

        # 如果筛选后的结果数量不足，尝试增加k值重新搜索
        while len(filtered_indices) < k:
            k *= 2
            # 检查k是否超过专利数据的长度
            if k > len(self.patents):
                break
            _, indices = self.index.search(np.array([query_vector]), k)
            filtered_indices = [idx for idx in indices[0] if idx not in skip_set]

        # 当k值已经超过专利数据的长度时，返回所有可用的筛选结果
        return self.patents.iloc[filtered_indices[:min(k, len(filtered_indices))]]   
    # def search(self, query, k=20, skip_set=None):
    #     if skip_set is None:
    #         skip_set = set()

    #     query_vector = self.distilbert_text_to_vector(query)
    #     _, indices = self.index.knn_query(query_vector, k=k * 2)

    #     filtered_indices = [idx for idx in indices[0] if idx not in skip_set]

    #     # 如果筛选后的结果数量不足，尝试增加k值重新搜索
    #     while len(filtered_indices) < k:
    #         k *= 2
    #         # 检查k是否超过专利数据的长度
    #         if k > len(self.patents):
    #             break
    #         _, indices = self.index.knn_query(query_vector, k=k)
    #         filtered_indices = [idx for idx in indices[0] if idx not in skip_set]

    #     # 当k值已经超过专利数据的长度时，返回所有可用的筛选结果
    #     return self.patents.iloc[filtered_indices[:min(k, len(filtered_indices))]]


    
def display_results(question, results, search_engine):
    logging.info("开始显示搜索结果")
    print("\n搜索结果：")
    for index, result in results.iterrows():
        patent_info = f"\n发明名称: {result['invention_title']}\n摘要: {result['abstract']}\n申请人: {result['assignee']}"

        # 截断问题和专利信息
        truncated_question = search_engine.truncate_text(question, search_engine.config.max_question_tokens)
        truncated_patent_info = search_engine.truncate_text(patent_info, search_engine.config.max_patent_info_tokens)

        answer = search_engine.get_gpt3_answer(truncated_question, truncated_patent_info)
        print(f"----------\n 答案：{answer}\n")
        print(patent_info + "\n")

        # 添加提取与问题相关的description文本片段
        relevant_description = search_engine.extract_relevant_part(truncated_question, result['descriptionText'])
        print(f"相关描述片段: {relevant_description}\n")
        logging.info("搜索结果显示完成")


def main():
    data_path = "patent_api_demo_image_fusion.csv"
    search_engine_config = PatentSearchEngineConfig()
    search_engine = PatentSearchEngine(data_path, search_engine_config)

    while True:
        question = input("请输入问题，或输入'退出'以结束：")
        if question.lower() == '退出':
            break
        query = search_engine.generate_gpt3_query(question)
        logging.info(f"GPT-3查询生成完成 {query}")
        results = search_engine.search(query, k=search_engine.config.max_search_results)
        display_results(question, results, search_engine)


if __name__ == '__main__':
    main()