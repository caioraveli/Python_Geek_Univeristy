class Calculadora:
    op = 0
    def __init__(self):
        pass

    def soma(self):
        self.op = Calculadora.op + 1
        num1 = float(input(f'Informe o primeiro numero: '))
        num2 = float(input(f'Informe o segundo numero: '))
        print(f'Soma: {num1}+{num2} = {num1+num2}')
        Calculadora.op = self.op
        print(f'Op = {self.op}')

    def subt(self):
        self.op = Calculadora.op + 1
        num1 = float(input(f'Informe o primeiro numero: '))
        num2 = float(input(f'Informe o segundo numero: '))
        print(f'Soma: {num1}-{num2} = {num1 - num2}')
        Calculadora.op = self.op
        print(f'Op = {self.op}')

    def mutipl(self):
        self.op = Calculadora.op + 1
        num1 = float(input(f'Informe o primeiro numero: '))
        num2 = float(input(f'Informe o segundo numero: '))
        print(f'Soma: {num1}x{num2} = {num1 * num2}')
        Calculadora.op = self.op
        print(f'Op = {self.op}')

    def divis(self):
        self.op = Calculadora.op + 1
        num1 = float(input(f'Informe o primeiro numero: '))
        num2 = float(input(f'Informe o segundo numero: '))
        print(f'Soma: {num1}/{num2} = {num1/num2}')
        Calculadora.op = self.op
        print(f'Op = {self.op}')

    def fibo(self):
        self.op = Calculadora.op + 1
        sz = int(input(f'Informe o tamanho da sequencia: '))
        st = 0
        st1 = 1
        print(f'{st} {st1}',end=" ")
        for i in range(1,sz):
            tmp = st + st1
            st = st1
            st1 = tmp
            print(f'{tmp}',end=" ")
        Calculadora.op = self.op
        print(f'Op = {self.op}')

n1 = Calculadora()
opt = int(input("1 - Soma"
      "\n2 - Subt"
      "\n3 - Mult"
      "\n4 - Div"
      "\n5 - Fibo"
      "\n0 - Sair"))

while opt != 0:
    if opt == 1:
        n1.soma()
    if opt == 2:
        n1.subt()
    if opt == 3:
        n1.mutipl()
    if opt == 4:
        n1.divis()
    if opt == 5:
        n1.fibo()
    if opt == 0:
        break

    opt = int(input("\n\n1 - Soma"
                    "\n2 - Subt"
                    "\n3 - Mult"
                    "\n4 - Div"
                    "\n0 - Sair"))