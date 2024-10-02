from s3fileuploader.config.logging_config import LoggingConfig


def test_logging_config():
    logging = LoggingConfig()
    assert logging.format == '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    assert logging.stream == 'ext://sys.stdout'
    assert logging.level == 'INFO'
    assert logging.config == {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }
