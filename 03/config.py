class Config:

    def __init__(self, **kwargs):
        self.dict = kwargs
    
    def __str__(self):
        return f'Configurações: host={self.dict.get('host')}, port={self.dict.get('port')}, timeout={self.dict.get('timeout')}, service={self.dict.get('service')}'

    def __repr__(self):
        return f'Config(settings={self.dict})'
    
    def __call__(self, key=None):
        if key == None:
            print(f'host : {self.dict.get('host', 'Não Configurado')}')
            print(f'porta : {self.dict.get('port', 'Não Configurado')}')
            print(f'timeout : {self.dict.get('timeout', 'Não Configurado')}')
            print(f'serviço : {self.dict.get('service', 'Não Configurado')}')
        else:
            print(key + ' = ', end='')
            print(self.dict.get(key, 'Não Configurado!'))

if __name__ == '__main__':
    config = Config(host='localhost', port=8080, timeout=30)
    
    print(repr(config))
    print(config)
    config()
    config('host')
    config('michaeljackson')
