codice = input("Inserisci il codice fiscale: ")

if len(codice) == 16:
    print("Codice fiscale valido (lunghezza corretta).")
else:
    print("Codice fiscale NON valido: deve contenere esattamente 16 caratteri.")
print