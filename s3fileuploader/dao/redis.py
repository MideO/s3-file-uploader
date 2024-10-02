# Redis
from redis import Redis

from s3fileuploader.config import app_config

redis = Redis(host=app_config.redis.host, port=app_config.redis.port)
