from pydantic import BaseModel


class Message(BaseModel):
    To: str
    From: str
    Body: str | None = None
    AccountSid: str
    SmsSid: str
    SmsStatus: str
