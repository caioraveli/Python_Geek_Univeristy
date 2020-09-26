class Conta:
    contador = 4999
    def __init__(self, titular, saldo, limite):
        self.id = Conta.contador+1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.id

    def extrato(self):
        print(f'O titular {self.__titular} tem saldo {self.__saldo} e liimte {self.__limite}')

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente! ')
        else:
            print('Valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

c1 = Conta('Caio', 100, 1000)
c2 = Conta('Raveli', 200, 2000)

print(c1.__dict__)
print(c2.__dict__)

c1.transferir(100, c2)

print(c1.__dict__)
print(c2.__dict__)