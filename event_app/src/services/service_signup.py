from functools import lru_cache
from uuid import UUID

from fastapi import Depends

from event_app.src.broker import AbstractBroker
from event_app.src.broker.rabbit_mq import get_broker
from event_app.src.services.mixin import MixinModel
from message.models.message_signup import MessageSignUp


class SignUpService(MixinModel):
    async def send_signup(self, user_id: UUID, email: str):
        data = {
            'user_id': str(user_id),
            'email': email
        }
        message = MessageSignUp(recipients=[user_id], data=data)
        response = await self._send_to_broker(message)
        if response:
            return True
        return False


@lru_cache()
def get_signup_service(
        broker: AbstractBroker = Depends(get_broker),
) -> SignUpService:
    return SignUpService(broker)
