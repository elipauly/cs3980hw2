from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import FileResponse, PlainTextResponse
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

@app.exception_handler(HTTPException)
async def my_http_exception_handler(request, ex):
    return PlainTextResponse(str(ex.detail), status_code=ex.status_code)