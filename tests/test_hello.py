import sys
sys.path.append("/mnt/c/Users/HOME/Downloads/mlops-course/pytest-tips-tricks")

from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_goodbye():
    assert "bye" == more_goodbye()
