import io
import os
from contextlib import redirect_stdout

import pytest

from process_files import search_term


CONTENT = """import pytest
import datetime

x = 1"""


# Fixture using `tmp_path`
# https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html
@pytest.fixture
def filename(tmp_path):  # fixture requires another fixture
    filename = "testfile.txt"
    f = tmp_path / filename
    f.write_text(CONTENT)
    return str(tmp_path / filename)


# This one was done without `tmp_path` in order to show fixture tear down
@pytest.fixture(scope="module")
def filename_unicode():
    filename = "testfile_unicode.txt"
    with open(filename, "wb") as f:
        f.write(b"u = \xae\xe2\xf0\xc4")
    yield filename
    os.remove(filename)


def test_search_term_found(filename):
    with redirect_stdout(io.StringIO()) as f:
        search_term(filename, "import")
    output = f.getvalue()
    assert output == "import pytest\nimport datetime\n"


def test_search_term_not_found(filename):
    with redirect_stdout(io.StringIO()) as f:
        search_term(filename, "hello")
    output = f.getvalue()
    assert output == ""


def test_search_term_decode_error(filename_unicode):
    with redirect_stdout(io.StringIO()) as f:
        search_term(filename_unicode, "hello")
    output = f.getvalue()
    assert output == ("'utf-8' codec can't decode byte 0xae in position 4: "
                      "invalid start byte testfile_unicode.txt\n")
