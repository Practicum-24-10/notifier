from functools import lru_cache
from uuid import UUID

from fastapi import Depends

from backend.src.broker import AbstractBroker
from backend.src.broker.rabbit_mq import get_broker
from backend.src.models.broker_model import EnricherIn
from backend.src.services.mixin import MixinModel


class EventService(MixinModel):
    async def send_event(self, user_ids: list[UUID], template_id: UUID, delay: bool):
        message = EnricherIn(
            recipients=user_ids, template=template_id, delay=delay, queue="api"
        )
        response = await self._send_to_broker(message)
        if response:
            return True
        return False


@lru_cache()
def get_event_service(
    broker: AbstractBroker = Depends(get_broker),
) -> EventService:
    return EventService(broker)
