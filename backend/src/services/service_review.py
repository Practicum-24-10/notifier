# from functools import lru_cache
# from uuid import UUID
#
# from fastapi import Depends
#
# from backend.src.broker import AbstractBroker
# from backend.src.broker.rabbit_mq import get_broker
# from backend.src.services.mixin import MixinModel
# from message.models.channels import MessageChannels
# from message.models.mixin import MessageModel
# from message.models.queue import MessageQueue
# from message.models.type import MessageTemplate
#
#
# class ReviewService(MixinModel):
#     async def send_review_like(self, user_id: UUID, review_id: str, value: int):
#         data = {"user_id": user_id, "review_id": str(review_id), "value": value}
#         message = MessageModel(recipients=[user_id], data=data,
#                                channels=[MessageChannels.EMAIL], queue=MessageQueue.API,
#                                template=MessageTemplate.LIKE_REVIEW)
#         response = await self._send_to_broker(message)
#         if response:
#             return True
#         return False
#
#
# @lru_cache()
# def get_reviews_service(
#         broker: AbstractBroker = Depends(get_broker),
# ) -> ReviewService:
#     return ReviewService(broker)
