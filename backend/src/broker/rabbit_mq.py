from backend.src.broker import RabbitBroker

rabbit: None | RabbitBroker = None


async def get_broker():
    return rabbit
