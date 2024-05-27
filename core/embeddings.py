from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import httpx

#http_client = httpx.Client(verify='petrobras-ca-root.pem')
http_client = httpx.Client(verify=False)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key=api_key, http_client=http_client)

def embed_doc(doc):
    return embeddings.embed_query(doc)

def embed_docs(docs):
    return embeddings.embed_documents(docs)