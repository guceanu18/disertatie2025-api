import requests

BASE_URL = "http://127.0.0.1:8000/inventory/"

class RouterClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def add_router(self, name, mgmt_ip, site):
        data = {
            "name": name,
            "mgmt_ip": mgmt_ip,
            "site": site
        }
        response = requests.post(self.base_url, json=data)
        response.raise_for_status()
        return response.json()

    def list_routers(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()

    def get_router_by_name(self, router_name):
        url = f"{self.base_url}{router_name}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def delete_router(self, router_name):
        url = f"{self.base_url}{router_name}"
        response = requests.delete(url)
        if response.status_code == 404:
            print(f"Router '{router_name}' not found.")
            return None
        response.raise_for_status()
        return response.json()

    def update_router(self, router_name, **kwargs):
        # kwargs can include name, mgmt_ip, site, device_type
        if not kwargs:
            raise ValueError("You must provide at least one field to update.")
        url = f"{self.base_url}{router_name}"
        response = requests.patch(url, json=kwargs)
        if response.status_code == 404:
            print(f"Router '{router_name}' not found.")
            return None
        response.raise_for_status()
        return response.json()
