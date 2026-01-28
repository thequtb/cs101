from fastapi import FastAPI
from pydantic import BaseModel

from logger import log

app = FastAPI()


class LogMessage(BaseModel):
    message: str


@app.post("/log")
def create_log(data: LogMessage):
    log(data.message)
    return {"status": "logged", "message": data.message}
