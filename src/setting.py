from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения"""


settings = Settings()
