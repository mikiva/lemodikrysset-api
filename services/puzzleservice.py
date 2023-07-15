from services.dbservice import DBService
from models import Puzzle

class PuzzleService:
    def __init__(self, db: DBService = None):
        self.db = db

    async def puzzle_exists(self, puzzle_id):
        return await self.db.document_exists(puzzle_id)

    async def get_puzzle(self, puzzle_id) -> dict | Puzzle:
        doc = await self.db.get_one_document_by_field(field="publicId", value=puzzle_id)

        return doc

    async def store_puzzle(self, puzzle_data: dict):
        ...