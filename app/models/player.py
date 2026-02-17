from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.config import settings


from app.core.database import Base

#создание таблицы игрока
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key = True, index = True)
    nickname = Column(String, unique = True, index = True, nullable = False)
    rating = Column(Integer, default = settings.ELO_DEFAULT_RATING, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())

    def __repr__(self):
        return f"<Player {self.nickname}>"