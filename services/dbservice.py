from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorGridOut

from settings import MongoSettings
from database import get_collection

from bson import json_util
import json
class DBService:
    _collection: AsyncIOMotorCollection = None

    def __init__(self, settings: MongoSettings):
        self.puzzle_collection_name = settings.collection

    async def collection(self):
        if not self._collection:
            self._collection = await get_collection(self.puzzle_collection_name)
        return self._collection

    async def document_exists(self, doc_id: str, field="publicId") -> bool:
        coll = await self.collection()
        found = await coll.find_one({field: doc_id}) is not None
        print(found)
        return found

    async def get_one_document_by_field(self, field="publicId", value=None):
        coll = await self.collection()
        doc = await coll.find_one({field: value})
        return doc

