from fastapi import APIRouter, Depends
from services.product_suggestions import get_eco_alternatives
from dependencies.firebase_auth import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/suggestions")
async def product_suggestions(name: str, brand: str, category: str, current_user: dict = Depends(get_current_user)):
    return await get_eco_alternatives(name, brand, category)
