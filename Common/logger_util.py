import logging


def error_log(message):
    """
    error等级日志
    :param message:
    :return: 错误日志
    """
    logger = logging.getLogger(__name__)
    logger.error(message)
    raise Exception(message)


def info_log(message):
    """
    info等级日志
    :param message:
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.info(message)


def debug_log(message):
    """
    debug等级日志
    :param message:
    :return:
    """
    looger = logging.getLogger(__name__)
    looger.debug(message)


def warning_log(message):
    """
    warning等级日志
    :param message:
    :return:
    """
    looger = logging.getLogger(__name__)
    looger.warning(message)

