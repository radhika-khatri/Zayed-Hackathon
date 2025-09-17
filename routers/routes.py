from fastapi import APIRouter, Depends
from services.google_maps_service import get_distance_matrix, get_nearby_recycling
from services.or_tools_routes import optimize_route
from services.gamification import add_eco_points
from dependencies.firebase_auth import get_current_user

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.post("/green-route")
async def green_route(
    locations: list[str],
    lat: float = None,
    lng: float = None,
    current_user: dict = Depends(get_current_user)
):
    user_id = current_user['uid']

    distance_matrix = get_distance_matrix(locations)
    optimized_indices = optimize_route(distance_matrix)
    if not optimized_indices:
        return {"error": "Could not optimize route"}

    optimized_route = [locations[i] for i in optimized_indices]
    total_distance_m = sum(distance_matrix[optimized_indices[i]][optimized_indices[i+1]] for i in range(len(optimized_indices)-1))
    total_distance_km = total_distance_m / 1000
    points_awarded = int(total_distance_km // 1)

    user_update = await add_eco_points(user_id, points_awarded)
    nearby_stops = get_nearby_recycling(lat, lng) if lat and lng else []

    return {
        "optimized_route": optimized_route,
        "total_distance_km": total_distance_km,
        "eco_points_awarded": points_awarded,
        "user": user_update,
        "nearby_stops": nearby_stops
    }
