from pydantic import BaseModel
from typing import Optional
class PuzzleSchema(BaseModel):
    id: Optional[str]
    solution: Optional[str]
    board_data: Optional[any]
    
    
    
class UserSchema(BaseModel):
    id: Optional[str]
    roles: Optional[list]