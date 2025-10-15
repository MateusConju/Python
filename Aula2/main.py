# usuarios = ["Ana", "Bruno", "Carla"]
# usuarios.append("Daniel")
# usuarios.insert("1", "Beatriz")
# usuarios.remove("Carla")
# ultimo = usuarios.pop()
# position = usuarios.index("Bruno")
# usuarios[usuarios.index("Beatriz")] = "Beata"
# print(usuarios)
# print(position)
# print(ultimo)

# coordenadas = (10.5, -23.5)
# coordenadas[0] = 11.0

# def obter_usuario():
#     return ("Eduardo", 30, "Masculino")

# nome, idade, genero = obter_usuario()
# print(nome, idade, genero)

tecnologias = {"Python", "Java", "JavaScript", "Python"}
print(tecnologias)


# Operações de conjuntos
backend_devs = {"Ana", "Bruno", "Carlos"}
frontend_devs = {"Bruno", "Diana", "Elena"}

# Interseção (quem faz ambos?)
fullstack = backend_devs & frontend_devs  # {'Bruno'}

# União (todos os devs)
todos_devs = backend_devs | frontend_devs

# Diferença (só backend)
so_backend = backend_devs - frontend_devs  # {'Ana', 'Carlos'}
