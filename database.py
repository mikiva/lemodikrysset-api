from motor.motor_asyncio import AsyncIOMotorClient

from settings import MongoSettings

client: AsyncIOMotorClient = None
async def init_database():
    global client
    config = MongoSettings()



    client = AsyncIOMotorClient(config.connection_string)
    #puzzle_collection = database.get_collection("puzzles")
    #users_collection = database.get_collection("users")

    try:
        await client.admin.command("ping")
        print("MongoDB Ping Successful")
    except Exception as e:
        print("MongoDB Ping Failed")
        print(e)

async def get_database(db: str = "lemodi"):
    if not client:
        await init_database()

    return client[db]
async def get_collection(coll: str = "puzzles"):
    c = await get_database()
    return c[coll]


async def close_database():
    try:
        await client.close()
    except:
        ...