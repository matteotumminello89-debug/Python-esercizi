def pari_o_dispari(numero):
    if numero % 2 == 0:
        print(f"Il numero {numero} è pari.")
    else:
        print(f"Il numero {numero} è dispari.")


# --- Inserimento da console ---
n = int(input("Inserisci un numero: "))

# --- Chiamata della funzione ---
pari_o_dispari(n)