from fastapi import FastAPI # This object of FastAPI will be used later to create our APIs

app = FastAPI() # The FastAPI object has many attributes and will be used

@app.get("/") # Homepage
def index():
    return {
        "name": "First Data"
    } # FastAPI uses JSON