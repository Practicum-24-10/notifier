async def get_user_info(user_id):
    # Тут должен быть запрос к Auth
    return {'email': 'user@mail.com', 'name': 'John'}


async def get_template(template_id):
    # Тут должен быть запрос к TemplateDB
    template_content = 'Привет, {{ name }}! Поздравляем с регистрацией аккаунта в нашем сервисе!'  # noqa
    return template_content
