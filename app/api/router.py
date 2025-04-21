from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.device import Device
from app.schemas import DeviceCreate
from app.tasks.sync import sync_trainings

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/authorize")
def authorize_connection(device: DeviceCreate, db: Session = Depends(get_db)):
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return {"message": "Conexión autorizada", "device_id": db_device.id}

@router.post("/sync/{device_id}")
def start_sync(device_id: int, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    sync_trainings.delay(device_id)
    return {"message": f"Sincronización iniciada para el dispositivo {device_id}"}
