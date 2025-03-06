"""the first solution for question 8:path parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get("/number/{number}")
def calculate(number:int):
    str_number=str(number)
    if len(str_number)==5:
        maximum=max(str_number)
        str_number=str_number.replace(maximum,'')
        return "your five digits number without it's maximum:",int(str_number)
    else:
        return "please enter a five digits number"






"""the second solution for question 8:query parameters."""

from fastapi import FastAPI
app=FastAPI()
@app.get("/number/")
def calculate(number:int):
    str_number=str(number)
    if len(str_number)==5:
        maximum=max(str_number)
        str_number=str_number.replace(maximum,'')
        return "your five digits number without it's maximum:",int(str_number)
    else:
        return "please enter a five digits number"





"""the third solution for question 8:request body."""

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class FiveDigits(BaseModel):
    number:int
@app.post("/number")
def calculate(data:FiveDigits):
    number=data.number
    str_number=str(number)
    if len(str_number)==5:
        maximum=max(str_number)
        str_number=str_number.replace(maximum,'')
        return "your five digits number without it's maximum:",int(str_number)
    else:
        return "please enter a five digits number"

