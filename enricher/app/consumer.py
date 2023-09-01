import aio_pika


class RabbitMQConsumer:
    def __init__(self, queue_name, amqp_url):
        self.queue_name = queue_name
        self.amqp_url = amqp_url
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=1)

    async def start_consuming(self, callback):
        if self.connection is None:
            await self.connect()

        if self.channel is None:
            raise Exception("Channel not initialized")

        queue = await self.channel.declare_queue(self.queue_name, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await callback(message.body.decode())

    async def close(self):
        if self.connection is not None:
            await self.connection.close()
