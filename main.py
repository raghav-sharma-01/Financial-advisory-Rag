from fastapi import FastAPI
from financial_advisory.router import router

app = FastAPI(
    title="Financial Advisory RAG API",
    description="Standalone Financial Advisory RAG system",
    version="1.0.0"
)

app.include_router(router)