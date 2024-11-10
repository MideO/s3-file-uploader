from ..src.dependency_factory import dependencies


def test_dependency_factory_celery_app():
    app = dependencies.celery
    assert app.conf.get("broker_url") == "redis://localhost:6379/0"
    assert app.conf.get("result_backend") == "redis://localhost:6379/0"
