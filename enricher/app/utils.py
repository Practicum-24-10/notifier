import aiohttp

from enricher.configs.settings import config
from enricher.configs.logger import logger


async def get_user_info(user_id):
    url = f"{config.auth_url}{user_id}"
    headers = {"Authorization": f"Bearer {config.auth_token}"}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    email = data.get("email")
                    name = data.get("name")
                    return {"email": email, "name": name}
                else:
                    error_message = (
                        f"Failed to fetch user info (Status Code: {response.status})"
                    )
                    logger.error(str(error_message))
                    return None
        except aiohttp.ClientConnectorError as e:
            logger.error(str(e))
            return None


async def get_template(template_id):
    # Тут должен быть запрос к TemplateDB
    template_content = "Привет, {{ name }}! Поздравляем с регистрацией аккаунта в нашем сервисе!"  # noqa
    return template_content
