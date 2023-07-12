# hra "Kámen nůžky papír"

# import random
import random

# Zvolme počet vítězných kol
pocetViteznychKol = int(input("Zadej počet vítězných kol: "))

# Vytvořme proměnné pro počet výher hráče a počítače
pocetVitezstviHrace = 0
pocetVitezstviPocitace = 0

while True:
    # Zadej tah hráče

    try:
        tah = input("Zadej svůj tah, 'k' = kámen, 'n' = nůžky a 'p' = papír, 'q' = exit: ")

        if tah == "q":
            break

        if tah != "k" and tah != "n" and tah != "p":
            raise ValueError("Tah není platný")

    except ValueError as err:
        print(err)

    else:
        # Zvolme tah počítače
        tahPocitace = random.choice(["k", "n", "p"])  # náhodný výběr z listu možných tahů
        print("Tah počítače: ", tahPocitace)

        # Níže vytvořme potřebnou logiku pro určení vítěze
        if tah == tahPocitace:
            print("Plichta")
            continue   # pokračujeme v cyklu while
        elif tah == "k" and tahPocitace == "n":
            print("Vyhrál jsi")
            pocetVitezstviHrace += 1
        elif tah == "p" and tahPocitace == "k":
            print("Vyhrál jsi")
            pocetVitezstviHrace += 1
        elif tah == "n" and tahPocitace == "p":
            print("Vyhrál jsi")
            pocetVitezstviHrace += 1
        else:
            print("Vyhrál počítač")
            pocetVitezstviPocitace += 1

        # Vypišme počet výher hráče a počítače
        print("Počet výher hráče: ", pocetVitezstviHrace)
        print("Počet výher počítače: ", pocetVitezstviPocitace)

        # Zjistěme, zda někdo vyhrál
        if pocetVitezstviHrace == pocetViteznychKol:
            print("Vyhrál jsi celou hru")
            break
        elif pocetVitezstviPocitace == pocetViteznychKol:
            print("Vyhrál počítač celou hru")
            break
        else:
            continue