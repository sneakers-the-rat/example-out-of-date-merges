from example.main import main

def test_main(capsys):
    strings = ("a", "b", "c")

    main(strings)

    out = capsys.readouterr().out

    assert str(strings) in out
    assert '.'.join(strings) in out