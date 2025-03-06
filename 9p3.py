from fastapi import FastAPI
app=FastAPI()
@app.get('/GlobelVariable')

def f():
    global s
    s='I live in khorramabad'
    return 'when we have both local and globel variable in same time ,with a same name ,the program will show us the local one:',s
