from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

def create_chain(vectorstores):
    llm = ChatOpenAI()
    chain = RetrievalQAWithSourcesChain.from_llm(
    llm=llm,
    retriever = vectorstores.as_retriever())
    return chain