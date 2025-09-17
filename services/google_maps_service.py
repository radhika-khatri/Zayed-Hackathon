import requests
from config.settings import GOOGLE_MAPS_API_KEY

def get_distance_matrix(locations):
    matrix = []
    for origin in locations:
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        params = {
            "origins": origin,
            "destinations": "|".join(locations),
            "mode": "driving",
            "key": GOOGLE_MAPS_API_KEY
        }
        response = requests.get(url, params=params).json()
        row = [elem['distance']['value'] for elem in response['rows'][0]['elements']]
        matrix.append(row)
    return matrix

def get_nearby_recycling(lat, lng, category="recycling"):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {"location": f"{lat},{lng}", "radius": 5000, "keyword": category, "key": GOOGLE_MAPS_API_KEY}
    return requests.get(url, params=params).json()
