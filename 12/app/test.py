from hashlib import md5

class MockDB:
    banco_senhas = {
        "admin":"e10adc3949ba59abbe56e057f20f883e"
    }

# Pedindo para o usuário as suas credenciais
user = input('Digite o usuário:\n> ')
password = input('Digite sua senha:\n> ')

# Hasheado a credencial
encoded_pass = password.encode('utf-8')
md5_object = md5(encoded_pass)

# Validação
user_password = MockDB.banco_senhas.get(user)
if user_password is None:
    print('Usuário está inválido!')
    exit()

if user_password != md5_object.hexdigest():
    print('Senha está inválida!')
    exit()

print('Entrou!')
