from passlib.context import CryptContext
from time import sleep

contexto_senha = CryptContext(schemes=['bcrypt'], deprecated='auto')

'''
Dada a seguinte hash: $2b$12$XfxESPJe0Fc8jYtBbtJss.nd1/Epv6PfLy7bPhHd0MnK5Uj/3AbQG

Utilize um script que identificará qual é a senha dessa Hash, levando em conta a seguinte wordlist:

senha
123456
minhasenha
adminadmin
mudar1234
'''
HASH = '$2b$12$XfxESPJe0Fc8jYtBbtJss.nd1/Epv6PfLy7bPhHd0MnK5Uj/3AbQG'
def verificador(senha_limpa:str, senha_hasheada:str) -> bool:
    return contexto_senha.verify(senha_limpa, senha_hasheada)

lista_senhas = ['senha','123456','minhasenha','adminadmin','mudar1234']
tamanho_senhas = len(lista_senhas)
for i, senha in enumerate(lista_senhas):
    print(f'({i+1}/{tamanho_senhas}) Testando: {senha}                  ', end='\r')
    is_password = verificador(senha,HASH)
    if is_password: 
        print(f'Senha Encontrada! > {senha}')
        exit()
