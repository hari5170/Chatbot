from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
#Extracting the data from pdf
def load_pdf_file(data):
    loader=DirectoryLoader(data, glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents
#split the data into smaller chunks
def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

#Downloading the embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def download_hugging_face_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings