import asyncio

from enricher.app.consumer import RabbitMQConsumer
from enricher.app.handler import message_handler
from enricher.app.producer import RabbitMQProducer
from enricher.app.rabbit import RabbitMQConnect


async def main():
    rabbit = RabbitMQConnect(amqp_url="amqp://guest:guest@localhost/")
    await rabbit.connect()
    consumer = RabbitMQConsumer(queue_name="api", connection=rabbit.connection)
    producer = RabbitMQProducer(queue_name="SendingQueue", connection=rabbit.connection)
    try:
        await consumer.start_consuming(message_handler, producer)
    finally:
        await rabbit.close()


if __name__ == "__main__":
    asyncio.run(main())
