from time import sleep

def get_current_user(token:str):
    sleep(2) # Simulando arquivos(ou bancos de dados) sendo lidos
    return {"username":"admin_real", "role":"admin"}