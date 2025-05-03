from src.client.client import RouterClient

client = RouterClient()

# Add a router
print(client.add_router(
    name="R_INTERNET",
    mgmt_ip="192.168.72.128",
    site="ISP"
))

# List routers
print(client.list_routers())

# Get a router by name
print(client.get_router_by_name("R_INTERNET"))

# Update a router
print(client.update_router("R_INTERNET", mgmt_ip="192.168.72.128"))

# Send a command to a router
print(client.run_command("R_INTERNET", "show ip interface brief"))

# Push a config to the router
print(client.push_config(
    router_name="R_INTERNET",
    template_name="add_router.j2",
    template_vars={
        "mgmt_ip": "1.1.1.1",
        "mgmt_lan_ip": "2.2.2.2"
    }
))


# Delete a router
# print(client.delete_router("R_INTERNET"))

