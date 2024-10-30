from s3fileuploader.config.url_config import RedisConfig, AppConfig


def test_redis_config():
    redis = RedisConfig()
    assert redis.host == "localhost"
    assert redis.port == 6379
    assert redis.url == "redis://localhost:6379/0"


def test_app_config():
    app_config = AppConfig()
    assert app_config.host == "localhost"
    assert app_config.port == 9000
    assert app_config.url == "http://localhost:9000"
