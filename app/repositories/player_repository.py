from app.models.player import Player
from sqlalchemy.orm import Session
from app.schemas.player import PlayerCreate, PlayerUpdate
from typing import Optional, List


class PlayerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, player_id : int) -> Optional[Player]:
        return self.db.query(Player).filter(Player.id == player_id).first()

    def get_by_nickname(self, player_nickname : str) -> Optional[Player]:
        return self.db.query(Player).filter(Player.nickname == player_nickname).first()

    def get_by_rating(self, player_rating : int) -> Optional[Player]:
        return self.db.query(Player).filter(Player.rating == player_rating).first()

    def get_all(self, skip : int = 0, limit : int = 100) -> List[Player]:
        return self.db.query(Player).offset(skip).limit(limit).all()

    def create(self, player_data : PlayerCreate) -> Player:
        player = Player(**player_data.model_dump())

        self.db.add(player)
        self.db.commit("Add new Player")
        self.db.refresh(player)
        return player

    #def update(self, player : Player, player_data : PlayerUpdate) -> Player:
    #дописать update, добавить delete