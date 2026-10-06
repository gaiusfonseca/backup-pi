#! /usr/bin/python
# usage: ./backup.py path
# path is the path to a text file (.txt) containing the absolute path to all folders you want to backup

import logging, os, sys, zipfile

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

def get_file_contents(path):
    with open(path, 'r', encoding="utf-8")as file:
        return [line.rstrip('\n') for line in file]

def main():    
    if not has_argument(sys.argv):
        print("at least one argument must be specified. supply the text file containing the folders to backup.")
        sys.exit(1)

    path = sys.argv[1]

    if not path_exists(path):
        print(f"the supplied path {path} does not exist.")
        sys.exit(1)

    if not is_file(path):
        print(f"the supplied path '{path}' does not point to a file.")
        sys.exit(1)

    if not is_txt_extension(path):
        print(f"'{path}' does not have a '.txt' extension")
        sys.exit(1)

    archive = zipfile.ZipFile("backup.zip", "w")

    folders = get_file_contents(path)
    for folder in folders:
        for (parent_folder, subfolders, files) in os.walk(folder):
            for file in files:
                file_path = os.path.join(parent_folder, file)
                archive.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
                print(file_path + " was added to the archive.")

    archive.close()

if __name__ == "__main__":
    main()