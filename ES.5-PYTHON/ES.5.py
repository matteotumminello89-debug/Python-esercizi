def area_rettangolo(base, altezza):
    return base * altezza

def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

print("Cosa vuoi calcolare?")
print("1. Area del rettangolo")
print("2. Perimetro del rettangolo")
scelta = input("Inserisci 1 o 2: ")

if scelta == "1" or scelta == "2":

    b = float(input("Inserisci la base del rettangolo: "))
    a = float(input("Inserisci l'altezza del rettangolo: "))

    if scelta == "1":
        area = area_rettangolo(b, a)
        print(f"L'area del rettangolo è: ", area)
    else:
        perimetro = perimetro_rettangolo(b, a)
        print(f"Il perimetro del rettangolo è: ", perimetro)
else:
    print("Scelta non valida. Scegli 1 o 2.")
