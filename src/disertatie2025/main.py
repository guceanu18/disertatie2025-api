from fastapi import FastAPI
from disertatie2025.routers import inventory, config, commands
from disertatie2025.database import Base, engine

app = FastAPI(title="Multicast VPN Automation Tool")
Base.metadata.create_all(bind=engine)

app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(config.router, prefix="/config", tags=["Config Push"])
app.include_router(commands.router, prefix="/commands", tags=["Show Commands"])
