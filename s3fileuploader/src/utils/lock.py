import logging

from redis import Redis

LOG = logging.getLogger("app")


class LockAlreadyAcquiredError(Exception):
    pass


class Lock:
    def __init__(self, name, redis: Redis):
        self.name: str = name
        self.redis: Redis = redis

    def __enter__(self):
        if self.redis.get(self.name):
            raise LockAlreadyAcquiredError(f"lock: {self.name} already exist")
        self.redis.set(name=self.name, value=1, nx=True)
        LOG.info("Lock created %s", self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.redis.delete(self.name)
        LOG.info("Released Lock %s", self.name)
