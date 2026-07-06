from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "ResumeRank AI"
    API_VERSION: str = "v1"

    DATABASE_URL: str = "sqlite:///./resumerank.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()