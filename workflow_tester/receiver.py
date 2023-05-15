import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

import content
import config

app = FastAPI()

logger = logging.getLogger(__name__)
logging.basicConfig(level='DEBUG', format='%(asctime)s - %(levelname)s - %(message)s')


@app.get("/")
async def root():
    return config.get_settings()


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
            'messaging_service_sid': config.get_settings().mss,
            'sid': config.get_settings().sid,
        }).json())
