from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


import pandas as pd
import json
import os

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
all_docs = []

# PDFs
# pdf_folder = "data/pdfs"

# for file in os.listdir(pdf_folder):
#     loader = PyPDFLoader(f"{pdf_folder}/{file}")
#     docs = loader.load()

#     chunks = splitter.split_documents(docs)

#     for c in chunks:
#         c.metadata["source"] = file
#         c.metadata["access"] = ["finance", "admin"]

#     all_docs.extend(chunks)

# CSV
csv_path = "data/csv/employees.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        text = str(row.to_dict())

        from langchain.schema import Document

        doc = Document(
            page_content=text,
            metadata={
                "source": "employees.csv",
                "access": ["hr", "admin"]
            }
        )

        all_docs.append(doc)

# JSON logs
json_path = "data/logs/logs.json"

if os.path.exists(json_path):
    with open(json_path) as f:
        logs = json.load(f)


    for log in logs:
        doc = Document(
            page_content=str(log),
            metadata={
                "source": "logs.json",
                "access": ["engineering", "admin"]
            }
        )
        all_docs.append(doc)

# Store in ChromaDB
vectordb = Chroma.from_documents(
    documents=all_docs,
    embedding=embedding,
    persist_directory="chroma_db"
)

vectordb.persist()

print("Data ingestion complete")