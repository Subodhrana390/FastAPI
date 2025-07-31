from typing import Generator, Any
from contextlib import contextmanager
from app.db.session import SessionLocal

@contextmanager
def get_db() -> Generator[Any, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
