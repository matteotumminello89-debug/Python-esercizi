def trova_minore_manuale():
    numeri = []

    # Chiedo all'utente di inserire 10 numeri interi
    for i in range(10):
        numero = int(input(f"Inserisci il numero {i+1}: "))
        numeri.append(numero)

    # Stampo i numeri inseriti
    print("Numeri inseriti:", numeri)

    # Trovo il valore minimo
    minore = numeri[0]
    for n in numeri:
        if n < minore:
            minore = n

    return minore

# Esempio di utilizzo
print("Il numero minore è:", trova_minore_manuale())


print('fine')