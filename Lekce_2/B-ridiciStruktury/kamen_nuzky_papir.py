# hra "Kámen nůžky papír"

# import random
import random

# Zvolme počet vítězných kol
pocetViteznychKol = int(input("Zadej počet vítězných kol: "))

# Vytvořme seznam možných tahů
# tahy = ["kámen", "nůžky", "papír"]

while True:
    # Zadej tah

    try:
        tah = input("Zadej svůj tah, 'k' = kámen, 'n' = nůžky a 'p' = papír: ")

        if tah != "k" and tah != "n" and tah != "p":
            raise ValueError("Tah není platný")
    except ValueError as err:
        print(err)

    else:
        pass  # pokračujeme dále v kódu
        break