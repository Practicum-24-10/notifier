from pydantic import BaseSettings


class TestSettings(BaseSettings):
    service_url: str = "http://localhost:8000/api/v1/event/"


test_settings = TestSettings()
