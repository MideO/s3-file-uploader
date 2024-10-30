import os

from pydantic import BaseModel

from . import environment_variables_names as variable_names
from .aws import AwsConfig
from .logging_config import LoggingConfig
from .url_config import RedisConfig, AppConfig


def _from_env(key: str, fallback):
    return os.environ.get(key, fallback)


class Config(BaseModel):
    secret: str = 'change me'
    logging: LoggingConfig = LoggingConfig()
    redis: RedisConfig = RedisConfig()
    app: AppConfig = AppConfig()
    aws: AwsConfig = AwsConfig()

    def model_post_init(self, __context) -> None:
        self.secret = _from_env(variable_names.APP_SECRET, self.secret)
        self.logging.level = _from_env(variable_names.LOG_LEVEL, self.logging.level)
        self.redis.host = _from_env(variable_names.REDIS_HOST, self.redis.host)
        self.redis.port = int(_from_env(variable_names.REDIS_PORT, self.redis.port))
        self.app.host = _from_env(variable_names.APP_HOST, self.app.host)
        self.app.port = int(_from_env(variable_names.APP_PORT, self.app.port))
        self.aws.region = _from_env(variable_names.AWS_DEFAULT_REGION, self.aws.region)
        self.aws.endpoint = _from_env(variable_names.AWS_DEFAULT_ENDPOINT, self.aws.endpoint)
