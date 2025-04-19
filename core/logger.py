import logging
import pathlib
from logging.config import dictConfig

def setup_logging():
    LOGS_DIR = pathlib.Path(__file__).resolve().parent.parent / "logs"
    LOGS_DIR.mkdir(exist_ok=True)
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(levelname)-8s | %(name)-15s | %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "standard",
                "filename": str(LOGS_DIR / "bot.log"),
                "encoding": "utf-8"
            }
        },
        "loggers": {
            "bot": {
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False
            }
        }
    })