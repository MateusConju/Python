from test_module import calcular_dobro

def test_calc_double():
    resposta = calcular_dobro(50)

    assert resposta == 100