from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    groq_api_key: str = ""
    gnews_api_key: str = ""
    newsdata_api_key: str = ""
    allowed_origins: str = "http://localhost:5500,http://127.0.0.1:5500"
    env: str = "development"


settings = Settings()
