from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from disertatie2025.database import SessionLocal, RouterModel
from disertatie2025.schemas import RouterInput

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

@router.delete("/{router_name}")
def del_router(router_name: str, db: Session = Depends(get_db)):
    router = db.query(RouterModel).filter_by(name=router_name).first()
    if router:
        db.delete(router)
        db.commit()
        return {"msg": f"Router {router_name} deleted"}
    else:
        raise HTTPException(status_code=404, detail="Router not found")
