from motor import motor_asyncio
from settings import MongoSettings



config = MongoSettings()



client = motor_asyncio.AsyncIOMotorClient(config.connection_string)

database = client.lemodi

puzzle_collection = database.get_collection("puzzles")
users_collection = database.get_collection("users")



