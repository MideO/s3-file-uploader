from ...src.config.logging_config import LoggingConfig


def test_logging_config():
    logging = LoggingConfig()
    assert logging.format == "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    assert logging.stream == "ext://sys.stdout"
    assert logging.level == "INFO"
    assert logging.config == {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "loggers": {"app": {"handlers": ["default"], "level": "INFO"}},
    }
