from fastapi import FastAPI

app=FastAPI()

# This is for the get request
@app.get("/")
def home():
    return {"Hello": "world"}