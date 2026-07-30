from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Valve Inventory API")

app.include_router(router)