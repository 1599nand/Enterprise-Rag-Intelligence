# Enterprise Secure RAG System

A secure enterprise-grade Retrieval-Augmented Generation (RAG) system with:

## Features
- Multi-source retrieval
- RBAC-based access control
- Semantic search
- ChromaDB vector storage
- FastAPI backend
- Streamlit frontend
- Citation-aware responses
- Hallucination reduction

## Tech Stack
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings

## Demo Users
- alice → HR
- bob → Engineering
- charlie → Finance
- admin → Full Access

## Run Backend

```bash
python -m uvicorn app.main:app --reload --port 8001
```

## Run Frontend

```bash
streamlit run frontend.py
```

## Architecture

User Query → RBAC Filter → Semantic Retrieval → ChromaDB → Grounded Response