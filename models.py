from bson import ObjectId, Timestamp
from pydantic import BaseModel, Field
from typing import Optional, List, Any

from datetime import datetime
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class PuzzleMetaData(BaseModel):
    createdBy: str = Field(...)
    created: datetime
    lastModified: datetime

    class Config:
        arbitrary_types_allowed = True


class Puzzle(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    publicId: str = Field(default=None)
    name: str = Field(default=None)
    gridDimensions: List[int] = Field(default=[10, 9])
    state: str
    wordStarts: Optional[List[int]] = []
    arrows: Optional[dict]
    dashes: Optional[dict]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class PuzzleExtended(Puzzle):
    solution: Optional[str] = None
    answer: Optional[str] = "answer"
    notes: Optional[Any]
    metadata: Optional[PuzzleMetaData] = None

class UserSchema(BaseModel):
    id: Optional[str]
    roles: Optional[list]
