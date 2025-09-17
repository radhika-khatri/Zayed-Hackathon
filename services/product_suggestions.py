import requests
from config.settings import GEMINI_API_KEY
from config.db import db

async def get_eco_alternatives(product_name, brand, category):
    result = await db.products.find_one({"name": product_name, "brand": brand, "category": category})
    if result:
        return result.get("eco_alternatives", [])

    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    payload = {"query": f"eco-friendly alternatives to {product_name} by {brand} in {category}"}
    response = requests.post("https://api.gemini.com/eco-suggestions", json=payload, headers=headers)
    data = response.json()
    alternatives = data.get("alternatives", [])

    await db.products.insert_one({"name": product_name, "brand": brand, "category": category, "eco_alternatives": alternatives})
    return alternatives
