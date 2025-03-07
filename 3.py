"""the first solution for question 3:path parameter."""

from fastapi import FastAPI
from typing import List,Optional
app=FastAPI()
@app.get("/num{num}",response_model=List[int])
def FirstPlusSecondEqualThirdByFourth(num:Optional[int]=None):
    num=[]
    for digits in range(1000,10000):
        str_num=str(digits)
        if int(str_num[0])+int(str_num[1])==int(str_num[2])*int(str_num[3]):
            num.append(digits)
    return num






"""the second solution for question 3:query parameters."""

from fastapi import FastAPI
from typing import List,Optional
app=FastAPI()
@app.get("/num",response_model=List[int])
def FirstPlusSecondEqualThirdByFourth(num:Optional[int]=None):
    num=[]
    for digits in range(1000,10000):
        str_num=str(digits)
        if int(str_num[0])+int(str_num[1])==int(str_num[2])*int(str_num[3]):
            num.append(digits)
    return num







"""the third solution for question 3:request body."""

from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel
app=FastAPI()
class result(BaseModel):
    num:int
@app.post("/num",response_model=List[int])
def FirstPlusSecondEqualThirdByFourth(num:Optional[int]=None):
    num=[]
    for digits in range(1000,10000):
        str_num=str(digits)
        if int(str_num[0])+int(str_num[1])==int(str_num[2])*int(str_num[3]):
            num.append(digits)
    return num