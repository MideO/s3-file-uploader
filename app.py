import logging
from logging.config import dictConfig

from flask import Flask
from gevent.pywsgi import WSGIServer

from s3fileuploader.config import app_config
from s3fileuploader.views import index
app = Flask(
    __name__,
    template_folder='/s3fileuploader/templates',
    static_folder='/s3fileuploader/static'
)
app.secret_key = app_config.secret


# logging configuration
dictConfig(app_config.logging.config)

# Celery configuration
app.config['CELERY_BROKER_URL'] = app_config.redis.url
app.config['CELERY_RESULT_BACKEND'] = app_config.redis.url

app.register_blueprint(index)

if __name__ == "__main__":
    http_server = WSGIServer(
        (app_config.app.host, app_config.app.port), app,
        log=app.logger,
        error_log=app.logger,
    )
    http_server.log.info(f"* Running on {app_config.app.url}")
    http_server.serve_forever()
