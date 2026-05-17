from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TAGGING_", env_file=".env", extra="ignore")

    storage_backend: str = Field(default="local")
    local_storage_dir: str = Field(default="data/documents")
    default_ocr_engine: str = Field(default="paddle")
    max_description_sentences: int = Field(default=2)


settings = Settings()
