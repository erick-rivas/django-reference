"""
__Seed builder__
  (Read_only) Logging util
"""
import logging


def info(message):
    logger = logging.getLogger('seed_logger')
    logger.info(message)


def warning(message):
    logger = logging.getLogger('seed_logger')
    logger.warning(message)


def error(message):
    logger = logging.getLogger('seed_logger')
    logger.error(message)