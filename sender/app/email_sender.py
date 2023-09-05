import logging
import smtplib
from email.message import EmailMessage
import uuid

from pydantic_settings import BaseSettings

from sender.models.models import EmailTemplate, Notification
from sender.db.abstract_database import AbstractNotificationDatabaseService

logger = logging.getLogger(__name__)


class EmailSender():
    """Class for e-mail sending"""

    def __init__(self, email_params: BaseSettings,
                 database: AbstractNotificationDatabaseService):
        self.email_params = email_params
        self.database = database

    def _get_smtp_server_connection(self):
        """Returns external SMTP-server connection"""
        server = smtplib.SMTP_SSL(
            self.email_params.address, self.email_params.port)
        server.login(self.email_params.login, self.email_params.password)
        self.server = server

    def send(self, data: EmailTemplate):
        """Send message for declared addresses"""
        logger.warning("SMTP connection made")
        # Forming message
        message = EmailMessage()
        message["From"] = self.email_params.login
        message["To"] = data.email
        message["Subject"] = data.subject
        message.set_content(data.message)
        # message.add_alternative(data.letter, subtype='html')
        # Sending message
        if self._allow_sending(data.notification_id, data.user_id):
            self.server.send_message(message)
            # Write sending confirmation to DB
            notification = Notification(
                notification_id=data.notification_id,
                user_id=data.user_id,
                content_id=data.content_id,
                type='email'
            )
            self.database.save_notification_to_db(notification)

    def _allow_sending(self, notification_id: uuid.UUID, user_id: uuid.UUID):
        """Checks whenever message with provided notification_id
        for declared user_id was not send"""
        # If there is no info about sent message sending is allowed
        if not self.database.get_notification_by_id(notification_id, user_id):
            return True
        logger.warning(f'''Данное сообщение id: {notification_id} уже отправлялось \
        данному пользователю {user_id}''')
        return False
