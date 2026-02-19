from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.services.player_service import PlayerService
from app.schemas.player import PlayerCreate, PlayerResponse, PlayerUpdate


