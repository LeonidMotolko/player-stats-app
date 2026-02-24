from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from pydantic import model_validator

class MatchBase(BaseModel):
    player1_id : int
    player2_id : int

    @model_validator(mode='after')
    def check_players_not_same(self):
        if self.player1_id == self.player2_id:
            raise ValueError('Player1 and Player2 must be different')
        return self

class MatchCreate(MatchBase):
    pass

class MatchResult(BaseModel):
    winner_id : int

class MatchResponse(MatchBase):
    id : int
    created_at : datetime
    finished_at : Optional[datetime] = None
    winner_id : Optional[int] = None

    class Config:
        from_attributes = True