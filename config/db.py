from motor.motor_asyncio import AsyncIOMotorClient
from .settings import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.eco_app
