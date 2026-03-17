def calcola_codice_fiscale(cognome, nome, anno, mese, giorno, sesso, comune):
    # Parte cognome
    cognome = cognome.upper()
    consonanti_c = ""
    vocali_c = ""

    for lettera in cognome:
        if lettera in "AEIOU":
            vocali_c += lettera
        elif lettera.isalpha():
            consonanti_c += lettera

    parte1 = (consonanti_c + vocali_c)[:3]
    while len(parte1) < 3:
        parte1 += "X"

    # Parte nome
    nome = nome.upper()
    consonanti_n = ""
    vocali_n = ""

    for lettera in nome:
        if lettera in "AEIOU":
            vocali_n += lettera
        elif lettera.isalpha():
            consonanti_n += lettera

    if len(consonanti_n) >= 4:
        parte2 = consonanti_n[0] + consonanti_n[2] + consonanti_n[3]
    else:
        parte2 = (consonanti_n + vocali_n)[:3]

    while len(parte2) < 3:
        parte2 += "X"

    # Parte data
    mesi = {
        1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "H",
        7: "L", 8: "M", 9: "P", 10: "R", 11: "S", 12: "T"
    }

    anno2 = str(anno)[-2:]
    mese_lettera = mesi[mese]

    if sesso.upper() == "F":
        giorno = giorno + 40

    giorno2 = str(giorno).zfill(2)

    parte3 = anno2 + mese_lettera + giorno2

    # Parte comune
    parte4 = comune.upper()

    # Unione delle prime 15 lettere
    cf15 = parte1 + parte2 + parte3 + parte4

    # Carattere di controllo
    valori_dispari = {
        "0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21,
        "A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21,
        "K": 2, "L": 4, "M": 18, "N": 20, "O": 11, "P": 3, "Q": 6, "R": 8, "S": 12, "T": 14,
        "U": 16, "V": 10, "W": 22, "X": 25, "Y": 24, "Z": 23
    }

    valori_pari = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
        "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
        "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
    }

    somma = 0
    for i in range(15):
        carattere = cf15[i]
        if (i + 1) % 2 == 0:
            somma += valori_pari[carattere]
        else:
            somma += valori_dispari[carattere]

    resto = somma % 26
    controllo = chr(resto + 65)

    return cf15 + controllo


# PROGRAMMA PRINCIPALE (stile scolastico)
cognome = input("Inserisci il cognome: ")
nome = input("Inserisci il nome: ")
anno = int(input("Anno di nascita (AAAA): "))
mese = int(input("Mese di nascita (1-12): "))
giorno = int(input("Giorno di nascita: "))
sesso = input("Sesso (M/F): ")
comune = input("Codice catastale del comune: ")

codice_fiscale = calcola_codice_fiscale(cognome, nome, anno, mese, giorno, sesso, comune)
print("Il codice fiscale è:", codice_fiscale)