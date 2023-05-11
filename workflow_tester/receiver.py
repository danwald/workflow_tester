
from fastapi import FastAPI
import content
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/testMessage/")
async def processIncomingMessage(message: content.Message) -> content.SMSResponse:
    print(f'received: {message}')
    return JSONResponse(
        content=content.TwilloSMSResponse(**{
            'acccountSid': message.AccountSid,
            'body': message.Body,
            'from': message.From,
            'to': message.To,
            'uri': '/testMessage',
            'messaging_service_sid': content.MSG_SSID,
            'sid': content.SID,
        }).json())
