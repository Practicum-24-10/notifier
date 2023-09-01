import asyncio

from enricher.app.consumer import RabbitMQConsumer
from enricher.app.handler import MessageHandler
from enricher.app.producer import RabbitMQProducer
from enricher.app.rabbit import RabbitMQConnect
from enricher.configs.settings import config


async def main():
    rabbit = RabbitMQConnect(amqp_url=config.rabbit_url)
    await rabbit.connect()
    consumer = RabbitMQConsumer(
        queue_name=config.enrichment_queue, connection=rabbit.connection
    )
    producer = RabbitMQProducer(
        queue_name=config.sending_queue, connection=rabbit.connection
    )
    handler = MessageHandler(producer)
    try:
        await consumer.start_consuming(handler.send_message)
    finally:
        await rabbit.close()


if __name__ == "__main__":
    asyncio.run(main())
