from message.models.initiator import MessageInitiator
from message.models.mixin import MessageMixin
from message.models.queue import MessageQueue
from message.models.type import MessageType


class MessageSignUp(MessageMixin):
    initiator: MessageInitiator = MessageInitiator.API
    type: MessageType = MessageType.SIGN_UP
    queue: MessageQueue = MessageQueue.API
    data: dict

