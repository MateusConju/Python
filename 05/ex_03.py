'''
 ________
|> EX03 <|
Crie uma classe Cliente para um e-commerce. O construtor (__init__) deve receber 

- nome (str)
- email (str)

Ele também deve definir um atributo interno |> self.carrinho | que deve ser inicializado como uma lista vazia.
'''
produtos_lista = [{'arroz': 6.80},{'feijão': 8.50},{'macarrão espaguete': 3.90},{'óleo de soja': 7.20},{'sal refinado': 2.10},{'açúcar refinado': 4.50},{'café em pó': 14.90},{'leite integral (litro)': 5.50},{'pão de forma': 8.99},{'manteiga (200g)': 15.00},{'ovos (dúzia)': 12.00},{'queijo mussarela (fatiado)': 35.00},{'presunto (fatiado)': 28.00},{'iogurte natural (pote)': 4.20},{'farinha de trigo': 4.10},{'fermento químico': 2.80},{'leite condensado': 6.50},{'creme de leite': 3.80},{'achocolatado em pó (lata)': 19.90},{'biscoito maizena': 3.50},{'refrigerante cola (2L)': 9.50},{'água mineral (1.5L)': 3.00},{'suco de caixinha (litro)': 7.90},{'molho de tomate (extrato)': 3.20},{'maionese (pote)': 10.50},{'mostarda (frasco)': 5.90},{'ketchup (frasco)': 8.50},{'atum em lata': 6.90},{'sardinha em lata': 4.50},{'milho verde em conserva': 3.00},{'ervilha em conserva': 2.90},{'azeite de oliva (virgem)': 29.90},{'vinagre de álcool': 2.50},{'pimenta do reino (moída)': 6.00},{'frango (peito)': 22.00},{'carne bovina (acém)': 32.00},{'linguiça toscana': 18.00},{'batata (kg)': 5.50},{'cebola (kg)': 4.99},{'tomate (kg)': 7.50},{'alface (pé)': 4.00},{'banana (kg)': 6.00},{'maçã (kg)': 9.90},{'laranja (kg)': 4.00},{'detergente líquido': 3.50},{'água sanitária': 5.00},{'desinfetante': 8.90},{'sabão em pó (kg)': 15.90},{'amaciante (litro)': 11.50},{'esponja de limpeza (kit)': 5.00},{'saco de lixo (50L)': 7.50},{'papel higiênico (12 rolos)': 18.00},{'sabonete em barra (unidade)': 2.50},{'shampoo (frasco)': 15.50},{'condicionador (frasco)': 17.00},{'pasta de dente': 4.80},{'escova de dentes': 7.00},{'fio dental': 6.50},{'desodorante aerosol': 13.90},{'absorvente (pacote)': 8.90},{'creme hidratante corporal': 22.00},{'filtro de café (pacote)': 5.50},{'mel (pote)': 25.00},{'aveia em flocos': 7.50},{'farinha de mandioca': 5.00},{'gelatina (caixa)': 2.50},{'pudim (pó)': 3.50},{'chá (caixa)': 8.00},{'mortadela (kg)': 15.00},{'requeijão (pote)': 11.90},{'biscoito recheado': 3.90},{'pipoca (milho)': 4.00},{'batata palha': 6.50},{'massa de lasanha': 9.90},{'azeitona (pote)': 8.50},{'picles (pote)': 7.00},{'cerveja (lata)': 4.50},{'vinho tinto (garrafa)': 35.00},{'carvão (saco)': 12.00},{'papel toalha (rolo)': 4.00},{'papel alumínio (rolo)': 8.00},{'palha de aço': 2.00},{'limpador multiuso': 6.50},{'álcool em gel': 10.90},{'salsicha (pacote)': 12.50},{'nuggets de frango (congelado)': 18.00},{'pizza congelada': 25.00},{'sorvete (pote 2L)': 30.00},{'água com gás': 3.20},{'gengibre (kg)': 10.00},{'pimentão (kg)': 9.00},{'cenoura (kg)': 5.00},{'couve (maço)': 4.00},{'cebolinha (maço)': 3.00},{'salsa (maço)': 3.00},{'bisnaguinha': 7.50},{'tapioca (massa)': 8.90},{'barra de cereal': 3.00},{'farinha de milho (fubá)': 4.00},{'goma de tapioca': 8.90},{'margarina (500g)': 6.50}]
                  
