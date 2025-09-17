from config.db import db

async def add_eco_points(user_id: str, points: int):
    user = await db.users.find_one({"id": user_id})
    if not user:
        await db.users.insert_one({"id": user_id, "eco_points": points, "streak": 1, "badges": []})
        return {"eco_points": points, "streak": 1}
    streak = user.get("streak", 0) + 1
    eco_points = user.get("eco_points", 0) + points
    await db.users.update_one({"id": user_id}, {"$set": {"eco_points": eco_points, "streak": streak}})
    return {"eco_points": eco_points, "streak": streak}
