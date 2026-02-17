from fastapi import HTTPException, status
from fastapi.openapi.utils import status_code_ranges
from sqlalchemy.orm import Session
from app.repositories.player_repository import PlayerRepository
from app.schemas.player import PlayerCreate, PlayerUpdate

class PlayerService:
    def __init__(self, db : Session):
        self.repo = PlayerRepository(db)

    def get_player_by_id(self, player_id : int):
        player = self.repo.get_by_id(player_id)
        if not player:
            raise HTTPException(404, f"Player with id {player_id} not found")

        return player

    def get_player_by_nickname(self, player_nickname : str):
        player = self.repo.get_by_nickname(player_nickname)
        if not player:
            raise HTTPException(404, f"Player with nickname {player_nickname} not found")

        return player

    def get_all_player(self, skip : int = 0, limit : int = 100):
        return self.repo.get_all(skip, limit)

    def create_player(self, player_data : PlayerCreate):
        if self.repo.get_by_nickname(player_data.nickname):
            raise HTTPException(400, "Nickname already exists")

        return self.repo.create(player_data)


    #def update_player(self, player_data : PlayerUpdate):
