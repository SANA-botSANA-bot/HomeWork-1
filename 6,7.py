"""the first solution for question 6 and 7:path parameters."""

from fastapi import FastAPI
import numpy as np
app=FastAPI()
@app.get("/numbers/{numbers}")
def calculate(numbers:str):
    NumberList=numbers.split(",")
    try:
        NumberList=[float(x) for x in NumberList]
        max_num=max(NumberList)
        min_num=min(NumberList)
        ave=np.mean(NumberList)
        s_d=np.std(NumberList)
        return{
            "the maximum of your list numbers is":max_num,
            "the minimum of your list numbers is":min_num,
            "the average of your list numbers is":ave,
            "the standard deviation of your list numbers is":s_d
        }
    except ValueError:
        return {"error": "Please provide a list of numbers separated by commas."}






"""the third solution for question 6 and 7:query parameters."""

from fastapi import FastAPI
import numpy as np
app=FastAPI()
@app.get("/numbers/")
def calculate(numbers:str):
    NumberList=numbers.split(",")
    try:
        NumberList=[float(x) for x in NumberList]
        max_num=max(NumberList)
        min_num=min(NumberList)
        ave=np.mean(NumberList)
        s_d=np.std(NumberList)
        return{
            "the maximum of your list numbers is":max_num,
            "the minimum of your list numbers is":min_num,
            "the average of your list numbers is":ave,
            "the standard deviation of your list numbers is":s_d
        }
    except ValueError:
        return {"error": "Please provide a list of numbers separated by commas."}






"""the second solution for question 6 and 7:request body."""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
app = FastAPI()
class NumList(BaseModel):
    numbers: str
@app.post("/numbers/")
def calculate(numbers: NumList):
    NumberList = numbers.numbers.split(",")
    try:
        NumberList = [float(x) for x in NumberList]
        max_num = max(NumberList)
        min_num = min(NumberList)
        ave = np.mean(NumberList)
        s_d = np.std(NumberList)
        return {
            "the maximum of your list numbers is": max_num,
            "the minimum of your list numbers is": min_num,
            "the average of your list numbers is": ave,
            "the standard deviation of your list numbers is": s_d
        }
    except ValueError:
        return {"error": "Please provide a list of numbers separated by commas."}