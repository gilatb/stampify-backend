from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Stampify"
    service_host: str = "localhost"
    service_port: int = 8000
    log_level: str = "INFO"
    autoreload: bool = True


settings = Settings()
