from fastapi import APIRouter, Depends
from dependencies.firebase_auth import get_current_user
from services.or_tools_routes import optimize_route
from services.pydeck_service import build_route_layer, build_recycling_layer, create_map_view

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.post("/eco-map")
async def eco_map(locations: list[tuple[float, float]], current_user: dict = Depends(get_current_user)):
    """
    Generate optimized eco-route + recycling centers as Pydeck JSON config
    Input: list of (lat, lng)
    """
    # Mock: simple Euclidean distance matrix
    def dist(a, b): return int(((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5 * 1000)
    n = len(locations)
    distance_matrix = [[dist(locations[i], locations[j]) for j in range(n)] for i in range(n)]

    route_indices = optimize_route(distance_matrix)
    coords = [[locations[i][1], locations[i][0]] for i in route_indices]  # lng, lat

    # Example recycling points
    recycling_points = [("Recycling Center A", locations[0][0]+0.01, locations[0][1]+0.01)]

    layers = [
        build_route_layer(coords),
        build_recycling_layer(recycling_points)
    ]

    return create_map_view([locations[0][1], locations[0][0]], layers)
