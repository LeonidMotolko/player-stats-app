from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class PlayerBase(BaseModel):
    nickname : str = Field(..., min_length=5, max_length=50, description="Player Nickname")

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(BaseModel):
    nickname : Optional[str] = Field(None, min_length=5, max_length=50)

class PlayerResponse(PlayerBase):
    id : int
    rating : int
    created_at : datetime

    class Config:
        from_attributes = True