from typing import List
from pydantic import BaseModel

class Router(BaseModel):
    name: str
    mgmt_ip: str
    site: str

class ISP_Router(BaseModel):
    name: str
    mgmt_ip: str
    role: str
