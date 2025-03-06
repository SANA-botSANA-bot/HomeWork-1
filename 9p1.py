from fastapi import FastAPI
app=FastAPI()
@app.get('/LocalVariable/')

def f():
    s='I live in khorramabad'
    return 'the local variable that introduced in function is:',s
