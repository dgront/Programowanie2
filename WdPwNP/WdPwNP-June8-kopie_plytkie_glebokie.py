
lista_duża = []
for j in range(4):
    lista_mala = []
    for i in range(4):
        lista_mala.append(i*j)
    lista_duża.append(lista_mala)

print(lista_duża)