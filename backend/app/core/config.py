from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    jwt_secret: str
    llm_base_url: str = "http:ollama:11434"
    llm_model: str = "qwen2.5:3b"
    embedding_model: str = "intfloat/multilingual-e5-small"


settings = Settings()
