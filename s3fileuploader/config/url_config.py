from pydantic import BaseModel


class _UrlConfig(BaseModel):
    host: str
    port: int
    scheme: str

    @property
    def url(self):
        return f"{self.scheme}://{self.host}:{self.port}"


class RedisConfig(_UrlConfig):
    host: str = 'localhost'
    port: int = 6379
    scheme: str = 'redis'

    @property
    def url(self):
        return f"{super().url}/0"


class AppConfig(_UrlConfig):
    host: str = 'localhost'
    port: int = 9000
    scheme: str = 'http'
