from fastapi import FastAPI

from taggingsystem.api.routes import router

app = FastAPI(title="TaggingSystem", version="0.1.0")
app.include_router(router)
