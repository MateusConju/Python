# HTTP
# REST == Representational State Transfer
#
# GET - Ler/Buscar algo em um servidor
#
# POST - Criar um novo recurso
#
# PUT - Substituir/Atualizar um recurso
#
# PATCH - Atualizar parcialmente um recurso
#
# DELETE - Remover um recurso

# Status Codes
#
# 200 - Sucesso
# 300 - Redirecionamento
# 400 - Erro
# 500 - Server Error
#
# 404 - Não Encontrado
# 403 - Proibido
# 200 - OK
# 201 - Creado com sucesso
# 401 - Não autorizado
# 500 - Internal Server Error
# 204 - Sem conteúdo
import requests

URL = 'https://www.fiap.com.br/fhjdsajhjkajfhjadsjfhjsahfjkhsjadfjkahsdf/'

# GET
print('Método: GET')
resposta_fiap = requests.get(URL)
print(f'Objeto: {resposta_fiap}')
print(f'Status Code: {resposta_fiap.status_code}')


# POST
print('Método: POST')
URL_POST = 'https://www.fiap.com.br/api/moodle/'
payload = {'x':0}
post_fiap = requests.get(URL_POST, payload)
print(f'Objeto: {post_fiap}')
print(f'Status Code: {post_fiap.status_code}')
