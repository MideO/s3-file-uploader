from pydantic import BaseModel


class LoggingConfig(BaseModel):
    format: str = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    stream: str = "ext://sys.stdout"
    level: str = "INFO"

    @property
    def config(self):
        return {
            "version": 1,
            "formatters": {
                "default": {
                    "format": self.format,
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "stream": self.stream,
                    "formatter": "default",
                }
            },
            "loggers": {"app": {"level": self.level, "handlers": ["default"]}},
        }
