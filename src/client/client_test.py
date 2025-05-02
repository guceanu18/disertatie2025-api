from src.client.client import RouterClient

client = RouterClient()

# Add a router
print(client.add_router(
    name="CE-R2",
    mgmt_ip="192.168.1.2",
    site="SiteB"
))

# List routers
print(client.list_routers())

# Get a router by name
print(client.get_router_by_name("CE-R2"))

# Update a router
print(client.update_router("CE-R2", site="SiteC"))

# Delete a router
print(client.delete_router("CE-R2"))


