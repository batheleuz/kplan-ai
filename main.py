### main.py ###
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama

def get_response(user_query):
    if not user_query:
        return {"error": "Query not provided"}

    # Charger la base de données vectorielle
    persist_directory = "db2"
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    # Charger le modèle de chat
    llm = ChatOllama(model="mistral", temperature=0)
    
    # Créer la chaîne QA avec retrieval
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    
    # Récupération des documents et réponse du modèle
    llm_response = qa_chain(user_query)
    response_text = llm_response["result"]
    sources = [doc.metadata['source'] for doc in llm_response["source_documents"]]
    
    return {"response": response_text, "sources": sources}
