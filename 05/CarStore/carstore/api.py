from requests import get
URL = 'https://parallelum.com.br/fipe/api/v1'
def connect():
    response = get('URL/carros/marcas')
    return True if response.status_code == 200 else False

def retrieve(**argumentos):
    veiculo = argumentos.get('veiculo')
    marca = argumentos.get('marca')
    modelo = argumentos.get('modelo')
    ano = argumentos.get('ano')

    if not veiculo: return '{\'erro\':\'NOT_FOUND\'}'
    if not marca: connection = f'{URL}/carros/marcas'
    elif not modelo: connection = f'{URL}/{veiculo}/marcas/{marca}/modelos'
    elif not ano: connection = f'{URL}/{veiculo}/marcas/{marca}/modelos/{modelo}/anos'
    else: connection = f'{URL}/{veiculo}/marcas/{marca}/modelos/{modelo}/anos/{ano}'

    return get(connection)

# print(retrieve(veiculo='carros', marca=171, modelo=9521, ano='2021-1'))