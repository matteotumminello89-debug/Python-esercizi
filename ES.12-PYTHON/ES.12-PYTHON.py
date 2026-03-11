# Programma che analizza una frase inserita dall'utente

frase = input("Inserisci una frase: ")

# Divide la frase in parole
parole = frase.split()

# 1. Numero totale di parole
numero_totale = len(parole)

# 2. Numero di parole uniche
parole_uniche = set(parole)
numero_uniche = len(parole_uniche)

# 3. Parola più lunga
parola_piu_lunga = max(parole, key=len)

# 4. Parola più corta
parola_piu_corta = min(parole, key=len)

# 5. Parole che compaiono più di una volta
ripetute = []
for parola in parole_uniche:
    if parole.count(parola) > 1:
        ripetute.append(parola)

# --- OUTPUT ---
print("\n--- RISULTATI ---")
print(f"Numero totale di parole: {numero_totale}")
print(f"Numero di parole uniche: {numero_uniche}")
print(f"Parola più lunga: {parola_piu_lunga}")
print(f"Parola più corta: {parola_piu_corta}")

print("\nParole che compaiono più di una volta:")
if ripetute:
    for p in ripetute:
        print(f"- {p}")
else:
    print("Nessuna parola ripetuta.")

print("fine")