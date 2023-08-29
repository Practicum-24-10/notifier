import datetime
from uuid import UUID, uuid4

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class MixinModel(BaseModel):
    id: UUID = Field(title="id сообщения", default_factory=uuid4)
    created_at: datetime.datetime = Field(
        title="Время создания", default_factory=datetime.datetime.now
    )
    queue: str
    delay: bool

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class EnricherIn(MixinModel):
    recipients: list[UUID]
    template: UUID
