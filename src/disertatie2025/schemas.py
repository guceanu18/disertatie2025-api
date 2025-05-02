from pydantic import BaseModel
from typing import Optional

class RouterInput(BaseModel):
    name: str
    mgmt_ip: str
    site: str

class CommandRequest(BaseModel):
    router_name: str
    command: str

class ConfigPushRequest(BaseModel):
    router_name: str
    template_vars: dict
