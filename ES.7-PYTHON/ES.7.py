def somma_fino_a_N(N):
    somma = 0
    for i in range(0, N + 1):
        somma += i
    print("La somma dei numeri da 0 a", N, "è:", somma)


# --- Inserimento da console ---
N = int(input("Inserisci un numero N: "))

# --- Chiamata della funzione ---
somma_fino_a_N(N)