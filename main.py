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

@app.post("/test/")
async def visual(data: list = Form(...)):
    return {"data": "Connect successfuly.."}

@app.post("/visual/")
async def visual(data: list = Form(...)):
    print(data)
    result = ""
    p1, p2, p3, p4 = [], [], [], []
    idx1 = [15, 21, 22, 23, 24, 25, 26, 27, 28, 29] # E I
    idx2 = [0, 1, 2, 3, 4, 5, 6, 7] # S N
    idx3 = [11, 18, 19, 20, 30, 31, 32, 33, 34, 35] # T F
    idx4 = [8, 9, 10, 12, 13, 14, 16, 17] # J P

    size = len(idx1) + len(idx2) + len(idx3) + len(idx4)

    for i in range(len(data)):
        if i in idx1: p1.append(data[i])
        elif i in idx2: p2.append(data[i])
        elif i in idx3: p3.append(data[i])
        elif i in idx4: p4.append(data[i])

    patternP2 = ["Z", "Z", "X", "X", "X", "X", "Z", "Z"]
    patternP4 = ["X", "X", "Z", "X", "Z", "Z", "X", "X"]

    # Visual P1
    if p1.count("X") > p1.count("Z"):
        result += "E"
    elif p1.count("X") < p1.count("Z"):
        result += "I"
    else:
        result += "I"

    # Visual P2
    key_N, key_S = 0, 0
    for v in range(8):
        if data[v] == patternP2[v]:
            key_S += 1
        else:
            key_N += 1
    if key_S > key_N:
        result += "S"
    elif key_S < key_N:
        result += "N"
    else:
        if data[3] == "Z":
            result += "S"
        else:
            result += "N"
            

    # Visual P3
    if p3.count("X") > p3.count("Z"):
        result += "T"
    elif p3.count("X") < p3.count("Z"):
        result += "F"
    else:
        result += "F"
    
    # Visual P4
    key_J, key_P = 0, 0
    for v in range(8):
        if p4[v] == patternP2[v]:
            key_J += 1
        else:
            key_P += 1
    if key_J > key_P:
        result += "J"
    elif key_J < key_P:
        result += "P"
    else:
        if p4[5] == "Z":
            result += "J"
        else:
            result += "P"
    return {"data": result}