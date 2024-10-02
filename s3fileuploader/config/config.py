import os

from pydantic import BaseModel

from s3fileuploader.config.logging_config import LoggingConfig
from s3fileuploader.config.url_config import RedisConfig, AppConfig

LOG_LEVEL = "LOG_LEVEL"
REDIS_HOST = "REDIS_HOST"
REDIS_PORT = "REDIS_PORT"
APP_HOST = "APP_HOST"
APP_PORT = "APP_PORT"
APP_SECRET = "APP_SECRET"


def _from_env(key: str, fallback):
    return os.environ.get(key, fallback)


class Config(BaseModel):
    secret: str = 'change me'
    logging: LoggingConfig = LoggingConfig()
    redis: RedisConfig = RedisConfig()
    app: AppConfig = AppConfig()

    def model_post_init(self, __context) -> None:
        self.secret = _from_env(APP_SECRET, self.secret)
        self.logging.level = _from_env(LOG_LEVEL, self.logging.level)
        self.redis.host = _from_env(REDIS_HOST, self.redis.host)
        self.redis.port = int(_from_env(REDIS_PORT, self.redis.port))
        self.app.host = _from_env(APP_HOST, self.app.host)
        self.app.port = int(_from_env(APP_PORT, self.app.port))
