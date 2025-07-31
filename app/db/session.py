from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import DATABASE_URL

if "render.com" in DATABASE_URL and "?sslmode=" not in DATABASE_URL:
    DATABASE_URL += "?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
