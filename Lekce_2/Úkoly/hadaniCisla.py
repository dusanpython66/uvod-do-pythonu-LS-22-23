# Napište program, který bude řešit hru Hádej číslo.
# Hra Hádej číslo je jednoduchá hra, kdy počítač si náhodně vybere
# číslo mezi určitým rozmezím a hráč se snaží uhodnout toto číslo na základě odpovědí,
# zda zvolené číslo je menší, větší nebo rovno hledanému číslu.
# Cílem hry je uhodnout číslo co nejrychleji s co nejmenším počtem pokusů.
#
# Napišeme tedy program, který umožní hráči hrát tuto hru proti počítači.
# Program by měl být rozdělen do několika kroků:
#
# 1. Nejprve si počítač náhodně vybere číslo v určeném rozmezí, například 1 až 100.
#
# 2. Poté program požádá hráče, aby zadal svůj odhad.
#
# 3. Program porovná hráčův odhad s vybraným číslem a vypíše zprávu,
#    zda je hráčův odhad menší, větší nebo roven vybranému číslu.
#
# 4. Pokud hráč uhodne číslo, program mu gratuluje a ukončí hru.
#
# 5. Pokud hráč neuhodne číslo, program mu umožní zadat
#    další odhad a vrátí se k bodu 3.
#
# 6. Program by měl také udržovat počet pokusů a vypisovat
#     tento počet spolu s každým dalším zadáním odhadu hráčem.
#
# 7. Počet pokusů by měl být co nejmenší, takže program by měl
# hráči poskytnout informace o tom, zda jeho poslední odhad byl
# blízko hledanému číslu nebo ne.

def main():
    import random

    min_value = 1
    max_value = 100
    number = random.randint(min_value, max_value)

    print(f"Hádej číslo mezi {min_value} a {max_value}.")

    guesses = 0

    while True:
        guess = int(input("Tvůj odhad: "))
        guesses += 1

        if guess < number:
            print("Tvoje číslo je menší než hledané číslo.")
        elif guess > number:
            print("Tvoje číslo je větší než hledané číslo.")
        else:
            print(f"Gratuluji! Uhodl jsi číslo {number} s {guesses} pokusy.")
            break

        if abs(guess - number) <= 5:
            print("Jsi velmi blízko.")
        elif abs(guess - number) <= 10:
            print("Jsi blízko.")

    print("Konec hry.")

main()