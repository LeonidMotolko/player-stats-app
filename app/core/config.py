from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional

class Settings(BaseSettings):
    #база данных
    DATABASE_URL: str = "sqlite:///./test.db"
    
    #настройки приложения
    PROJECT_NAME: str = "Player Statistics Service"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    
    #настройки рейтинга ELO
    ELO_K_FACTOR: int = 32
    ELO_DEFAULT_RATING: int = 1000
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()
