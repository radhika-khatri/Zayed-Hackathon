from pydantic import BaseModel
from datetime import datetime

class EcoAction(BaseModel):
    user_id: str
    action_type: str
    impact_co2: float
    impact_water: float
    timestamp: datetime = datetime.utcnow()