class Cliente:

    def __init__(self, nome:str, email:str) -> None:
        self.nome = nome
        self.email = email
        self.carrinho = []
    '''
    ________
    |> EX04 <|
    Usando a classe Cliente, implemente os dunder methods de representação:

    __str__(self): Deve retornar uma string amigável para o usuário 
    (ex: "Cliente: 'Nome do Cliente' (email@exemplo.com)").

    __repr__(self): Deve retornar uma string para o desenvolvedor 
    (ex: "Cliente(email='email@exemplo.com')").
    '''
    def __str__(self) -> str:
        return f'Cliente: \'{self.nome}\' ({self.email})'

    def __repr__(self) -> str:
        return f'Cliente(nome={self.nome}, email={self.email})'
    '''
    ________
    |> EX05 <|
    Vamos fazer nossa classe Cliente se comportar como um
    contêiner para o carrinho. Implemente os seguintes dunders:

    __len__(self): Deve retornar o número de itens no self.carrinho.

    __getitem__(self, index): Deve permitir o acesso direto aos itens do carrinho 
    (ex: cliente[2] > Saída: 'banana').

    Adicione um método adicionar_ao_carrinho(self, item).
    '''
    def __len__(self) -> int:
        return len(self.carrinho)
    
    def __getitem__(self, index):
        return self.carrinho[index]
    '''
    ________
    |> EX06 <|
    Imagine que você recebeu do banco de dados uma lista de produtos, formatada como uma
    lista de dicionários:

    |> produtos_lista = [{'arroz': 6.80},{'feijão': 8.50},{'macarrão espaguete': 3.90},{'óleo de soja': 7.20},{'sal refinado': 2.10},{'açúcar refinado': 4.50},{'café em pó': 14.90},{'leite integral (litro)': 5.50},{'pão de forma': 8.99},{'manteiga (200g)': 15.00},{'ovos (dúzia)': 12.00},{'queijo mussarela (fatiado)': 35.00},{'presunto (fatiado)': 28.00},{'iogurte natural (pote)': 4.20},{'farinha de trigo': 4.10},{'fermento químico': 2.80},{'leite condensado': 6.50},{'creme de leite': 3.80},{'achocolatado em pó (lata)': 19.90},{'biscoito maizena': 3.50},{'refrigerante cola (2L)': 9.50},{'água mineral (1.5L)': 3.00},{'suco de caixinha (litro)': 7.90},{'molho de tomate (extrato)': 3.20},{'maionese (pote)': 10.50},{'mostarda (frasco)': 5.90},{'ketchup (frasco)': 8.50},{'atum em lata': 6.90},{'sardinha em lata': 4.50},{'milho verde em conserva': 3.00},{'ervilha em conserva': 2.90},{'azeite de oliva (virgem)': 29.90},{'vinagre de álcool': 2.50},{'pimenta do reino (moída)': 6.00},{'frango (peito)': 22.00},{'carne bovina (acém)': 32.00},{'linguiça toscana': 18.00},{'batata (kg)': 5.50},{'cebola (kg)': 4.99},{'tomate (kg)': 7.50},{'alface (pé)': 4.00},{'banana (kg)': 6.00},{'maçã (kg)': 9.90},{'laranja (kg)': 4.00},{'detergente líquido': 3.50},{'água sanitária': 5.00},{'desinfetante': 8.90},{'sabão em pó (kg)': 15.90},{'amaciante (litro)': 11.50},{'esponja de limpeza (kit)': 5.00},{'saco de lixo (50L)': 7.50},{'papel higiênico (12 rolos)': 18.00},{'sabonete em barra (unidade)': 2.50},{'shampoo (frasco)': 15.50},{'condicionador (frasco)': 17.00},{'pasta de dente': 4.80},{'escova de dentes': 7.00},{'fio dental': 6.50},{'desodorante aerosol': 13.90},{'absorvente (pacote)': 8.90},{'creme hidratante corporal': 22.00},{'filtro de café (pacote)': 5.50},{'mel (pote)': 25.00},{'aveia em flocos': 7.50},{'farinha de mandioca': 5.00},{'gelatina (caixa)': 2.50},{'pudim (pó)': 3.50},{'chá (caixa)': 8.00},{'mortadela (kg)': 15.00},{'requeijão (pote)': 11.90},{'biscoito recheado': 3.90},{'pipoca (milho)': 4.00},{'batata palha': 6.50},{'massa de lasanha': 9.90},{'azeitona (pote)': 8.50},{'picles (pote)': 7.00},{'cerveja (lata)': 4.50},{'vinho tinto (garrafa)': 35.00},{'carvão (saco)': 12.00},{'papel toalha (rolo)': 4.00},{'papel alumínio (rolo)': 8.00},{'palha de aço': 2.00},{'limpador multiuso': 6.50},{'álcool em gel': 10.90},{'salsicha (pacote)': 12.50},{'nuggets de frango (congelado)': 18.00},{'pizza congelada': 25.00},{'sorvete (pote 2L)': 30.00},{'água com gás': 3.20},{'gengibre (kg)': 10.00},{'pimentão (kg)': 9.00},{'cenoura (kg)': 5.00},{'couve (maço)': 4.00},{'cebolinha (maço)': 3.00},{'salsa (maço)': 3.00},{'bisnaguinha': 7.50},{'tapioca (massa)': 8.90},{'barra de cereal': 3.00},{'farinha de milho (fubá)': 4.00},{'goma de tapioca': 8.90},{'margarina (500g)': 6.50}]

    Escreva uma função buscar_produto_por_id_lista(produtos, id_busca) que itera pela lista e retorna 
    o dicionário do produto com o id correspondente. Se não encontrar, retorna None.
    '''
    def buscar_produto_por_id_lista(id_busca:int):
        global produtos_lista
        for i, item in enumerate(produtos_lista):
            if i == id_busca:
                return item



