import asyncio

from enricher.app.consumer import RabbitMQConsumer
from enricher.app.handler import MessageHandler
from enricher.app.producer import RabbitMQProducer
from enricher.app.rabbit import RabbitMQConnect


async def main():
    rabbit = RabbitMQConnect(amqp_url="amqp://guest:guest@localhost/")
    await rabbit.connect()
    consumer = RabbitMQConsumer(queue_name="api", connection=rabbit.connection)
    producer = RabbitMQProducer(queue_name="SendingQueue", connection=rabbit.connection)
    handler = MessageHandler(producer)
    try:
        await consumer.start_consuming(handler.send_message)
    finally:
        await rabbit.close()


if __name__ == "__main__":
    asyncio.run(main())
