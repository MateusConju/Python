# **Briefing do Exercício:**

# > **Cenário Real:** Você foi contratado para criar um módulo de gerenciamento de funcionários para um sistema de RH. O sistema precisa:
# > 

# > 
# > 

# > 1. Cadastrar funcionários (nome, cargo, salário)
# > 

# > 2. Calcular bônus anual (10% do salário para todos)
# > 

# > 3. Listar funcionários por cargo
# > 

# > 4. Calcular folha de pagamento total
# > 

# > 
# > 

# > **Requisitos Técnicos:**
# - Use uma classe `Funcionario`
# - Crie funções auxiliares em um módulo separado
# - Implemente validações (salário > 0, nome não vazio)
# - Use type hints
# >
# # funcionario.py
# class Funcionario:
#     def __init__(self, nome: str, cargo: str, salario: float):
#         # TODO: Implementar validações e inicialização
#         pass
    
#     def calcular_bonus(self) -> float:
#         # TODO: Calcular 10% do salário
#         pass

# # gerenciador.py
# def adicionar_funcionario(lista: list, funcionario):
#     # TODO: Adicionar à lista
#     pass

# def listar_por_cargo(lista: list, cargo: str) -> list:
#     # TODO: Filtrar funcionários por cargo
#     pass

# def calcular_folha_total(lista: list) -> float:
#     # TODO: Somar salários + bônus
#     pass
# **Critérios de Avaliação:**
# ✅ Código funcional e sem erros
# ✅ Uso correto de POO (atributos, métodos)
# ✅ Validações implementadas
# ✅ Type hints presentes

# **Tempo:** 20 minutos para implementação
# **Formato:** Individual, mas podem tirar dúvidas no chat/com professor

from typing import List
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if salario <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        
        self.nome: str = nome
        self.cargo: str = cargo
        self.salario: float = salario

    def calcular_bonus(self) -> float:
        return self.salario * 0.10

    def __repr__(self):
        return f"Funcionario(nome='{self.nome}', cargo='{self.cargo}', salario={self.salario:.2f})"

def adicionar_funcionario(lista: List[Funcionario], funcionario: Funcionario) -> None:
    lista.append(funcionario)

def listar_por_cargo(lista: List[Funcionario], cargo: str) -> List[Funcionario]:
    return [f for f in lista if f.cargo.lower() == cargo.lower()]

def calcular_folha_total(lista: List[Funcionario]) -> float:
    total = 0.0
    for f in lista:
        total += f.salario + f.calcular_bonus()
    return total

if __name__ == "__main__":
    funcionarios: List[Funcionario] = []

    f1 = Funcionario("Ana", "Desenvolvedora", 5000)
    f2 = Funcionario("Carlos", "Gerente", 8000)
    f3 = Funcionario("João", "Desenvolvedora", 5500)

    adicionar_funcionario(funcionarios, f1)
    adicionar_funcionario(funcionarios, f2)
    adicionar_funcionario(funcionarios, f3)

    print("Desenvolvedores:", listar_por_cargo(funcionarios, "Desenvolvedora"))

    print("Folha total:", calcular_folha_total(funcionarios))
