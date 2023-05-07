# 这段代码实现了一个基于专利数据的搜索引擎，它能够回答用户提出的自然语言问题，并返回与问题相关的专利和专利描述文本。它的大致流程如下：
# 1. 加载专利数据并预处理。
# 2. 加载DistilBERT模型以计算文本向量。
# 3. 利用FAISS将专利向量索引以加速搜索。
# 4. 通过OpenAI GPT-3生成关键字查询。
# 5. 根据查询调用DistilBERT模型获取查询向量。
# 6. 通过FAISS查询得到最相关的专利。
# 7. 在搜索结果中显示每个专利的摘要信息和申请人信息。
# 8. 使用GPT-3从搜索结果中提取与问题相关的描述片段。
# 9. 显示搜索结果和相应的问答和相关描述片段。
# 该程序使用了第三方库NumPy, pandas, faiss, transformers和OpenAI API来完成特定任务，例如计算向量、构建索引、生成关键词查询和提供问答服务。程序还使用了类来组织代码并使其易于扩展和修改。

import numpy as np
import pandas as pd
import faiss
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import openai

class PatentSearchEngine:
    def __init__(self, data_path):
        self.patents = self.load_data(data_path)
        self.tokenizer, self.model = self.load_transformer_model()
        self.patent_vectors = self.compute_patent_vectors()
        self.index = self.create_faiss_index()
    def generate_gpt3_query(self,question):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"根据以下问题生成一个关键词查询: {question}"}],
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=1.0,
        )
        return response.choices[0]['message']['content'].strip()
    
    def truncate_text(self,text, max_tokens):
        tokens = text.split()
        truncated_tokens = tokens[:max_tokens]
        return " ".join(truncated_tokens)
    
    def extract_relevant_part(self, question, text):
        truncated_question = self.truncate_text(question, 200)
        truncated_text = self.truncate_text(text, 1500)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"从以下文本中提取与问题相关的部分:\n问题: {truncated_question}\n文本: {truncated_text}\n相关部分:"}],
            max_tokens=1520,
            n=1,
            stop=None,
            temperature=0.5
        )
        return response.choices[0]['message']['content'].strip()



    def get_gpt3_answer(self, question, patent_info):
        truncated_question = self.truncate_text(question, 200)
        truncated_patent_info = self.truncate_text(patent_info, 1500)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"根据以下问题和专利信息生成一个答案：\n问题：{truncated_question}\n专利信息：{truncated_patent_info}\n答案："}],
            max_tokens=1520,
            n=1,
            stop=None,
            temperature=0.5
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
        return ' '.join(str(field) for field in patent)

    def distilbert_text_to_vector(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).detach().numpy().squeeze()

    def compute_patent_vectors(self):
        return np.array([self.distilbert_text_to_vector(self.patent_to_text(patent)) for _, patent in self.patents.iterrows()])

    def create_faiss_index(self):
        dimension = self.patent_vectors.shape[1]
        quantizer = faiss.IndexFlatL2(dimension)
        nlist = 10
        index = faiss.IndexIVFFlat(quantizer, dimension, nlist)
        index.train(self.patent_vectors)
        index.add(self.patent_vectors)
        return index

    def search(self, query, k=10):
        query_vector = self.distilbert_text_to_vector(query)
        _, indices = self.index.search(np.array([query_vector]), k)
        return self.patents.iloc[indices[0]]
    

data_path = "patent_api_demo_noise_reduction.csv"
search_engine = PatentSearchEngine(data_path)
openai.api_key = "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"
def display_results(question, results):
    print("\n搜索结果：")
    for index, result in results.iterrows():
        patent_info = f"\n发明名称: {result['invention_title']}\n摘要: {result['abstract']}\n申请人: {result['assignee']}"

        # 截断问题和专利信息
        truncated_question = search_engine.truncate_text(question, 200)
        truncated_patent_info = search_engine.truncate_text(patent_info, 1500)

        answer = search_engine.get_gpt3_answer(truncated_question, truncated_patent_info)
        print(f"----------\n 答案：{answer}\n")
        print(patent_info + "\n")

        # 添加提取与问题相关的description文本片段
        relevant_description = search_engine.extract_relevant_part(truncated_question, result['descriptionText'])
        print(f"相关描述片段: {relevant_description}\n")


while True:
    question = input("请输入问题，或输入'退出'以结束：")
    if question.lower() == '退出':
        break
    query = search_engine.generate_gpt3_query(question)
    results = search_engine.search(query)
    display_results(question, results)

