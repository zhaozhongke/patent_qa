import numpy as np
import pandas as pd
import faiss
import openai
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# 加载CSV数据
print("加载CSV数据...")
data = pd.read_csv("patent_api_demo_.csv")
patents = data[['invention_title', 'abstract', 'descriptionText', 'assignee']]

# 设置OpenAI API
print("设置OpenAI API...")
openai.api_key = "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"

# 加载DistilBERT模型和分词器
print("加载DistilBERT模型和分词器...")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

# 将专利信息转换为文本
def patent_to_text(patent):
    return ' '.join(str(field) for field in patent)

# 使用DistilBERT模型将文本转换为向量表示
def distilbert_text_to_vector(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy().squeeze()

# 创建Faiss索引
print("创建Faiss索引...")
patent_vectors = np.array([distilbert_text_to_vector(patent_to_text(patent)) for _, patent in patents.iterrows()])
dimension = patent_vectors.shape[1]

# 使用IVFFlat索引方法
print("构建IVFFlat索引...")
quantizer = faiss.IndexFlatL2(dimension)
nlist = 10  # 将聚类数量减少到10
index = faiss.IndexIVFFlat(quantizer, dimension, nlist)
index.train(patent_vectors)
index.add(patent_vectors)

# 搜索函数
def search(query, k=10):
    print("使用DistilBERT执行初步搜索...")
    query_vector = distilbert_text_to_vector(query)
    
    # 使用DistilBERT执行初步搜索
    distances, indices = index.search(np.array([query_vector]), k * 2)
    
    # 使用OpenAI API处理查询并对初步结果进行再次搜索
    print("使用OpenAI API进行再次搜索...")
    query_vector = distilbert_text_to_vector(query)
    selected_patents = data.iloc[indices[0]]
    selected_patent_vectors = np.array([distilbert_text_to_vector(patent_to_text(patent)) for _, patent in selected_patents.iterrows()])
    similarities = cosine_similarity([query_vector], selected_patent_vectors)
    
    # 获取最终结果
    print("获取最终搜索结果...")
    final_indices = np.argsort(-similarities[0])[:k]
    final_results = selected_patents.iloc[final_indices]

    # 删除重复项
    final_results = final_results.drop_duplicates()

    return final_results

def extract_relevant_part(question, text):
    response = openai.Completion.create(
            engine="davinci",
            prompt=f"从以下文本中提取与问题相关的部分:\n问题: {question}\n文本: {text}\n相关部分:",
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.5
        )
    return response.choices[0].text.strip()
def get_gpt3_answer(question, patent_info):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"根据以下问题和专利信息生成一个答案：\n问题：{question}\n专利信息：{patent_info}\n答案：",
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
def display_results(question, results):
    print("\n搜索结果：")
    for index, result in results.iterrows():
        patent_info = f"专利申请号: {result['application_#']}\n发明名称: {result['invention_title']}\n摘要: {result['abstract']}\n申请人: {result['assignee']}"
        answer = get_gpt3_answer(question, patent_info)
        print(f"答案：{answer}\n")
        print(patent_info + "\n")
        
        # 添加提取与问题相关的description文本片段
        relevant_description = extract_relevant_part(question, result['descriptionText'])
        print(f"相关描述片段: {relevant_description}\n")

def generate_gpt3_query(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"根据以下问题生成一个关键词查询: {question}",
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=1.0,
    )
    return response.choices[0].text.strip()
while True:
    question = input("请输入问题，或输入'退出'以结束：")
    if question.lower() == '退出':
        break
    query = generate_gpt3_query(question)
    results = search(query)
    display_results(question, results)

