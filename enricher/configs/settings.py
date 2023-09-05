from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    enrichment_queue: str = "queue"
    sending_queue: str = "queue"
    rabbit_url: str = "url"
    auth_url: str = 'url'
    auth_token: str = 'token'
    loglevel: str = 'INFO'

    model_config = SettingsConfigDict(
        env_file="enricher/.env", env_file_encoding="utf-8", extra='ignore'
    )


class PgSettings(BaseSettings):
    dbname: str = 'str'
    user: str = 'str'
    password: str = 'str'
    host: str = 'str'
    port: int = 111

    model_config = SettingsConfigDict(
        env_file="enricher/.env", env_file_encoding="utf-8", extra='ignore'
    )


config = AppSettings()

pg_config = PgSettings()
