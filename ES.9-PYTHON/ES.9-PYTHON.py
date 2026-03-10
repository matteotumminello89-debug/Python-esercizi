import random

def trova_minore():
    # Genero una lista di 10 numeri interi casuali tra 1 e 100
    numeri = []
    for _ in range(10):
        numero = random.randint(1, 100)
        numeri.append(numero)

    # Stampo i numeri generati
    print("Numeri generati:", numeri)

    # Trovo il valore minimo
    minore = numeri[0]  # parto dal primo elemento
    for n in numeri:
        if n < minore:
            minore = n

    # Restituisco il minore
    return minore

# Esempio di utilizzo
print("Il numero minore è:", trova_minore())

print("fine")