from fastapi import APIRouter, Depends
from models.eco_action import EcoAction
from config.db import db
from dependencies.firebase_auth import get_current_user

router = APIRouter(prefix="/eco-actions", tags=["EcoActions"])

@router.post("/")
async def log_eco_action(action: EcoAction, current_user: dict = Depends(get_current_user)):
    action.user_id = current_user['uid']
    await db.eco_actions.insert_one(action.dict())
    return {"message": "Eco action logged successfully"}
