class RabbitMQConsumer:
    def __init__(self, queue_name, connection):
        self.queue_name = queue_name
        self.connection = connection

    async def start_consuming(self, callback, producer):
        channel = await self.connection.channel()
        await channel.set_qos(prefetch_count=1)
        queue = await channel.declare_queue(self.queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await callback(message.body.decode(), producer)
