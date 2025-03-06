from fastapi import FastAPI
from typing import List
app=FastAPI()
@app.get("/",response_model=List[int])
def FirstPlusSecondEqualThirdByFourth():
    num=[]
    for digits in range(1000,10000):
        str_num=str(digits)
        if int(str_num[0])+int(str_num[1])==int(str_num[2])*int(str_num[3]):
            num.append(digits)
    return num