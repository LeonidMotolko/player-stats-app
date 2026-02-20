from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.routers import player_router

# Создаем таблицы в БД (будем использовать миграции)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(player_router.router, prefix="/api/v1")

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

