# Exercício 1:
raio = int(input("Digite o raio do circulo: "))
pi = 3.14159
area = pi*raio**2
print(f"A área de um círculo com um valor de raio igual a {raio} possui área de: {area}")


#Exercício 2:
Farenheit = float(input("\n\nDigite a temperatura em Fireheint"))
Celsius = (Farenheit-32)*5/9
print(f"O valor de {Farenheit} em celsius fica {Celsius}")

#Exercício 3:
livros = 3*25
canetas = 2*5
total = livros + canetas
print(f"\n\nO total gasto na compra foi: R${total}")

#Exercício 4:
velocidade = 60
distancia = 150
tempo = distancia / velocidade
print(f"\n\nO tempo em horas demorado para cruzar o caminho foi: {tempo}")

#Exercício 5:
not1 = float(input("\n\nInforme a primeira nota do aluno para o cálculo da média: "))
not2 = float(input("Informe a segunda nota do aluno para o cálculo da média: "))
media = (not1 + not2) /2
print(f"A nota média de um aluno que possui as notas {not1} e {not2} é de {media}")

#Exercício 6:
not1 = float(input("\n\nInforme a primeira nota do aluno para o cálculo da média: "))
not2 = float(input("Informe a segunda nota do aluno para o cálculo da média: "))
media = ((not1*4) + (not2*6)) / 10
print(f"A média com peso de um aluno com notas {not1} e {not2} é: {media}")


#Exercício 7:
nome_valor1 = input("\n\nQual o nome da peça/objeto a ser mencionado no gasto? ")
numero_valor1 = int(input(f"Qual a quantidade de uma unidade do {nome_valor1}? "))
preco_valor1 = float(input(f"Qual o preço de um {nome_valor1}? "))
nome_valor2 = input("\n\nQual o nome da peça/objeto a ser mencionado em segundo no gasto? ")
numero_valor2 = int(input(f"Qual a quantidade de uma unidade do {nome_valor2}? "))
preco_valor2 = float(input(f"Qual o preço de um {nome_valor2}? "))

total1 = numero_valor1*preco_valor1
total2 = numero_valor2*preco_valor2
total = total1+total2

print(f"Confere! Então o total da compra de {nome_valor1} dentro do mercado ficou {total1}\n O total da compra do {nome_valor2} foi {total2}\n E o total de todas as compras foi {total}")

#Exercício 8:
valor_produto = float(input("\n\nQual o valor do produto comprado? "))
valor_pago = float(input("Qual foi o valor pago nessa compra? "))
troco = valor_pago - valor_produto
print(f"O valor do troco é: {troco}")
