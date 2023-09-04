import json
import logging

from sender.app.email_sender import EmailSender
from sender.models.models import EmailTemplate

logger = logging.getLogger(__name__)


class MessageHandler:
    """Class for validating and sending message"""

    async def send_message(self, message):

        sender = EmailSender()
        template = EmailTemplate()

        try:
            email = message["email"]
            message_text = message["message"]
        except json.JSONDecodeError:
            logger.warning("Сообщение из RabbitMQ не удалось обработать")

        to_send = template.parse_obj(message)
        sender.send(data=to_send)

        logger.warning("Сообщение отправлено")
