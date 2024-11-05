from unittest.mock import patch, MagicMock

from ...src.clients import redis_client


def test_redis():
    with patch("s3fileuploader.src.clients.redis.Redis", MagicMock()) as mock_redis:
        redis_client("localhost", 6379)

        mock_redis.assert_called()
        mock_redis.assert_called_with(host="localhost", port=6379)
