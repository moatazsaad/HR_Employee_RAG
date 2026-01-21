from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "HR Employee RAG system live!"}

@app.post("/query")
def query_employee(data: Query):
    result = conversation_chain.invoke({"question": data.question})
    return {"answer": result["answer"]}

