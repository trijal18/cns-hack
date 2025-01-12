from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse
import apimodels
from models import temp, rf
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/fishy/")
async def check_fishy(reqBody: apimodels.UrlRequest):
    url=reqBody.url
    res=temp.check_fishy(url)
    jsonResponse = JSONResponse(status_code=200, content=json.loads(str(res)))
    return jsonResponse

@app.post("/check_url/")
async def check_url(reqBody: apimodels.UrlRequest):
    url=reqBody.url
    res=rf.process_url(url)
    jsonResponse = JSONResponse(status_code=200, content=res)
    return jsonResponse