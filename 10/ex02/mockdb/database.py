class MockDB: 
    def __init__(self):
        self.connected = False
        
    def connect(self):
        self.connect = True
        print(">>> DB | Open")

    def close(self):
        return('>>> DB | Closed')

    # def query(self):
    #     if not (self):

# Exercício A: O Timer de Requisição

# Tarefa: Criar uma dependência measure_time com yield.

# Setup: Gravar o tempo inicial (time.time()).

# Yield: Não precisa retornar nada (yield).

# Teardown: Calcular tempo_final - tempo_inicial e imprimir no console: "Tempo de execução: X segundos".

# Objetivo: Criar um "mini-profiler" que loga quanto tempo a rota levou.

# Exercício B: O Arquivo Temporário

# Tarefa: Criar uma dependência que cria um arquivo temporário (tempfile), escreve "Olá" nele, faz yield do caminho do arquivo, e no finally deleta o arquivo.

# Rota: A rota lê o arquivo e retorna o conteúdo.

# Verificação: Verificar se o arquivo realmente sumiu do disco após a requisição.