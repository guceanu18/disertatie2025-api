from fastapi import APIRouter, HTTPException, Depends
from disertatie2025.schemas import CommandRequest
from sqlalchemy.orm import Session
from disertatie2025.services.ssh import run_command
from disertatie2025.database import SessionLocal, RouterModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/run")
def run_show_command(data: CommandRequest, db: Session = Depends(get_db)):
    target = db.query(RouterModel).filter_by(name=data.router_name).first()
    if not target:
        raise HTTPException(status_code=404, detail="Router not found")

    output = run_command(target.mgmt_ip, data.command)
    return {"output": output}
