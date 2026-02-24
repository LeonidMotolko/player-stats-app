from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(Integer, ForeignKey('players.id'), index=True, nullable=False)
    player2_id = Column(Integer, ForeignKey('players.id'), index=True, nullable=False)
    winner_id = Column(Integer, ForeignKey('players.id'), index=True, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<Match {self.id}: Player {self.player1_id} vs Player {self.player2_id}>"