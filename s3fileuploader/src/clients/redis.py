from redis import Redis


def redis_client(host: str, port: int) -> Redis:
    return Redis(host=host, port=port)
