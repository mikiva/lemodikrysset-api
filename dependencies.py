from fastapi import Depends

from services.dbservice import DBService
from services.puzzleservice import PuzzleService
from settings import MongoSettings


async def mongo_settings_provider():
    return MongoSettings()


async def db_service_provider(settings=Depends(mongo_settings_provider)) -> DBService:
    service = DBService(settings)
    return service


async def puzzle_service_provider(db: DBService = Depends(db_service_provider)) -> PuzzleService:
    return PuzzleService(db)
