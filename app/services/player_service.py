from fastapi import HTTPException, status
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

    def get_all_players(self, skip : int = 0, limit : int = 100):
        return self.repo.get_all(skip, limit)

    def create_player(self, player_data : PlayerCreate):
        if self.repo.get_by_nickname(player_data.nickname):
            raise HTTPException(400, "Nickname already exists")

        return self.repo.create(player_data)

    def update_player(self, player_id: int, player_data: PlayerUpdate):
        player = self.get_player_by_id(player_id)

        if player_data.nickname and player_data.nickname != player.nickname:
            existing = self.repo.get_by_nickname(player_data.nickname)
            if existing:
                raise HTTPException(400,"Nickname already taken")

        return self.repo.update(player, player_data)

    def delete_player(self, player_id : int):
        player = self.get_player_by_id(player_id)
        self.repo.delete(player)
        return {"message":"Player deleted successfully"}