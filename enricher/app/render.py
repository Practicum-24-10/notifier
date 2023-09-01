from jinja2 import Template


async def render(template, user_info):
    template = Template(template)
    rendered_template = template.render(name=user_info['name'])
    return rendered_template
