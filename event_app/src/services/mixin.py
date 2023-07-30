from abc import ABC
from typing import Any

from bson import ObjectId

from event_app.src.broker import AbstractBroker
from message.models.mixin import MessageMixin


class AbstractMixin(ABC):
    pass


class MixinModel(AbstractMixin):
    def __init__(self, broker: AbstractBroker):
        self.broker = broker

    async def _send_to_broker(self, message: MessageMixin):
        response = await self.broker.send(message)
        if not response:
            return None
        return response
