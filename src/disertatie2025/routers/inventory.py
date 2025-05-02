from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from disertatie2025.database import SessionLocal, RouterModel
from disertatie2025.schemas import RouterInput, RouterUpdate

router = APIRouter()

# Dependency to get a session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_router(router: RouterInput, db: Session = Depends(get_db)):
    # Check if router already exists
    existing = db.query(RouterModel).filter_by(name=router.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Router already exists")
    new_router = RouterModel(**router.dict())
    db.add(new_router)
    db.commit()
    db.refresh(new_router)
    return {"msg": f"Router {new_router.name} added"}

@router.get("/")
def list_routers(db: Session = Depends(get_db)):
    routers = db.query(RouterModel).all()
    return routers

@router.get("/{router_name}")
def get_router_by_name(router_name: str, db: Session = Depends(get_db)):
    router = db.query(RouterModel).filter_by(name=router_name).first()
    return router

@router.delete("/{router_name}")
def delete_router(router_name: str, db: Session = Depends(get_db)):
    router = db.query(RouterModel).filter_by(name=router_name).first()
    if router:
        db.delete(router)
        db.commit()
        return {"msg": f"Router {router_name} deleted"}
    else:
        raise HTTPException(status_code=404, detail="Router not found")

@router.patch("/{router_name}")
def update_router(router_name: str, updates: RouterUpdate, db: Session = Depends(get_db)):
    router = db.query(RouterModel).filter_by(name=router_name).first()
    if not router:
        raise HTTPException(status_code=404, detail="Router not found")

    update_data = updates.dict(exclude_unset=True)

    # If the name is being updated, ensure it's not a duplicate
    if "name" in update_data:
        existing = db.query(RouterModel).filter_by(name=update_data["name"]).first()
        if existing and existing.id != router.id:
            raise HTTPException(status_code=400, detail="A router with this new name already exists")

    for key, value in update_data.items():
        setattr(router, key, value)

    db.commit()
    db.refresh(router)
    return {"msg": f"Router {router_name} updated", "updated_fields": update_data}
