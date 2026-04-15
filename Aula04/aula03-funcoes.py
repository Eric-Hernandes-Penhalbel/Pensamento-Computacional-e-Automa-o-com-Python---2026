# Função com param sem retorno
def boas_vindas(nome):
        print(f"\nOlá {nome} seja bem vindo!!\n")

nome = input("Digite seu nome: ")
boas_vindas(nome)


def soma(num_a, num_b):
    soma = int(num_a + num_b)
    return soma

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

resultado = soma(num1, num2)
print(f"\nResultado = {resultado}")

def pode_aprovar(idade):
    if idade >= 18:
        return True
    else:
        return False

idade = int(input("Digite a sua idade: "))
pode_aprovar(idade)


