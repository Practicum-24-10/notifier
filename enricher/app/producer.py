import aio_pika


class RabbitMQProducer:
    def __init__(self, amqp_url, queue_name):
        self.amqp_url = amqp_url
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()

    async def send_message(self, message):
        if not self.connection or self.connection.is_closed:
            await self.connect()

        if self.channel is None:
            raise Exception("Channel not initialized")

        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()), routing_key=self.queue_name
        )

    async def close(self):
        if self.connection and not self.connection.is_closed:
            await self.connection.close()


async def main():
    amqp_url = "amqp://guest:guest@localhost/"
    queue_name = "SendingQueue"

    producer = RabbitMQProducer(amqp_url, queue_name)
    await producer.connect()

    message = "Hello4, RabbitMQ!"
    await producer.send_message(message)

    await producer.close()
