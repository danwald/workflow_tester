import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

import constants
import content

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/testMessage/")
async def processIncomingMessage(message: content.Message) -> content.SMSResponse:
    logger.debug(f'received: {message}')
    return JSONResponse(
        content=content.TwilloSMSResponse(**{
            'acccountSid': message.AccountSid,
            'body': message.Body,
            'from': message.From,
            'to': message.To,
            'uri': '/testMessage',
            'messaging_service_sid': constants.MSG_SSID,
            'sid': constants.SID,
        }).json())
