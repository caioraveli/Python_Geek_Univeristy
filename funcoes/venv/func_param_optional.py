'''

Neste caso, já temos um valor default para o parametro potência. Caso eu nao passe quando chamar a função,
valor de potencia sempre será 2

'''

def exponencial(num, potencia=2):
    return num ** potencia

print(exponencial(3,4))
print(exponencial(3))

def expenencial2(numero=2,pot=2):
    return numero ** pot

print(expenencial2())

'''

OBS: Parâmetro default deve sempre ser declarado nos últimos parametros

'''

def exponencial3(potencia, num=2):
    return num ** potencia

#print(exponencial3()) DA ERRO
print(exponencial3(3))
print(exponencial3(2,4))

'''

PASSAR FUNÇÃO COMO PARAMETRO.

'''

def soma(num1,num2):
    return num1+num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def subt(num1,num2):
    return num1-num2

print(mat(3,4,)) #nesse caso, mat usa soma como default
print(mat(3,4,subt)) #repare que não usamos () pra passar a funcao.

'''

Se tivermos uma variavel global e uma local de mesmo nome, a variável local (definida dentro da função) terá prioridade. 
Caso eu queira utilizar a variável global dentro de uma função, tenho que usar o operador "global"

'''

total = 0

def incrementa():
    global total
    total = total + 1
    return total

print(incrementa())

'''

Se eu quiser usar uma variável de uma função anterior (dentro do mesmo escopo),
tenho que utilizar o operador "nonlocal"

'''


def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
print(fora())