print(Cliente('Julio', 'julio@gmail.com').buscar_produto_por_id_lista(98))

'''
 ________
|> EX07 <|
O exercício anterior é muito lento para um catálogo de 1 milhão de produtos.

Escreva uma função transformar_lista_para_dict(produtos_lista) que converte a 
produtos_lista em um dicionário (hash map) onde a chave é o id do produto e o valor é o 
dicionário do produto.

Agora, escreva a função buscar_produto_por_id_dict(hashid) que busca o 
produto nesse dicionário.
'''
def transformar_lista_para_dict(produtos_lista:list) -> dict:
        return {i: item for i, item in enumerate(produtos_lista)}

def buscar_produto_por_id_dict(produtos_dict:dict, id_busca:int) -> dict:
    return produtos_dict.get(id_busca)

'''
 ________
|> EX08 <|
Usando a produtos_lista do Exercício 6, escreva uma list comprehension (compreensão de lista) 
em uma única linha que crie uma nova lista contendo apenas os nomes dos produtos que custam 
mais de R$ 40-50, 50-55, 55-70, 70+.
'''

faixas = {
    "40-50": [list(p.keys())[0] for p in produtos_lista if 40 <= list(p.values())[0] < 50],
    "50-55": [list(p.keys())[0] for p in produtos_lista if 50 <= list(p.values())[0] < 55],
    "55-70": [list(p.keys())[0] for p in produtos_lista if 55 <= list(p.values())[0] < 70],
    "70+": [list(p.keys())[0] for p in produtos_lista if list(p.values())[0] >= 70]
}

print(faixas)

