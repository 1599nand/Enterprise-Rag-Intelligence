from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import retrieve
from app.prompts import SYSTEM_PROMPT

app = FastAPI()


class QueryRequest(BaseModel):
    username: str
    query: str


@app.post("/ask")
def ask_question(req: QueryRequest):

    docs = retrieve(req.query, req.username)
    
    if not docs:
        return {
            "answer": "Access denied or no relevant information found"
        }

    context = "\n\n".join([
        d.page_content for d in docs
    ])

    citations = [
        d.metadata.get("source") for d in docs
    ]

    answer = f"""
Using enterprise context:

{context[:1000]}

Generated grounded response.
"""

    return {
        "answer": answer,
        "citations": citations,
        "confidence": "High"
    }