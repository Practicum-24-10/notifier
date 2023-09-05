import json

from enricher.app.render import render
from enricher.app.utils import get_template, get_user_info


class MessageHandler:
    def __init__(self, producer, backoff) -> None:
        self.producer = producer
        self.backoff = backoff

    async def send_message(self, message):
        recipient_ids = message["recipients"]
        template = await get_template(message["template"])

        for recipient in recipient_ids:
            user_info = await get_user_info(recipient)
            if user_info:
                message = await render(template, user_info)
                await self.producer.send_message(
                    json.dumps({"email": user_info["email"], "message": message})
                )
            else:
                await self.backoff.send_message(json.dumps(json.dumps(message)))
