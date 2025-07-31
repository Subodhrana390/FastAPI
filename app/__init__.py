from fastapi import FastAPI
from .api import auth, api_router
from .db.session import engine
from .models import Base


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    Base.metadata.create_all(bind=engine)
    return app
