from fastapi import FastAPI
from routers import info_router
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()
app.include_router(info_router)

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT)