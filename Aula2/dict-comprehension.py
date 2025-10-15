quadrados = {x: x**2 for x in range(5)}
# print(quadrados)

config_default = {"timeout": 30, "retries": 3}
config_usuario = {"timeout": 60, "retries": 3}
config_final = config_default | config_usuario
print(config_final)