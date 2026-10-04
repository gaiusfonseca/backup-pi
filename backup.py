#! /usr/bin/python
# usage: ./backup.py path
# path is the path to a text file (.txt) containing the absolute path to all folders you want to backup

import logging, os

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
# logger.disable(logging.CRITICAL)

# verifies if an argument was passed
def has_argument(argument):
    if len(argument) == 2:
        return True

    return False


