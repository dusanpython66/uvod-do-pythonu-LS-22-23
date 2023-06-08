# funkce a moduly

# prvni funkce: prázdná funkce (bez parametrů)

# def pozdrav():
#     jmeno = "karel"
#     prijmeni = "novák"
#     print(f"Pan {jmeno} {prijmeni}")

# def pozdrav(jmeno, prijmeni):
#     print(f"Pan/Paní {jmeno} {prijmeni}")

# pozdrav(prijmeni="Kolář", jmeno = "Petr")

print("Karel Novák", "Petr Kolář", sep="    ")

# defaultní hodnoty parametrů
def pozdrav(jmeno="Karel", prijmeni="Novák"):
    print(f"Pan/Paní {jmeno} {prijmeni}")

pozdrav()




# funkce s parametry

def prepona(a, b):
    c = (a**2 + b**2)**(1/2)
    print("c = ", c)

prepona(3, 4)

# funkce vracející hodnotu:

def prepona(a, b):
    c = (a**2 + b**2)**(1/2)
    return c  # vrací hodnotu proměnné c

delkaPrepony = prepona(3, 4) # uložíme si hodnotu proměnné c do proměnné delkaPrepony

# print(prepona(3, 4) * 2)
print(delkaPrepony)

# externí moduly

import sympy as sym
sym.sin(sym.pi)

x = sym.symbols("x")
f = sym.sin((2*x) / (x**2 + 1))
print(sym.diff(f, x))

#######  externí moduly vytvořené uživatelem

from newModul import prepona  # import uživatelského modulu umístěného v kořenovém adresáři projektu
c = prepona(3,5)
print(c)

# import  uživatelského modulu umístěného v podadresáři projektu ./Lekce_2
import sys
sys.path.append('./Lekce_2')
from mujModul import delkaPrepony

# volání funkce z uživatelského modulu:
c = delkaPrepony(3,20)
print(c)

print(1 / 0)

# handling exceptions  (zachytávání výjimek)
def prepona(a, b):
    try: # pokusí se provést následující kód
        c = (a**2 + b**2)**(1/2)
    except TypeError: # pokud dojde k vyvolání výjimky TypeError
        print("Funkce přijímá pouze čísla")
    else:  # pokud nedošlo k vyvolání výjimky
        return c
prepona(4, 3)
# sami si vytvoříme výjimku ...


# Collatzova posloupnost  (https://en.wikipedia.org/wiki/Collatz_conjecture)
# 1. Pokud je číslo sudé, vydělíme jej dvěma
# 2. Pokud je číslo liché, vynásobíme jej třemi a přičteme jedna
# 3. Opakujeme dokud nedostaneme číslo 1

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

n = int(input("Zadej číslo: "))
while n != 1:
    n = collatz(n)
    print(n)








