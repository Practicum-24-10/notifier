from pydantic import Field
from pydantic_settings import BaseSettings


class MainSettings(BaseSettings):
    class Config:
        env_file = 'sender/.env'
        env_file_encoding = 'utf-8'


class AppSettings(MainSettings):
    sending_queue: str = "queue"
    rabbit_url: str = "url"


class PostgresSettings(MainSettings):
    dbname: str = Field('notifications', env='POSTGRES_DB')
    user: str = Field('admin', env='POSTGRES_USER')
    password: str = Field('123qwe', env='POSTGRES_PASSWORD')
    host: str = Field('notifications-db', env='POSTGRES_HOST')
    port: int = Field(5432, env='POSTGRES_PORT')


class EmailServerSettings(MainSettings):
    address: str = Field('smtp.yandex.ru', env='EMAIL_SERVER_ADDRESS')
    port: int = Field(465, env='EMAIL_SERVER_PORT')
    login: str = Field('test', env='EMAIL_ACCOUNT_LOGIN')
    password: str = Field('test', env='EMAIL_ACCOUNT_PASSWORD')


config = AppSettings()
postgres_config = PostgresSettings()
email_service_config = EmailServerSettings()
