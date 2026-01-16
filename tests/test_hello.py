import pytest
from src.modules.hello import say_hello


def test_say_hello_valid():
    assert say_hello("Alice") == "Hello, Alice!"


def test_say_hello_empty_name():
    with pytest.raises(ValueError):
        say_hello("")
