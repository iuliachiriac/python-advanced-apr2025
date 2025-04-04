import glob
import logging
import time
from pathlib import Path


logger = logging.getLogger("main")
logging.basicConfig(filename='ex_10_1.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
)


def search_term(filename, term):
    with open(filename, "r") as f:
        try:
            for line in f:
                if term in line:
                    logger.info(line.rstrip())
        except UnicodeDecodeError:
            logger.error("Exception occurred in %s",
                         filename, exc_info=True)


def find_files(path, extension, /, *, recursive=False):
    pattern = Path(path)
    if recursive:
        pattern /= "**"
    pattern /= f"*.{extension}"
    return glob.iglob(str(pattern), recursive=recursive, include_hidden=True)


def search_across_files(root_path, file_extension, term):
    files_count = 0
    for filename in find_files(root_path, file_extension, recursive=True):
        logger.debug("Searching %s in %s...", term, filename)
        search_term(filename, term)
        files_count += 1
    logger.debug("Searched in %d files", files_count)


if __name__ == "__main__":
    time_start = time.time()
    search_across_files(".", "py", "import")
    time_diff = time.time() - time_start
    logger.info("Execution took %s.", time_diff)
