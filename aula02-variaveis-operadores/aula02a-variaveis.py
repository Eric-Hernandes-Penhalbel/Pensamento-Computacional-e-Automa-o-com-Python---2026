print("Olá mundo")
print(7+4)
print("7 + 4")
print("7" + "4")# Concatenando os textos (Strings)

#Comentário de uma linha
'''
Comentário de multiplas linhas
1
2
3
4
'''

#Variáveis
nome = "Alexandre" #String
print("nome") #Digita nome
print(nome) #Exibe variável nome

idade = 26 #int
peso = 70.2 #float

print(nome, idade, peso)
print("Olá", nome, idade, peso)
print(f"Olá {nome}!")


#Input - Simulação de um forms no CMD
nome = input("Digite seu nome: ") # recebendo o valor como texto (String)
print(nome)

idade = int(input("Digite sua idade: ")) # recebendo o valor como INT
print(idade)

peso = float(input("Digite seu peso: ")) # recebendo o valor como Float
print(peso)

print(nome, idade, peso)


ano_nascimento = 1999
ano_atual = 2026
idade = ano_atual - ano_nascimento #operação matemática
print(idade)