import asyncio

from enricher.app.consumer import RabbitMQConsumer
from enricher.app.handler import message_handler


async def main():
    consumer = RabbitMQConsumer(
        queue_name="api", amqp_url="amqp://guest:guest@localhost/"
    )
    try:
        await consumer.start_consuming(message_handler)
    finally:
        await consumer.close()


if __name__ == "__main__":
    asyncio.run(main())
