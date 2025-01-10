from fastapi import FastAPI
import apimodels
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/fishy/")
async def check_fishy(reqBody: apimodels.UrlRequest):
    return 1