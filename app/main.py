from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="ONE Running API")
app.include_router(router)
