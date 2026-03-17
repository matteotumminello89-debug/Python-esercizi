codice = input("Inserisci il codice fiscale: ").strip().upper()

# Controllo lunghezza
if len(codice) != 16:
    print("Errore: il codice fiscale deve contenere esattamente 16 caratteri.")
else:
    valido = True

    # Controllo lettere nelle posizioni 0-5 (cognome + nome)
    if not codice[0:6].isalpha():
        valido = False

    # Controllo numeri nelle posizioni 6-7 (anno)
    if not codice[6:8].isdigit():
        valido = False

    # Controllo lettera del mese (posizione 8)
    if not codice[8].isalpha():
        valido = False

    # Controllo numeri nelle posizioni 9-10 (giorno/sesso)
    if not codice[9:11].isdigit():
        valido = False

    # Controllo lettere nelle posizioni 11-15 (comune + carattere finale)
    if not codice[11:16].isalpha():
        valido = False

    # Risultato finale
    if valido:
        print("Codice fiscale formalmente valido.")
    else:
        print("Codice fiscale NON valido: errore nella struttura o nei tipi di caratteri.")