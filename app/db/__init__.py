from app.db.session import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


__all__ = ['get_db', "engine"]
