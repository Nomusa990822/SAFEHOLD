from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SAFEHOLD"
    environment: str = "development"

    database_url: str = ""

    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    ai_api_key: str = ""

    storage_bucket: str = ""
    storage_access_key: str = ""
    storage_secret_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
