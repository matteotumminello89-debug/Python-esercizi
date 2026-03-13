import random

class Analizzatore:

    def area_rettangolo(self, base, altezza):
        return base * altezza

    def trova_il_minimo(self, lista_numeri):
        return min(lista_numeri)

    def pari_o_dispari(self, numero):
        if numero % 2 == 0:
            print(f"Il numero {numero} è pari.")
        else:
            print(f"Il numero {numero} è dispari.")

    def trova_minore(self):
        # Genero una lista di 10 numeri interi casuali tra 1 e 100
        numeri = []
        for _ in range(10):
            numero = random.randint(1, 100)
            numeri.append(numero)

        # Trovo il minore manualmente
        minore = numeri[0]
        for n in numeri:
            if n < minore:
                minore = n

        print("Numeri generati:", numeri)
        print("Il numero minore è:", minore)
        return minore
    def somma_fino_a(self, N):
        somma = 0
        for i in range(N + 1):
            somma += i
        return somma




# -------------------------
# TEST DELLA CLASSE
# -------------------------

analizzatore = Analizzatore()

# Test area rettangolo
print("Area rettangolo:", analizzatore.area_rettangolo(5, 3))

# Test trova il minimo
print("Minimo:", analizzatore.trova_il_minimo([5, 2, 9, 1]))

# Test pari o dispari
analizzatore.pari_o_dispari(7)
analizzatore.pari_o_dispari(10)

# Test trova_minore
analizzatore.trova_minore()

# Test somma_fino_a
numero = int(input("Inserisci un numero intero positivo: "))

if numero > 0:
    risultato = analizzatore.somma_fino_a(numero)
    print(f"La somma dei numeri da 1 a {numero} è: {risultato}")
else:
    print("Il numero deve essere positivo")

