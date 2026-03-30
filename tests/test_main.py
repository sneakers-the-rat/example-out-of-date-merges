from example.main import main

import pytest

@pytest.mark.parametrize("print_strings", (False, True))
def test_main(capsys, print_strings):
    strings = ("a", "b", "c")

    if print_strings:
        main([*strings, "--print"])
    else:
        main(strings)

    out = capsys.readouterr().out

    assert bool(str(strings) in out) == print_strings
    assert '.'.join(strings) in out