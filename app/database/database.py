from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.CourseTaught import Base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)

