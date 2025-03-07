"""the first solution for question 4:path parameter."""

from fastapi import FastAPI
from typing import List
app=FastAPI()
@app.get("/number/{EvenNumbers}",response_model=List[int])
def PrintAllEvenDigits():
    EvenNumbers=[]
    for number in range(100,1000,2):
        str_number=str(number)
        if int(str_number[0])%2==0 and int(str_number[1])%2==0 and int(str_number[2])%2==0:
            EvenNumbers.append(number)
    return EvenNumbers






"""the second solution for question 4:query parameters."""


from fastapi import FastAPI
from typing import List,Optional
app=FastAPI()
@app.get("/number/",response_model=List[int])
def PrintAllEvenDigits(EvenNumbers:Optional[int]=None):
    EvenNumbers=[]
    for number in range(100,1000,2):
        str_number=str(number)
        if int(str_number[0])%2==0 and int(str_number[1])%2==0 and int(str_number[2])%2==0:
            EvenNumbers.append(number)
    return EvenNumbers








"""the third solution for question 4:request body."""

from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel
app=FastAPI()
class number(BaseModel):
    EvenNumbers:int
@app.post("/number/",response_model=List[int])
def PrintAllEvenDigits(EvenNumbers:Optional[int]=None):
    EvenNumbers=[]
    for number in range(100,1000,2):
        str_number=str(number)
        if int(str_number[0])%2==0 and int(str_number[1])%2==0 and int(str_number[2])%2==0:
            EvenNumbers.append(number)
    return EvenNumbers
