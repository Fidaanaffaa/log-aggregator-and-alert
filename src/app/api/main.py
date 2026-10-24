from fastapi import FastAPI
from sqlmodel import create_engine
from sqlmodel import Session
from Data.database import get_session
from Data.Repo.logs import logs
app = FastAPI()
session = next(get_session())

@app.get("/")
async def root():
    return {"message": "Welcome to the Log Management System API!"}

@app.post("/create_log")
async def create_log(log: dict):
    logg = logs(session)
    print(log)
    result = await logg.create_log(log)
    return result

@app.get("/logs")
async def get_logs():
    logg = logs(session)
    result = await logg.get_logs()
    return result