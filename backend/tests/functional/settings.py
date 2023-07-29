from pydantic import BaseSettings


class TestSettings(BaseSettings):
    service_url: str = "http://localhost/api/v1/"


test_settings = TestSettings()
