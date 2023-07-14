import os
import pytest
from print_hello_service import print_hello  # replace with the name of your python file


def test_return_hello():
    assert print_hello.return_hello() == 'hello'
