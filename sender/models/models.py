import uuid
import re

from pydantic import BaseModel


class Notification(BaseModel):
    notification_id: uuid.UUID
    user_id: uuid.UUID
    content_id: str
    type: str

    @classmethod
    def get_random_notification(cls):
        return cls(notification_id=uuid.uuid4(),
                user_id=uuid.uuid4(),
                content_id="tt3245235",
                type='email')


class Email:
    "E-mail validation class"
    def __init__(self, email: str):
        self.email = self._is_valid_email(email)

    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("Неверный емэйл: {self.email}")
        return email

    def __repr__(self):
        return f'Email: {self.email}'

    def __str__(self):
        return self.email


class EmailTemplate(BaseModel):
    "Validate e-mail from SendingQueue"
    email: str
    message: str
    #letter: str 
    subject: str = "random"
    content_id: str = "random"
    user_id: uuid.UUID = uuid.uuid4()
    notification_id: uuid.UUID = uuid.uuid4()