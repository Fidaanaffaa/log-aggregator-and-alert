from fastapi import FastAPI

app = FastAPI()

app.get("/")
async def root():
    return {"message": "Welcome to the Log Management System API!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)