"""Console script for workflow_tester."""
from fastapi import FastAPI
import content

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/testMessage/")
async def processIncomingMessage(message: content.Message):
    print(f'received: {message}')
    return message
