import aio_pika


class RabbitMQProducer:
    def __init__(self, connection, queue_name):
        self.connection = connection
        self.queue_name = queue_name

    async def send_message(self, message):
        self.channel = await self.connection.channel()
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()), routing_key=self.queue_name
        )
