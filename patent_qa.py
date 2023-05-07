import pandas as pd
from haystack.document_stores.faiss import FAISSDocumentStore
from haystack.nodes.retriever.dense import DensePassageRetriever
from haystack.nodes import PromptNode,PromptTemplate
from haystack.nodes.preprocessor import PreProcessor
from haystack.pipelines import Pipeline
import os
import logging

from haystack.nodes.base import BaseComponent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Load and preprocess the CSV data
logger.info("Loading and preprocessing CSV data")
data = pd.read_csv('patent_api_demo_image_fusion.csv')
data = data[['invention_title', 'abstract', 'descriptionText', 'claim_text']]
data.columns = ['title', 'content', 'meta.description', 'meta.claims']

# 2. Create Haystack Document Store
logger.info("Creating Haystack Document Store")
# document_store.delete_documents(index='document')
document_store = FAISSDocumentStore(sql_url="sqlite:///faiss_patent012.db")

# 3. Import data into DocumentStore without preprocessing
logger.info("Importing data into DocumentStore")
documents = data.to_dict(orient='records')
document_store.write_documents(documents)

# 4. Use Dense Retriever
logger.info("Initializing Dense Retriever")
retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
    passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
    use_gpu=False
)

logger.info("Updating document embeddings")
document_store.update_embeddings(retriever)

# 5. Create a GPT-3.5 PromptNode
logger.info("Creating GPT-3.5 PromptNode")
from haystack.nodes import PromptNode
from haystack.nodes import PromptTemplate, PromptNode, PromptModel
from haystack.pipelines import Pipeline

# Specify the model you want to use:
openai_api_key = "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"

prompt_open_ai = PromptModel(
    model_name_or_path="gpt-3.5-turbo",
    use_gpu=False,
    api_key=openai_api_key)

# This sets up the default model:
prompt_model = PromptModel()

# Now let make one PromptNode use the default model and the other one the OpenAI model:
node_openai_q = PromptNode(prompt_model, default_prompt_template="question-generation")
node_openai_qa = PromptNode(prompt_open_ai, default_prompt_template="question-answering-with-references")

# 7. Create custom Haystack Pipeline
logger.info("Creating custom Haystack Pipeline")
custom_pipeline = Pipeline()
custom_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
custom_pipeline.add_node(component=node_openai_q, name="q_node", inputs=["Retriever"])
custom_pipeline.add_node(component=node_openai_qa, name="Generator", inputs=["q_node"])

# 8. Run the pipeline with a query
logger.info("Running the pipeline with a query")
query = "what's the image fusion process?"
output = custom_pipeline.run(query=query, params={"Retriever": {"top_k": 10}})
logger.info("Pipeline output: %s", output)
result = dict(zip(output["query"], output["answers"]))
logger.info("Final result: %s", result)
