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

# verifies if the path exists
def path_exists(path):
    return os.path.exists(path)

# verifies if it's a file
def is_file(path):
    return os.path.isfile(path)

# verifies if the extension is .txt
def is_txt_extension(path):
    basename = str(os.path.basename(path))
    return basename.lower().endswith(".txt")
    
