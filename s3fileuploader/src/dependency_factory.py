from celery import Celery

from clients import s3_client, redis_client
from config import Config
from services.aws import AwsS3Service
from utils.lock import Lock


class DependencyFactory:
    def __init__(self, config: Config):
        self.config: Config = config
        self._s3_service: AwsS3Service = AwsS3Service(
            s3_client(config.aws.region, config.aws.endpoint),
            lambda x: Lock(x, redis_client(config.redis.host, config.redis.port)),
        )

    def s3_service(self):
        return self._s3_service

    def celery(self, name: str):
        return Celery(
            name,
            broker=self.config.redis.url,
            backend=self.config.redis.url,
        )


dependencies = DependencyFactory(Config())
