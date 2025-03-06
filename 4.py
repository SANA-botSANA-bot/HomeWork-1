from fastapi import FastAPI,Path
from typing import List
app=FastAPI()
@app.get("/",response_model=List[int])
def PrintAllEvenDigits():
    EvenNumbers=[]
    for number in range(100,1000,2):
        str_number=str(number)
        if int(str_number[0])%2==0 and int(str_number[1])%2==0 and int(str_number[2])%2==0:
            EvenNumbers.append(number)
    return EvenNumbers