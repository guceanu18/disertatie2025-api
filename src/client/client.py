import requests

BASE_URL = "http://127.0.0.1:8000"
INVENTORY_URL = f'{BASE_URL}/inventory/'
COMMANDS_URL = f'{BASE_URL}/commands/'
CONFIG_URL = f'{BASE_URL}/config/'

class RouterClient:
    def __init__(self, base_url=BASE_URL, inventory_url=INVENTORY_URL, commands_url=COMMANDS_URL, config_url=CONFIG_URL):
        self.base_url = base_url
        self.inventory_url = inventory_url
        self.commands_url = commands_url
        self.config_url = config_url

    def add_router(self, name, mgmt_ip, site):
        data = {
            "name": name,
            "mgmt_ip": mgmt_ip,
            "site": site
        }
        response = requests.post(self.inventory_url, json=data)
        return response.json()

    def list_routers(self):
        response = requests.get(self.inventory_url)
        response.raise_for_status()
        return response.json()

    def get_router_by_name(self, router_name):
        url = f"{self.inventory_url}{router_name}"
        response = requests.get(url)
        return response.json()

    def delete_router(self, router_name):
        url = f"{self.inventory_url}{router_name}"
        response = requests.delete(url)
        if response.status_code == 404:
            print(f"Router '{router_name}' not found.")
            return None
        return response.json()

    def update_router(self, router_name, **kwargs):
        # kwargs can include name, mgmt_ip, site, device_type
        if not kwargs:
            raise ValueError("You must provide at least one field to update.")
        url = f"{self.inventory_url}{router_name}"
        response = requests.patch(url, json=kwargs)
        if response.status_code == 404:
            print(f"Router '{router_name}' not found.")
            return None
        return response.json()

    def run_command(self, router_name, command):
        url = f"{self.commands_url}run"
        payload = {
            "router_name": router_name,
            "command": command
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["output"]

    def push_config(self, router_name, template_name, template_vars):
        url = f"{self.config_url}push"
        payload = {
            "router_name": router_name,
            "template_name": template_name,
            "template_vars": template_vars
        }
        response = requests.post(url, json=payload)
        if response.status_code == 404:
            raise ValueError(f"Router '{router_name}' not found.")
        response.raise_for_status()
        return response.json()["result"]
