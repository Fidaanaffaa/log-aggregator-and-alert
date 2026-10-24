from sqlmodel import create_engine, Session
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres@localhost:5433/lumberyard")
engine = create_engine(DATABASE_URL)

def __init__(self):
    pass

def get_session():
    with Session(engine) as session:
        yield session