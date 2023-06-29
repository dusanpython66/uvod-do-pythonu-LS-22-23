# funkce a moduly

# prvni funkce: prázdná funkce (bez parametrů)

def pozdrav():
    jmeno = "karel"
    prijmeni = "novák"
    print(f"Pan {jmeno} {prijmeni}")  # f-string (formátovaný řetězec)

# Nyní zavoláme funkci pozdrav()
pozdrav()

def pozdrav(jmeno, prijmeni):
    print(f"Pan/Paní {jmeno} {prijmeni}")

pozdrav(prijmeni="Kolář", jmeno = "Petr")

print("Karel Novák", "Petr Kolář", sep="     ")  # sep je parametr funkce print (oddělovač) - defaultně je mezera

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
print("Délka přepony je rovna: ", delkaPrepony)
# Totéž pomocí f-stringu:
print(f"Délka přepony je rovna: {delkaPrepony}")

# externí moduly
# Vyzkoušejme si importovat modul Sympy, který obsahuje funkce pro symbolické výpočty.
# V rámci následujícího příkladu si vyzkoušíme spočítat derivaci funkce sin(x) pomocí funkce diff().
# Více o modulu Sympy se můžete dočíst v dokumentaci. https://docs.sympy.org/latest/index.html

import sympy as sym
sym.sin(sym.pi)

x = sym.symbols("x")
f = sym.sin((2*x) / (x**2 + 1))
print(sym.diff(f, x))

#######  externí moduly vytvořené uživatelem

# import  uživatelského modulu umístěného v podadresáři projektu ./Lekce_2
import sys

sys.path.append('./Lekce_2/D-funkceModuly')
from mujModul import delkaPrepony  # import uživatelského modulu

# volání funkce z uživatelského modulu:
c = delkaPrepony(3,20)
print(c)

print(1 / 0)

# handling exceptions  (zachytávání výjimek)
# Syntaxe:
# try:
#     <kód>
# except <výjimka>:
#     <kód>
# else:
#     <kód>
# finally:   # nepovinný blok  (vykoná se vždy)
#     <kód>


def prepona(a, b):
    try: # pokusí se provést následující kód
        c = (a**2 + b**2)**(1/2)
    except TypeError: # pokud dojde k vyvolání výjimky TypeError
        print("Funkce přijímá pouze čísla")
    else:  # pokud nedošlo k vyvolání výjimky
        return c
prepona(4, 3)


# Collatzova posloupnost  (https://en.wikipedia.org/wiki/Collatz_conjecture)
# 1. Pokud je číslo sudé, vydělíme jej dvěma
# 2. Pokud je číslo liché, vynásobíme jej třemi a přičteme jedna
# 3. Opakujeme dokud nedostaneme číslo 1
# Více o Collatzově posloupnosti se můžete dočíst na Wikipedii. https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

n = int(input("Zadej číslo: "))
while n != 1:
    n = collatz(n)  # přiřazení výsledku funkce collatz() do proměnné n
    print(n)

# Předávání libovolného počtu parametrů do funkce
# Syntaxe:
# def <název_funkce>(<parametry>, *args, **kwargs):
#     <kód>

# *args - předává libovolný počet parametrů do funkce ve formě n-tice
# **kwargs - předává libovolný počet pojmenovaných parametrů do funkce ve formě slovníku

def udelej_pizzu(*ingredience):
    print("Ingredience: ", ingredience)

# volání funkce udelej_pizzu()
udelej_pizzu("sýr", "šunka", "rajče", "houby")





