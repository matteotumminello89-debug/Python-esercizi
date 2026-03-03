def somma_fino_a(N):
    somma = 0
    for i in range(N + 1):
        somma += i
    return somma

numero = int(input("Inserisci un numero intero positivo: "))

if numero > 0:
    ris = somma_fino_a(numero)
    print(f"La somma dei numeri da 1 a {numero}: {ris}")
else:
    print("Il numero deve essere positivo")
