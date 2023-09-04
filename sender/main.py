import asyncio

from psycopg2.extras import DictCursor

from sender.app.consumer import RabbitMQConsumer
from sender.app.handler import MessageHandler
from sender.app.rabbit import RabbitMQConnect
from sender.app.email_sender import EmailSender
from sender.app.postgres_service import NotificationPostgresService
from sender.config.settings import config, postgres_config, email_service_config
from sender.db.connection import create_pg_conn


async def main():
    rabbit = RabbitMQConnect(amqp_url=config.rabbit_url)
    await rabbit.connect()
    consumer = RabbitMQConsumer(
        queue_name=config.sending_queue, connection=rabbit.connection
    )
    handler = MessageHandler()
    try:
        await consumer.start_consuming(handler.send_message)
    finally:
        await rabbit.close()


if __name__ == "__main__":
    with create_pg_conn(**postgres_config.dict(), cursor_factory=DictCursor) as pg_conn:
        postgres_service = NotificationPostgresService(
            connection=pg_conn, tablename='notifications')
        email_sender = EmailSender(email_service_config, postgres_service)

        asyncio.run(main())
