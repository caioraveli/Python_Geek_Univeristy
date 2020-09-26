from passlib.hash import pbkdf2_sha256 as crypt

class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuarios! ')

    def __init__(self,nome,sobrenome,email,senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.senha = crypt.hash(senha,rounds=200000,salt_size=16)
        Usuario.contador = self.id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha2):
        if crypt.verify(senha2,self.senha):
            return True
        return False


nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme sua senha: ")

if senha == confirma_senha:
    user = Usuario(nome,sobrenome,email,senha)
else:
    print("Senha não confere...")

print("Usuario criado com sucesso!!!")


senha = input("Informe senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado!!!")

print(f'Senha criptografada: {user.senha}')

Usuario.conta_usuarios()