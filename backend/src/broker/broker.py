from abc import ABC

import aio_pika
import orjson

from backend.src.models.broker_model import MixinModel


class AbstractBroker(ABC):
    async def send_in_queue(self, message):
        pass


class RabbitBroker(AbstractBroker):
    def __init__(self, rabbitmq_host):
        self.rabbitmq_host = rabbitmq_host
        self._connection = None
        self._channel = None

    async def start(self, queue):
        self._connection = await aio_pika.connect_robust(self.rabbitmq_host)
        self._channel = await self._connection.channel()
        await self._channel.declare_queue(queue, durable=True)

    async def send_in_queue(self, message: MixinModel):
        try:
            if self._channel is not None:
                await self._channel.default_exchange.publish(
                    aio_pika.Message(
                        body=orjson.dumps(message.json()), delivery_mode=2
                    ),
                    routing_key=message.queue,
                )
            else:
                raise
            return True
        except aio_pika.exceptions.AMQPError:
            return False

    async def close(self):
        if self._connection is not None:
            await self._connection.close()
