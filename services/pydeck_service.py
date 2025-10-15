import pydeck as pdk

def build_route_layer(coords: list):
    """Create a Pydeck layer for optimized eco-routes"""
    return pdk.Layer(
        "PathLayer",
        data=[{"path": coords, "name": "Eco Route"}],
        get_path="path",
        get_color=[0, 128, 0],
        width_scale=2,
        width_min_pixels=3,
    )

def build_recycling_layer(points: list):
    """Create a Pydeck layer for recycling/donation centers"""
    return pdk.Layer(
        "ScatterplotLayer",
        data=[{"coordinates": [lng, lat], "name": name} for name, lat, lng in points],
        get_position="coordinates",
        get_color=[0, 0, 200],
        get_radius=50,
    )

def create_map_view(center: list, layers: list):
    """Return full Pydeck JSON config"""
    view_state = pdk.ViewState(latitude=center[1], longitude=center[0], zoom=12)
    deck = pdk.Deck(layers=layers, initial_view_state=view_state, map_style="light")
    return deck.to_json()
