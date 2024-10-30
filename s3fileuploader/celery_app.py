from celery import Celery

from s3fileuploader.config import app_config

celery = Celery(
    __name__,
    broker=app_config.redis.url,
    backend=app_config.redis.url,
)
