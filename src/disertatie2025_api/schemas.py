from pydantic import BaseModel
from typing import Optional

class RouterInput(BaseModel):
    name: str
    mgmt_ip: str
    site: str

class RouterUpdate(BaseModel):
    name: Optional[str] = None
    mgmt_ip: Optional[str] = None
    site: Optional[str] = None

class CommandRequest(BaseModel):
    router_name: str
    command: str

class ConfigPushRequest(BaseModel):
    router_name: str
    template_vars: dict
    template_name: str
