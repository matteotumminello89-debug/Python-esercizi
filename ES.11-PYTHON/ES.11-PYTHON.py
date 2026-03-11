# Programma che analizza una frase inserita dall'utente

frase = input("Inserisci una frase: ")

# 1. Visualizza la frase
print("\nHai scritto:")
print(frase)

# 2. Divide la frase in parole
parole = frase.split()

print("\nLunghezza di ogni parola:")
for parola in parole:
    print(f"'{parola}' → {len(parola)} caratteri")

# 3. Stampa solo le parole che iniziano per vocale
vocali = "aeiouAEIOU"

print("\nParole che iniziano per vocale:")
for parola in parole:
    if parola[0] in vocali:
        print(parola)
print("fine")