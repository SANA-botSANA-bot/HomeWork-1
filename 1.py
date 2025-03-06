"""the first solution for question 1:path parameters."""

from fastapi import FastAPI
app = FastAPI()
@app.get("/number/{number}")
def PrintEvenDigitsWithStar(number:int):
    number_str = str(number)
    result = ""
    for digit in number_str:
        if int(digit) % 2 == 0:
            result += digit + "*"
    return 'this is a shown of your number with seprate the even digits and shown them by star:',result






"""the second solution for question 1:query parameters."""

from fastapi import FastAPI
app = FastAPI()
@app.get("/number/")
def PrintEvenDigitsWithStar(number:int=123456789):
    number_str = str(number)
    result = ""
    for digit in number_str:
        if int(digit) % 2 == 0:
            result += digit + "*"
    return 'this is a shown of your number with seprate the even digits and shown them by star:',result






"""the third solution for question 1:request body."""

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class num(BaseModel):
    number:int
@app.post("/number")
def PrintEvenDigitsWithStar(number:num):
    number_str = str(number.number)
    result = ""
    for digit in number_str:
        if int(digit) % 2 == 0:
            result += digit + "*"
    return 'this is a shown of your number with seprate the even digits and shown them by star:',result