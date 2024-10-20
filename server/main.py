from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gemini import enter_prompt
from tts import tts


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


# TODO: error handling at each step

'''
Steps:
1. gather prompt
2. pass prompt into gemini
3. parse result to 2 separate variables: script and code
4. generate the video 
5. generate the tts script
6. speed up script so that it is same length as the video 
7. add together with pymovie?
8. save to folder
9. frontend displays video 
'''
@app.get("/prompt/{prompt}")
def read_prompt(prompt: str):
    # print(prompt)
    enter_prompt(prompt)
    # return {"prompt": prompt}
