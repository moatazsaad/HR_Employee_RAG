# Import libraries
import os
import glob
import pandas as pd
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
import numpy as np
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import gradio as gr

# Load environment variables and set OpenAI API key
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Define model and database name
MODEL = "gpt-4o-mini"
db_name = "vector_db_hr"

# Convert HR CSV into Markdown files for RAG 

csv_path = "HR-Employee-Attrition.csv"  
base_folder = "hr_data"
employees_folder = os.path.join(base_folder, "employees")
os.makedirs(employees_folder, exist_ok=True)

# Read CSV
df = pd.read_csv(csv_path)

# Create Markdown files per employee with descriptive header for RAG retrieval
for idx, row in df.iterrows():
    emp_id = row["EmployeeNumber"]
    filename = os.path.join(employees_folder, f"employee_{emp_id}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Employee {emp_id}\n\n")
        f.write(f"This document is about Employee {emp_id}.\n\n")  # explicit sentence
        for col in df.columns:
            f.write(f"**{col}**: {row[col]}\n\n")

print(f"Created {len(df)} employee Markdown files in '{employees_folder}'")

# Load documents from folders and assign doc_type 
folders = [employees_folder]  # only employees for now
documents = []

for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader)
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        documents.append(doc)

print(f"Loaded {len(documents)} documents.")

# Split documents into chunks 
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks from employee documents.")

# Create embeddings and vector store 
embeddings = OpenAIEmbeddings()

# Delete existing collection if exists
if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

vectorstore = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=db_name)
print(f"Vectorstore created with {vectorstore._collection.count()} documents.")

# Conversational RAG setup 
llm = ChatOpenAI(temperature=0.7, model_name=MODEL)
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
retriever = vectorstore.as_retriever()

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm, retriever=retriever, memory=memory
)

# Example query
query = "Give me a summary of employee 1"
answer = conversation_chain.run("Give me a summary of employee 1")
print(answer)

# Gradio interface 
def chat(message, history):
    result = conversation_chain.invoke({"question": message})
    return result["answer"]

gr.ChatInterface(chat, type="messages").launch(share=True)
