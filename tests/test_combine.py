import pytest

from example.combine import combine_strings

@pytest.mark.parametrize("print_strings", (False, True))
def test_combine(print_strings, capsys):
    strings = ("a", "b", "c")
    sep = "."

    result = combine_strings(*strings, sep=sep, print_strings=print_strings)

    assert result == sep.join(strings)

    captured = capsys.readouterr()
    if print_strings:
        assert str(strings) in captured.out
    else:
        assert str(strings) not in captured.out

