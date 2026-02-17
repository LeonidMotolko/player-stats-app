from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base

# Создаем таблицы в БД (будем использовать миграции)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/")
def root():
    return {
        "message": "Player Statistics API",
        "status": "running",
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected"  # Позже добавим реальную проверку БД
    }

# Здесь будем подключать роутеры
# app.include_router(player_router, prefix="/api/v1/players", tags=["players"])
