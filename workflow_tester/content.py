from datetime import date, datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    To: str
    From: str
    Body: str | None = None
    AccountSid: str
    SmsSid: str
    SmsStatus: str


class SMSResponse(BaseModel):
    pass


class TwilloSMSResponse(SMSResponse):
    account_sid: str | None = None                      # "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    api_version: date | None = None                     # "2010-04-01",
    body: str                                           # "Hi there",
    date_created: datetime = datetime.utcnow()          # "Thu, 30 Jul 2015 20:12:31 +0000",
    date_updated: datetime = datetime.utcnow()          # "Thu, 30 Jul 2015 20:12:31 +0000",
    date_sent: datetime = datetime.utcnow()             # "Thu, 30 Jul 2015 20:12:31 +0000",
    direction: str = "outbound-api"
    error_code: str | None = None
    error_message: str | None = None
    from_: str = Field(alias='from')                    # "+15017122661",
    messaging_service_sid: str                          # "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    num_media: str = "0"
    num_segments: str = "1"
    price: str | None = None
    price_unit: str | None = None
    sid: str
    status: int | str = "sent"
    subresource_uris: dict[str, str] = {}
    to: str                                              # "+15558675310",
    uri: str                                             # URL Path
    more_info: str | None = None
