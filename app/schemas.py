from pydantic import BaseModel

class DeviceCreate(BaseModel):
    provider: str
    user_id: str
