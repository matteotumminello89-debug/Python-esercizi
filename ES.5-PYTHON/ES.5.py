def rettangolo(scelta, base, altezza):
    if scelta == "area":
        risultato = base * altezza
        print("L'area del rettangolo è:", risultato)
    elif scelta == "perimetro":
        risultato = 2 * (base + altezza)
        print("Il perimetro del rettangolo è:", risultato)
    else:
        print("Scelta non valida. Devi scrivere 'area' oppure 'perimetro'.")


# --- Prima decido cosa voglio calcolare ---
scelta = input("Cosa vuoi calcolare (area o perimetro)? ")

if scelta != "area" and scelta != "perimetro":
    print("Errore: scelta non valida.")
else:
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))
    rettangolo(scelta, base, altezza)