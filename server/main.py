from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# http://127.0.0.1:8000/

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prompt/{prompt}")
def read_prompt(prompt: str):
    print(prompt)
    return {"prompt": prompt}
