from typing import Union
from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prompt/{prompt}")
def read_prompt(prompt: str):
    return {"prompt": prompt}
