from fastapi import APIRouter, Depends
from services.gamification import add_eco_points
from dependencies.firebase_auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/eco-points")
async def update_eco_points(points: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user['uid']
    return await add_eco_points(user_id, points)
