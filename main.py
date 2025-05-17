from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/webhook")
async def whatsapp_webhook(request: Request):
    body = await request.json()
    print("Mensaje recibido de WhatsApp:", body)
    return JSONResponse(content={"status": "ok"})
