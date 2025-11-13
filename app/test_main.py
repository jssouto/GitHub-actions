from app.main import saludo

def test_saludo_output(capsys):
    saludo()
    captured = capsys.readouterr()
    assert "Hola Jorge" in captured.out
