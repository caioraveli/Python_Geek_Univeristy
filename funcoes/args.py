"""
*Args é uma espécie de parâmetro variável. Ao invés de eu ir criando vários parâmetros, posso utilizar apenas o args
e ele se encarrega de ir montando esses parâmetros dentro de uma tupla

Obs: args é só um nome convencional. O que é importante é o *  --> Eu poderia usar qualquer nome no lugar de args,
contanto que tivesse com o * antes, teria o mesmo efeito. Ex: *teste, *outros,*qualquercoisa, etc

"""

'''
def soma_numeros(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(5,6))
print(soma_numeros(3,3,5,6,9))

#Melhor forma de fazer utilizando função sum

def soma_numeros(*args):
    return sum(args)

print("\n\nFUNÇÃO 2")
print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(5,6))
print(soma_numeros(3,3,5,6,9))


print("\n\nFUNÇÃO 3")

def cadastro(nome,email,*args):
    print(nome)
    print(email)
    print(args)

cadastro('caio','email@mail.com',10,20,30)

def verifica_info(*args):
    if 'Caio' in args and 'University' in args:
        return 'Bem vindo Caio'
    return 'Eu não tenho certeza quem é você'

print(verifica_info())
print(verifica_info('Caio'))
print(verifica_info(True))
print(verifica_info(1,True,3,456,'Teste','University',3.55,'Caio'))

'''
#DESEMPACOTADOR

numeros = [3, 4, 5, 6]

num1, num2, num3, num4 = numeros

print(num1)
print(num2)

#Se passar a lista numeros pro args, ele vai entender como um só elemento.

#Pra ele entender posição por posição ao inves de um elemento só, posso utilizar *numeros

#ISTO SERVE PARA QUALQUER COLEÇÂO DE ELEMENTOS

def soma(*args):
    return sum(args)

print(soma(*numeros))

#Fazendo a mesma coisa com tupla

numerostupla = (3, 4, 5, 6)
print(soma(*numerostupla))