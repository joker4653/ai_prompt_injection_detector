# Basic Frontend Routing using FastApi

from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Prompt Injection Detector API")
app.include_router(router)

# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Prompt Injection Detector API"}

# Basic health check endpoint
@app.get("/status")
async def status():
    return {"status": "ok"}