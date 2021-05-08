import logging

class LoggerMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=LoggerMeta):
    def config(self, filename, level, format, datefmt):
        # TODO: Implement loggin level
        logging.basicConfig(filename=filename,
                    level=logging.INFO,
                    format=format,
                    datefmt=datefmt)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def debug(self, message):
        logging.debug(message)

    def exception(self, message):
        logging.exception(message)

    def error(self, message):
        logging.error(message)