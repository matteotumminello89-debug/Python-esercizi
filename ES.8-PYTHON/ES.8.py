def somma_fino_a(N):
    somma = 0
    for i in range(N + 1):
        if isDispari(i):
            somma += i
    return somma

def isDispari(N):
    tmp = N % 2
    if tmp == 0:
        return False
    else:
        return True

numero=int(input("Inserisci un numero intero positivo: "))

if numero > 0:
    ris = somma_fino_a(numero)
    print(f"La somma dei numeri dispari da 1 a {numero}: {ris}")
else:
    print("Il numero deve essere positivo")
