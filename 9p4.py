from fastapi import FastAPI
app=FastAPI()
@app.get('/GlobelVariable')

def f():
    s='I live in Iran'
    return s
