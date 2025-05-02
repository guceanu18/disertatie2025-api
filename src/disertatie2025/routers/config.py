from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from disertatie2025.database import RouterModel, SessionLocal
from disertatie2025.schemas import ConfigPushRequest
from disertatie2025.services.config_render import render_template
from disertatie2025.services.ssh import push_config

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/push")
def push_router_config(data: ConfigPushRequest, db: Session = Depends(get_db)):
    target = db.query(RouterModel).filter_by(name=data.router_name).first()
    if not target:
        raise HTTPException(status_code=404, detail="Router not found")

    config = render_template("mvpn_template.j2", data.template_vars)
    result = push_config(target.mgmt_ip, config)
    return {"result": result}
