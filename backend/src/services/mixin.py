from abc import ABC

from backend.src.broker import AbstractBroker
from backend.src.models.model_mixin import EnricherIn


class AbstractMixin(ABC):
    pass


class MixinModel(AbstractMixin):
    def __init__(self, broker: AbstractBroker):
        self.broker = broker

    async def _send_to_broker(self, message: EnricherIn):
        response = await self.broker.send_in_queue(message)
        if not response:
            return None
        return response
