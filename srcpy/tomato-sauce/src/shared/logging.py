import logging
import sys
import inspect

_get_function = lambda: inspect.stack()[2].function


def init_logging(level=None):
    level = logging.WARN if level is None else level
    logger = logging.getLogger()
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    info("Logging Interface now initialized")


def debug(message: str, *args):
    logging.debug(f"{_get_function()} - {message}", *args)


def info(message: str, *args):
    logging.info(f"{_get_function()} - {message}", *args)


def error(message: str, *args):
    logging.error(f"{_get_function()} - {message}", *args)


def warn(message: str, *args):
    logging.warn(f"{_get_function()} - {message}", *args)
