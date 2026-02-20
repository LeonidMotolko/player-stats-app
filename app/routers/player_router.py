from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.services.player_service import PlayerService
from app.schemas.player import PlayerResponse, PlayerCreate, PlayerUpdate

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", response_model=PlayerResponse, status_code=status.HTTP_201_CREATED)
def create_player(
    player_data: PlayerCreate,
    db: Session = Depends(get_db)
):
    """Создать нового игрока"""
    service = PlayerService(db)
    return service.create_player(player_data)


@router.get("/", response_model=List[PlayerResponse])
def get_all_players(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Получить список всех игроков (с пагинацией)"""
    service = PlayerService(db)
    return service.get_all_players(skip, limit)


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player_by_id(
    player_id: int,
    db: Session = Depends(get_db)
):
    """Получить игрока по ID"""
    service = PlayerService(db)
    return service.get_player_by_id(player_id)


@router.get("/nickname/{nickname}", response_model=PlayerResponse)
def get_player_by_nickname(
    nickname: str,
    db: Session = Depends(get_db)
):
    """Получить игрока по никнейму"""
    service = PlayerService(db)
    return service.get_player_by_nickname(nickname)


@router.put("/{player_id}", response_model=PlayerResponse)
def update_player(
    player_id: int,
    player_data: PlayerUpdate,
    db: Session = Depends(get_db)
):
    """Обновить данные игрока"""
    service = PlayerService(db)
    return service.update_player(player_id, player_data)


@router.delete("/{player_id}", status_code=status.HTTP_200_OK)
def delete_player(
    player_id: int,
    db: Session = Depends(get_db)
):
    """Удалить игрока"""
    service = PlayerService(db)
    return service.delete_player(player_id)