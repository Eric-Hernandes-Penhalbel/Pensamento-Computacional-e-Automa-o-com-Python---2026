nomes = ["Ana", "Bia", "Alex", "Caio", "Alan"]

for i in range(len(nomes)):
    for x in range(len(nomes)):
        if i == x:
            continue
        print(f"Dupla: {nomes[i]} e {nomes[x]}")

