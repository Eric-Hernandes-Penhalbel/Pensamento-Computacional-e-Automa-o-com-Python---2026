 #Lógica E (and)

email = True
senha = False

verifica_login = email and senha == True
print(verifica_login)


#Lóogica OU (or)

logica_ou = False or True or False
print(logica_ou)

#Lógica NOT
negacao = not True
print(negacao)

if not verifica_login:
    print("acerta ai...")