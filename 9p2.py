from fastapi import FastAPI
app=FastAPI()
@app.get('/LocalVariable/')

def f():
    s='I live in khorramabad'
    return 'Inside Function:(local variable)',s


