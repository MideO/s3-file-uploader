from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .aws import AwsConfig
from .logging_config import LoggingConfig
from .url_config import RedisConfig, AppConfig


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="_")
    secret: str = Field(default="change me")
    storage_path: str = Field(default="/shared_data/")
    logging: LoggingConfig = Field(default=LoggingConfig())
    redis: RedisConfig = Field(default=RedisConfig())
    app: AppConfig = Field(default=AppConfig())
    aws: AwsConfig = Field(default=AwsConfig())
