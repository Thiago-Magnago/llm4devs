from langchain_community.document_loaders import WebBaseLoader

def load(url):
    loader = WebBaseLoader(url, verify_ssl=False)
    data = loader.load()
    return data