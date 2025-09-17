import requests
from .settings import GOOGLE_MAPS_API_KEY

def get_nearby_places(lat, lng, keyword, radius=5000):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "keyword": keyword,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()
