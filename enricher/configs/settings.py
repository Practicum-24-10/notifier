from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    enrichment_queue: str = "queue"
    sending_queue: str = "queue"
    rabbit_url: str = "url"

    model_config = SettingsConfigDict(env_file='enricher/.env', env_file_encoding='utf-8')


config = AppSettings()
