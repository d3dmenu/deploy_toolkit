import uvicorn 
import numpy as np
import warnings

from fastapi import FastAPI, Form   

app = FastAPI()
warnings.simplefilter("ignore")

@app.get("/")
async def main():
    return {"Message": 'Deploy API Success By.Nicky'}

@app.get("/calc")
async def calculator(a : int = 0, b : int = 0):
    return {"result": a + b}

@app.post("/visual/")
async def visual(data: list = Form(...)):
    return {"data": data}