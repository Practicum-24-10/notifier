import uuid

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


class EmailTemplate(BaseModel):
    "Validate e-mail from SendingQueue"
    email: str
    message: str
    # letter: str
    subject: str = "random"
    content_id: str = "random"
    user_id: uuid.UUID = uuid.uuid4()
    notification_id: uuid.UUID = uuid.uuid4()
