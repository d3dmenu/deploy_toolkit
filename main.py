import uvicorn 
import numpy as np
import warnings

from fastapi import FastAPI, Form   

app = FastAPI()
warnings.simplefilter("ignore")

@app.get("/")
async def main():
    return {"Message": 'Deploy API Success By.Nicks'}

@app.get("/calc")
async def calculator(a : int = 0, b : int = 0):
    return {"result": a + b}

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.post("/data/")
async def visual(data: list = Form(...), account: str = Form(...), firebase: str = Form(...)):
    data = np.array(data).astype(float)
    count, status = 0, False
    for i in range(100, len(data)):
        
        PosX = data[i - 100:i].mean()
        PosY = data[i - 200:i].mean()
        PosZ = abs(PosX - PosY)

        if PosX > PosY and status == False:
            count += 1
            status = True
        if PosX < PosY and status == True:
            status = False
    return {"size": len(data), "count": count-1, "account": account, "firebase": firebase}