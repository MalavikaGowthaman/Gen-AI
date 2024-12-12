from langchain.document_loaders import UnstructuredURLLoader

def load_documents(urls):
    loaders = UnstructuredURLLoader(urls=urls)
    
    return loaders.load()