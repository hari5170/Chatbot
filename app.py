import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings

# Load your FAISS vectorstore (assumes you already saved it)
# e.g., faiss_index = FAISS.load_local("your_faiss_dir", OpenAIEmbeddings())
vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings())

# Define your RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Streamlit app
st.title("Medical RAG Chatbot")
user_input = st.text_input("Ask a medical question:")

if user_input:
    response = rag_chain.invoke({"query": user_input})  # Use 'query' instead of 'input' if needed
    st.markdown("**Answer:**")
    st.write(response['result'])

    with st.expander("Show context (retrieved documents)"):
        for doc in response['source_documents']:
            st.write(doc.page_content[:300] + "...")
