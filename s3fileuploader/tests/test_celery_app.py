from s3fileuploader.celery_app import celery


def test_celery_redis_configured():
    assert celery.conf.get('broker_url') == 'redis://localhost:6379/0'
    assert celery.conf.get('result_backend') == 'redis://localhost:6379/0'
