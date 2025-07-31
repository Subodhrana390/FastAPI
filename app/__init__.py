from fastapi import FastAPI
from .api import auth, api_router


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    return app
