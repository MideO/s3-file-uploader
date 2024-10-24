import os
from unittest.mock import patch

from s3fileuploader.config.config import Config
from s3fileuploader.config.logging_config import LoggingConfig
from s3fileuploader.config.url_config import RedisConfig, AppConfig


def test_config_with_defaults():
    config = Config()
    assert config.logging == LoggingConfig()
    assert config.redis == RedisConfig()
    assert config.app == AppConfig()
    assert config.secret == 'change me'


@patch.dict(
    os.environ,
    {
        "LOG_LEVEL": "DEBUG",
        "REDIS_HOST": "redis",
        "REDIS_PORT": "6379",
        "APP_HOST": "0.0.0.0",
        "APP_PORT": "9000",
        "APP_SECRET": "super secret",

    },
    clear=True,
)
def test_config_with_environment_variables():
    config = Config()
    assert config.secret == 'super secret'
    assert config.logging.level == 'DEBUG'
    assert config.redis.url == 'redis://redis:6379/0'
    assert config.app.url == 'http://0.0.0.0:9000'
