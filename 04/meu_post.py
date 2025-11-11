from requests import post

email = 'medeva9091@delaeb.com'
senha_errada = '123456'
senha = 'MinhaS3nhaF0rte'


def login(URL:str, login:str, senha:str):
    payload = {
        'user[login]':login,
        'user[password]':senha,
        'commit': 'Log in'
        }
    response = post(URL, payload, allow_redirects=False)
    print(response.status_code)

login('https://users.nexusmods.com/auth/sign_in', 'medeva9091@delaeb.com', senha)
