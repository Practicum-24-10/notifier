from abc import ABC

import aio_pika
import orjson
from aio_pika.abc import AbstractRobustChannel

from backend.src.models.model_mixin import MixinModel


class AbstractBroker(ABC):
    async def send_in_queue(self, message):
        pass


class RabbitBroker(AbstractBroker):
    def __init__(self, rabbitmq_host):
        self.rabbitmq_host = rabbitmq_host
        self._connection = None
        self._channel = None

    async def connect(self):
        self._connection = await aio_pika.connect_robust(self.rabbitmq_host)
        self._channel = await self._connection.channel()

    async def send_in_queue(self, message: MixinModel):
        try:
            if self._channel is not None:
                await self._channel.default_exchange.publish(
                    aio_pika.Message(body=orjson.dumps(message.json())),
                    routing_key=message.queue,
                )
            else:
                raise
            return True
        except Exception:
            return False
