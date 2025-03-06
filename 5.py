"""the first solution for question 5:path parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get("/n/{n}")
def triangle(n:int):
    result=''
    for i in range(1,n+1):
        for j in range (1,i+1):
            result+=str(i*j)+' '
        result+='\n '
    return result






"""the second solution for question 5:query parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get("/n")
def triangle(n:int):
    result=''
    for i in range(1,n+1):
        for j in range (1,i+1):
            result+=str(i*j)+' '
        result+='\n '
    return result






"""the third solution for question 5:request body."""

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class AllEvenDigitsNumbers(BaseModel):
    num: int
@app.post("/n")
def triangle(n: AllEvenDigitsNumbers):
    result = ''
    for i in range(1, n.num + 1):
        for j in range(1, i + 1):
            result += str(i * j) + ' '
        result += '\n'
    return {"result": result}