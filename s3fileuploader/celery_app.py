from celery import Celery

from app import app
from s3fileuploader.config import app_config

celery = Celery(
    app.import_name,
    broker=app_config.redis.url,
    backend=app_config.redis.url,
)
celery.conf.update(app.config)
