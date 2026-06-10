from fastapi import FastAPI
from sqlmodel import create_engine
from Data.Repo.logs import logs
app = FastAPI()

postgres_file_name = "LumberYard.db"
postgres_url = f"postgresql://user:password@localhost/{postgres_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(postgres_url, connect_args=connect_args)

@app.get("/")
async def root():
    return {"message": "Welcome to the Log Management System API!"}

@app.post("/create_log")
async def create_log(log: dict):
    logg = logs()
    print(log)
    result = await logg.create_log(log)
    return result
