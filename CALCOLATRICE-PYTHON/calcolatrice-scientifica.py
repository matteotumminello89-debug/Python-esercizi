import math


def menu_scientifica():
    print("=== CALCOLATRICE SCIENTIFICA ===")
    print("1 - Potenza")
    print("2 - Radice quadrata")
    print("3 - Seno")
    print("4 - Coseno")
    print("5 - Tangente")
    print("6 - Logaritmo naturale")
    print("0 - Esci")
    print("================================")


def potenza(a, b):
    return a ** b


def radice(a):
    if a < 0:
        return "Errore: radice di numero negativo"
    return math.sqrt(a)


def seno(a):
    return math.sin(a)


def coseno(a):
    return math.cos(a)


def tangente(a):
    return math.tan(a)


def logaritmo(a):
    if a <= 0:
        return "Errore: logaritmo definito solo per numeri positivi"
    return math.log(a)


# PROGRAMMA PRINCIPALE
scelta = -1

while scelta != 0:
    menu_scientifica()

    try:
        scelta = int(input("Scegli un'operazione: "))
    except ValueError:
        print("Errore: inserisci un numero valido\n")
        continue

    if scelta == 0:
        print("Uscita dalla calcolatrice scientifica.")

    elif scelta == 1:  # Potenza
        try:
            base = float(input("Inserisci la base: "))
            esp = float(input("Inserisci l'esponente: "))
            risultato = potenza(base, esp)
            print("Risultato:", round(risultato, 4), "\n")
        except ValueError:
            print("Errore: devi inserire numeri validi\n")

    elif scelta == 2:  # Radice
        try:
            num = float(input("Inserisci il numero: "))
            risultato = radice(num)
            print("Risultato:", risultato if isinstance(risultato, str) else round(risultato, 4), "\n")
        except ValueError:
            print("Errore: devi inserire un numero valido\n")

    elif scelta == 3:  # Seno
        try:
            num = float(input("Inserisci il numero (in radianti): "))
            risultato = seno(num)
            print("Risultato:", round(risultato, 4), "\n")
        except ValueError:
            print("Errore: inserisci un numero valido\n")

    elif scelta == 4:  # Coseno
        try:
            num = float(input("Inserisci il numero (in radianti): "))
            risultato = coseno(num)
            print("Risultato:", round(risultato, 4), "\n")
        except ValueError:
            print("Errore: inserisci un numero valido\n")

    elif scelta == 5:  # Tangente
        try:
            num = float(input("Inserisci il numero (in radianti): "))
            risultato = tangente(num)
            print("Risultato:", round(risultato, 4), "\n")
        except ValueError:
            print("Errore: inserisci un numero valido\n")

    elif scelta == 6:  # Logaritmo
        try:
            num = float(input("Inserisci il numero: "))
            risultato = logaritmo(num)
            print("Risultato:", risultato if isinstance(risultato, str) else round(risultato, 4), "\n")
        except ValueError:
            print("Errore: inserisci un numero valido\n")

    else:
        print("Scelta non valida\n")