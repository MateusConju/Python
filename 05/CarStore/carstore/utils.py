from argparse import ArgumentParser

def retorna_argumentos():
    argumentos = ArgumentParser(
        'Carstore',
        'carstore.py -t carro -b Lamborghini - m Aventador - y 2020-1',
        'Busca carro e seus preços para a venda'
    )
    argumentos.add_argument('b', '--brand')