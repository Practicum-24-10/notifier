import json
from typing import Any

from enricher.app.render import render
from enricher.app.utils import get_template, get_user_info


class MessageHandler:
    def __init__(self, producer) -> None:
        self.producer = producer

    async def send_message(self, message):
        message = json.loads(json.loads(message))
        recipient_ids = message["recipients"]
        template_id = message["template"]
        template = await get_template(template_id)
        for recipient in recipient_ids:
            user_info = await get_user_info(recipient)
            message = await render(template, user_info)
            await self.producer.send_message(json.dumps({'email': user_info["email"], 'message': message}))
