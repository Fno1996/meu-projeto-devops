def soma(a, b):
    resultado = a + b
    print(f"soma({a}, {b}) = {resultado}")
    return resultado

def test_soma():
    resultado = soma(2, 3)
    assert resultado == 5

def test_soma_negativo():
    resultado = soma(-2, -3)
    assert resultado == -5

def test_soma_zero():
    resultado = soma(0, 0)
    assert resultado == 0

def test_soma_misto():
    resultado = soma(-2, 5)
    assert resultado == 3

def test_soma_tipo_errado():
    try:
        soma("2", 3)
    except TypeError as e:
        print(f"Erro esperado: {e}")
        pass  # Esperamos um erro de tipo...
