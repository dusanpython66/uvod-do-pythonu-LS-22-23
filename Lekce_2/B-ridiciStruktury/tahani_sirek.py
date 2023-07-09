"""
Napišme program, který bude představovat hru kde budou hrát proti sobě buď dva hráči nebo hráč proti počítači.
Hráči budou střídat tahy. Hráč, který na tahu je, si vybere počet zápalek, které chce vzít.
Může si vybrat 1, 2 nebo 3 zápalky. Hráč, který vezme poslední zápalku, prohrává.
"""

# zvolme počet zápalek na začátku hry
pocetZapalek = int(input("Zadejte počet zápalek na začátku hry: "))

# z modulu random importujeme funkci randint
from random import randint

# rozhodneme, jestli hrají dva hráči nebo jeden hráč proti počítači

print("Zvolte si režim hry:")
print("1 - hrají dva hráči")
print("2 - hraje hráč proti počítači")
volba = int(input("Zadejte číslo režimu: "))

if volba == 1:  # hrají dva hráči
    # zadejme jména hráčů:
    jmeno1 = input("Zadejte jméno prvního hráče: ")
    jmeno2 = input("Zadejte jméno druhého hráče: ")

    # náhodně určíme, kdo začíná
    hrac = randint(1, 2)  # náhodné číslo 1 nebo 2
    # vypíšeme jméno hráče, který začíná
    if hrac == 1:
        jmenoHrace = jmeno1
        print(f"Začíná {jmeno1}")
    else:
        jmenoHrace = jmeno2
        print(f"Začíná {jmenoHrace}")

    # dokud nejsou všechny zápalky sebrané, hraje se dál
    while pocetZapalek > 0:
        try:
            # hráč, který je na tahu, si vybere počet zápalek
            tah = int(input(f"Zadejte počet zápalek, které chcete vzít (1-3): "))
            # pokud hráč zadá špatný tah, vyvolá se výjimka
            if tah < 1 or tah > 3:
                raise ValueError  # vyvoláme výjimku ValueError (hodnota je chybná)
        except ValueError:
            print("Chyba: Zadán neplatný vstup. Zadej prosím číslo 1, 2 nebo 3.")
        else:
            # odečteme počet zápalek, které hráč vzal
            pocetZapalek -= tah
            # vypíšeme, kolik zápalek zbývá
            print(f"Zbývá {pocetZapalek} zápalek")

            # pokud jsou všechny zápalky sebrané, vyhrál hráč, který je na tahu
            if pocetZapalek == 0:
                # zjistíme jméno vítěze hry
                if jmenoHrace == jmeno1:
                    jmenoViteze = jmeno2
                else:
                    jmenoViteze = jmeno1
                print(f"Vyhrál hráč {jmenoViteze}")
            else:
                # pokud nejsou všechny zápalky sebrané, předáme tah druhému hráči
                if jmenoHrace == jmeno1:
                    jmenoHrace = jmeno2
                else:
                    jmenoHrace = jmeno1
                print(f"Hraje hráč {jmenoHrace}")

elif volba == 2:  # hraje hráč proti počítači
    # zadejme jméno hráče:
    jmenoHrace = input("Zadejte jméno hráče: ")

    # náhodně určíme, kdo začíná
    hrac = randint(1, 2)  # náhodné číslo 1 nebo 2
    # vypíšeme jméno hráče, který začíná
    if hrac == 1:
        kdoJeNaTahu = "hráč"
        print(f"Začíná {jmenoHrace}")
    else:
        kdoJeNaTahu = "počítač"
        print(f"Začíná počítač")

    # dokud nejsou všechny zápalky sebrané, hraje se dál
    while pocetZapalek > 0:
        try:
            # hráč, který je na tahu, si vybere počet zápalek
            if kdoJeNaTahu == "hráč":
                tah = int(input(f"Zadejte počet zápalek, které chcete vzít (1-3): "))
                # pokud hráč zadá špatný tah, vyvolá se výjimka
                if tah < 1 or tah > 3:
                    raise ValueError  # vyvoláme výjimku ValueError (hodnota je chybná)
            else:  # počítač
                # počítač si vybere náhodný počet zápalek
                # počítač si vybere náhodné číslo 1, 2 nebo 3 a zároveň
                # toto číslo nemůže být větší než počet zbývajících zápalek
                # zvolí se náhodné číslo 1, 2 nebo 3 (ale ne víc než zbývá zápalek)
                tah = randint(1, min(3, pocetZapalek))
                print(f"Počítač vzal {tah} zápalek")
        except ValueError:
            print("Chyba: Zadán neplatný vstup. Zadej prosím číslo 1, 2 nebo 3.")
        else:  # všechno je v pořádku - hráč zadal správný tah nebo počítač vybral náhodný tah

            # odečteme počet zápalek, které hráč vzal
            pocetZapalek -= tah
            # vypíšeme, kolik zápalek zbývá
            print(f"Zbývá {pocetZapalek} zápalek")

            # pokud jsou všechny zápalky sebrané, vyhrál hráč, který je na tahu
            if pocetZapalek == 0:
                # zjistíme jméno vítěze hry
                if kdoJeNaTahu == "hráč":
                    jmenoViteze = "počítač"
                else:
                    jmenoViteze = jmenoHrace
                print(f"Vyhrál hráč {jmenoViteze}")
            else:
                # pokud nejsou všechny zápalky sebrané, předáme tah druhému hráči
                if kdoJeNaTahu == "hráč":
                    kdoJeNaTahu = "počítač"
                else:
                    kdoJeNaTahu = "hráč"
                print(f"Hraje {kdoJeNaTahu}")
