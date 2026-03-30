import pytest

from example.combine import combine_strings

def test_combine():
    strings = ("a", "b", "c")
    sep = "."

    result = combine_strings(*strings, sep=sep)

    assert result == sep.join(strings)
