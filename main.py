import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == os.getenv("SECRET_TOKEN"):
        return PlainTextResponse(content=params.get("hub.challenge"))
    return JSONResponse(status_code=403, content={"error": "Invalid verification token"})


@app.post("/webhook")
async def receive_message(request: Request):
    try:
        data = await request.json()
        print("Mensaje recibido:", data)
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        print("Error parseando JSON:", e)
        return JSONResponse(status_code=400, content={"error": "Invalid JSON"})
