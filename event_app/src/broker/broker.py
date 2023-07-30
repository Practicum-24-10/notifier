from abc import ABC

from event_app.src.broker.rabbit_mq import rabbit
from message.models.mixin import MessageMixin


class AbstractBroker(ABC):
    async def send(self, message):
        pass


class RabbitBroker(AbstractBroker):
    def __init__(self):
        self._connect = rabbit

    async def send(self, message: MessageMixin):
        return True
