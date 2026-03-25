def menu():
    print("=== CALCOLATRICE SEMPLICE ===")
    print("1 - Addizione")
    print("2 - Sottrazione")
    print("3 - Moltiplicazione")
    print("4 - Divisione")
    print("5 - Percentuale")
    print("0 - Esci")
    print("=============================")


def addizione(a, b):
    return a + b


def sottrazione(a, b):
    return a - b


def moltiplicazione(a, b):
    return a * b


def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    else:
        return a / b


def percentuale(a, b):
    # b è la percentuale di a
    return (a * b) / 100


# PROGRAMMA PRINCIPALE
scelta = -1

while scelta != 0:
    menu()
    scelta = int(input("Scegli un'operazione: "))

    if scelta == 0:
        print("Uscita dal programma.")

    elif scelta >= 1 and scelta <= 5:
        n1 = float(input("Inserisci il primo numero: "))
        n2 = float(input("Inserisci il secondo numero: "))

        if scelta == 1:
            risultato = addizione(n1, n2)
        elif scelta == 2:
            risultato = sottrazione(n1, n2)
        elif scelta == 3:
            risultato = moltiplicazione(n1, n2)
        elif scelta == 4:
            risultato = divisione(n1, n2)
        elif scelta == 5:
            risultato = percentuale(n1, n2)

        print("Risultato:", risultato)
        print()

    else:
        print("Scelta non valida\n")