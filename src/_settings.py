from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.constants import ENV_PATH

load_dotenv()


class Settings(BaseSettings):
    CHECK_INTERVAL: int = 60
    PROXY_CHECK_URL: str = "https://some-url.com"

    DEBUG: bool = False

    model_config = SettingsConfigDict(extra="ignore")


def settings_factory() -> Settings:
    return Settings(_env_file=ENV_PATH)
