import logging


class Logger:

    @classmethod
    def setup(cls):
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"
        )

        cls.logger = logging.getLogger()
        cls.__create_handlers(formatter)

    @classmethod
    def __create_handlers(cls, formatter: logging.Formatter):
        view_handler = logging.FileHandler("logs_view.log")
        view_handler.setLevel(logging.INFO)
        view_handler.setFormatter(formatter)
        cls.logger.addHandler(view_handler)

        domain_handler = logging.FileHandler("logs_domain.log")
        domain_handler.setLevel(logging.DEBUG)
        domain_handler.setFormatter(formatter)
        cls.logger.addHandler(domain_handler)

        presenter_handler = logging.FileHandler("logs_presenter.log")
        presenter_handler.setLevel(logging.DEBUG)
        presenter_handler.setFormatter(formatter)
        cls.logger.addHandler(presenter_handler)

        infra_handler = logging.FileHandler("logs_infra.log")
        infra_handler.setLevel(logging.INFO)
        infra_handler.setFormatter(formatter)
        cls.logger.addHandler(infra_handler)

    @classmethod
    def log_debug(cls, message: str, *args, **kwargs):
        cls.logger.debug(message.format(*args, **kwargs))

    @classmethod
    def log_info(cls, message: str, *args, **kwargs):
        cls.logger.info(message.format(*args, **kwargs))

    @classmethod
    def log_warning(cls, message: str, *args, **kwargs):
        cls.logger.warning(message.format(*args, **kwargs))

    @classmethod
    def log_error(cls, message: str, *args, **kwargs):
        cls.logger.error(message.format(*args, **kwargs))
