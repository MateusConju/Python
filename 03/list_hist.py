class ListaHistorico:

    def __init__(self, lista:list):
        self.lista = lista
        self.historico = []
    
    def __repr__(self):
        return str(self.lista)
    
    def __getitem__(self, index):
        return self.lista[index]
    
    def __setitem__(self, index, valor):
        print('Foi')
    
    def __delitem__(self, index):
        self.historico.append(self.lista[index])
        del self.lista[index]
    
    def __contains__(self, valor):
        if valor in self.lista: return True
        elif valor in self.historico: return True
        else: return False
    
    def __len__(self):
        return len(self.lista)
    

if __name__ == '__main__':
    hlist = ListaHistorico(['maçã', 'banana', 'cereja'])

    print(f'length = {len(hlist)}') # 3

    print(hlist)
    del hlist[1] # Deletar 'banana'
    print(hlist)

    print(hlist[0]) # 'maçã'

    print('maçã' in hlist) # True

    print('banana' in hlist) # True

    print('caju' in hlist) # False

    hlist[0] = 'caju' # Deletar a maçã, adicionar 'maçã' no histórico, adicionar 'caju' na lista