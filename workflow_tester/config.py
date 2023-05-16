import dataclasses
from functools import lru_cache
from pydantic import BaseSettings

import playback


@dataclasses.dataclass
class Configuration:
    settings: BaseSettings
    player: playback.Player


class Settings(BaseSettings):
    message: str = 'App env'
    playback_file: str
    mss: str
    sid: str
    log_level: str


@lru_cache()
def get_config() -> Configuration:
    settings = Settings()
    return Configuration(settings, playback.Player(settings.playback_file))
