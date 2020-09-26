class Cliente:
    id = 0
    def __init__(self,nome,end,tel):
        self.id = self.id + 1
        self.nome = nome
        self.end = end
        self.tel = tel
        Cliente.id = self.id
    '''
    def printa_dados(self):
        print(self.nome)
        print(self.end)
        print(self.tel)
        print(self.id)
        '''
    def printa_dados(self):
        print(self.nome)
        print(self.end)
        print(self.tel)
        print(self.id)

c1 = Cliente('Caio Raveli','Rua I, 121','888888888')
Cliente.printa_dados(c1)
c2 = Cliente('Freitas Barbosa','Pedro de Alencar','999999999')
Cliente.printa_dados(c2)

