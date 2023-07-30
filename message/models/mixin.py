from uuid import UUID, uuid4

import orjson
from pydantic import BaseModel, Field
import datetime

from message.models.queue import MessageQueue


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class MessageMixin(BaseModel):
    id: UUID = Field(title='id сообщения', default_factory=uuid4)
    created_at: datetime.datetime = Field(title='Время создания',
                                          default_factory=datetime.datetime.now)
    queue: MessageQueue
    recipients: list[UUID]

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
