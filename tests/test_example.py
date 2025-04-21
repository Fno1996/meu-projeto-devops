def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5

def test_soma_negativo():
    assert soma(-2, -3) == -5

def test_soma_zero():
    assert soma(0, 0) == 0

def test_soma_misto():
    assert soma(-2, 5) == 3

def test_soma_tipo_errado():
    try:
        soma("2", 3)
    except TypeError:
        pass  # Esperamos um erro de tipo...
