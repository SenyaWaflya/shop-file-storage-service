from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_API_URL: str
    MINIO_MAX_POOL_CONNECTIONS: int
    MINIO_RETRY_ATTEMPTS: int
    MINIO_BUCKET: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
