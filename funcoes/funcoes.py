from random import random

'''
numeros = [1,2,3]

numeros.pop()

print(numeros)

def say_hi():
    return "Hello world"

ret = say_hi()
print(ret)

print(f'Retorno de {say_hi()}')


#USANDO FUNÇÃO DENTRO DE OUTRA FUNÇÃO

def quadrado(num1):
    return num1 * num1

print(f'Quadro de 7: {quadrado(7)}')


## RETORNO DA FUNÇÃO + ALGUMA COISAS

def quadrado(num):
    return num*num

def dizoi():
    return 'Oi, '

print(f'Quadrado de 7: {quadrado(7)}')

print(f'Quadrado de 7 + 1: {quadrado(7) + 1}')

nome = 'Caio'

print(dizoi()+nome+'!')


### RETORNANDO VARIOS VALORES

def multvalores():
    return 3,4,5,6

n1, n2 , n3 , n4 = multvalores()

print(n1,n2,n3,n4)

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())
'''

fish_tuple = ('blowfish','clownfish','catfish','octupus')

#new_list = [fish for fish in fish_tuple if i != 'catfish']

def gen_new_list(oldlist):
    new_list = []
    for fish in fish_tuple:
        if fish != 'octupus':
            new_list.append(fish)
    return new_list

quadlist = [num * num for num in range(10) if (num % 2 != 0)]

print(gen_new_list(fish_tuple))

print(quadlist)