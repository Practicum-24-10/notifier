from functools import lru_cache
from uuid import UUID

from fastapi import Depends

from event_app.src.broker import AbstractBroker
from event_app.src.broker.rabbit_mq import get_broker
from event_app.src.services.mixin import MixinModel
from message.models.message_review import MessageLikeReview


class ReviewService(MixinModel):
    async def send_review_like(self, user_id: UUID, review_id: str, value: int):
        data = {"user_id": user_id, "review_id": str(review_id), "value": value}
        message = MessageLikeReview(recipients=[user_id], data=data)
        response = await self._send_to_broker(message)
        if response:
            return True
        return False


@lru_cache()
def get_reviews_service(
    broker: AbstractBroker = Depends(get_broker),
) -> ReviewService:
    return ReviewService(broker)
