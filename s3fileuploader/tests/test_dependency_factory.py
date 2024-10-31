from s3fileuploader.src.dependency_factory import dependencies


def test_dependency_factory_s3_service_returns_same_instance_always():
    ins1 = dependencies.s3_service()
    ins2 = dependencies.s3_service()
    assert repr(ins1) == repr(ins2)


def test_dependency_factory_celery_app():
    app = dependencies.celery("my_celery_app")
    assert app.conf.get("broker_url") == "redis://localhost:6379/0"
    assert app.conf.get("result_backend") == "redis://localhost:6379/0"
