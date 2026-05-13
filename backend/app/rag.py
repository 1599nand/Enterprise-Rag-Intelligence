from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.auth import get_user_role

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

def retrieve(query, username):

    role = get_user_role(username)

    docs = vectordb.similarity_search(query, k=5)

    allowed_docs = []

    for d in docs:

        access_roles = d.metadata.get("access", [])

        if role in access_roles:
            allowed_docs.append(d)

    return allowed_docs