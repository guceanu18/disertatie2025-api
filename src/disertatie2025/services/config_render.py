import os
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_template(template_name: str, vars: dict) -> str:
    template = env.get_template(template_name)
    return template.render(vars)
