def somma_dispari(N):
    somma = 0
    for i in range(0, N + 1):
        if i % 2 != 0:   # numero dispari
            somma += i
    print("La somma dei numeri dispari da 0 a", N, "è:", somma)


# --- Inserimento da console ---
N = int(input("Inserisci un numero N: "))

# --- Chiamata della funzione ---
somma_dispari(N)