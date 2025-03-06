"""the first solution for question 10:path parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get('/factorial/{x}')

def factorial(x:int):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
    





"""the second solution for question 10:query parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get('/factorial/')

def factorial(x:int):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))






"""the third solution for question 10:request body."""

def calculate_factorial(x: int):
    if x == 1 or x == 0:
        return 1
    else:
        return x * calculate_factorial(x - 1)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    x: int

@app.post("/factorial/")
def factorial(x: Number):
    if x.x < 0:
        return {"error": "Factorial is not defined for negative numbers"}
    else:
        return {"result": calculate_factorial(x.x)}
    
