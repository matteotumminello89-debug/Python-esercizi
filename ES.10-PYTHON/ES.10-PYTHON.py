def trova_il_minimo(lista_numeri):
    return min(lista_numeri)

n = int(input("Quanti numeri vuoi inserire? "))

if n > 0:
    numeri = []
    for i in range(n):
        numero = int(input(f"Inserisci il numero {i+1}: "))
        numeri.append(numero)

    valore_minimo = trova_il_minimo(numeri)
    print(f"Il numero minimo è: {valore_minimo}")
else:
    print("Il numero deve essere maggiore di zero.")