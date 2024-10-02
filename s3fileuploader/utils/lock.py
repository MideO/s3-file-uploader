from s3fileuploader.dao import redis


class LockAlreadyAcquiredError(Exception):
    pass


class Lock:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        if redis.get(self.name):
            raise LockAlreadyAcquiredError(
                f"lock: {self.name} already exist"
            )
        redis.set(name=self.name, value=1, nx=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        redis.delete(self.name)
