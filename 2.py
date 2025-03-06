"""the first solution for question 2:path parameters."""

from fastapi import FastAPI,Path
import math
app=FastAPI()
@app.get("/compute-expression/{terms}")
def compute_expression_path(terms: int = Path(...)):
    total = 0.0
    for i in range(terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}






"""the second solution for question 2:query parameters."""

from fastapi import FastAPI,Query
import math
app=FastAPI()
@app.get("/compute-expression/")
def compute_expression_path(terms: int = Query(500)):
    total = 0.0
    for i in range(terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}






"""the third solution for question 2:body request."""

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class TermsInput(BaseModel):
    terms: int
@app.post("/compute-expression")
def compute_expression_body(data: TermsInput):
    total = 0.0
    for i in range(data.terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}