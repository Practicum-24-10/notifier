import json
import logging

from sender.models.models import EmailTemplate

logger = logging.getLogger(__name__)


class MessageHandler:
    def __init__(self, sender):
        self.sender = sender

    async def send_message(self, message):

        template = EmailTemplate

        try:
            email = message["email"]
            message_text = message["message"]
            logger.info(email, message_text)
        except json.JSONDecodeError:
            logger.warning("Сообщение из RabbitMQ не удалось обработать")

        to_send = template.parse_obj(message)
        self.sender.send(data=to_send)

        logger.warning("Сообщение отправлено")
