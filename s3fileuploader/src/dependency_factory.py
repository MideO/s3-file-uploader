from celery import Celery

from clients import s3_client, redis_client
from config import Config
from tasks.upload import UploadTask
from utils.lock import Lock


class DependencyFactory:
    def __init__(self, config: Config):
        self.config: Config = config
        self.celery: Celery = Celery(
            "s3fileuploaderCelery",
            broker=self.config.redis.url,
            backend=self.config.redis.url,
        )
        # Register tasks
        self.upload_task: UploadTask = UploadTask(
            s3_client(config.aws.region, config.aws.endpoint),
            lambda x: Lock(x, redis_client(config.redis.host, config.redis.port)),
        )
        self.celery.register_task(self.upload_task)


dependencies = DependencyFactory(Config())
