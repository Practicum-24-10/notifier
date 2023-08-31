import datetime
from uuid import UUID, uuid4

from pydantic import Field

from backend.src.models.model_mixin import OrjsonMixin


class MixinModel(OrjsonMixin):
    id: UUID = Field(title="id сообщения", default_factory=uuid4)
    created_at: datetime.datetime = Field(
        title="Время создания", default_factory=datetime.datetime.now
    )
    queue: str
    delay: bool


class EnricherIn(MixinModel):
    recipients: list[UUID]
    template: UUID
