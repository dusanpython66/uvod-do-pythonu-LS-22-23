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


pozdrav(prijmeni="Kolář", jmeno="Petr")

print("Karel Novák", "Petr Kolář", sep="     ")  # sep je parametr funkce print (oddělovač) - defaultně je mezera


# defaultní hodnoty parametrů
def pozdrav(jmeno="Karel", prijmeni="Novák"):
    print(f"Pan/Paní {jmeno} {prijmeni}")


pozdrav()


# funkce s parametry

def prepona(a, b):
    c = (a ** 2 + b ** 2) ** (1 / 2)
    print("c = ", c)


prepona(3, 4)


# funkce vracející hodnotu:

def prepona(a, b):
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c  # vrací hodnotu proměnné c


delkaPrepony = prepona(3, 4)  # uložíme si hodnotu proměnné c do proměnné delkaPrepony

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
f = sym.sin((2 * x) / (x ** 2 + 1))
print(sym.diff(f, x))

#######  externí moduly vytvořené uživatelem

# import  uživatelského modulu umístěného v podadresáři projektu ./Lekce_2
import sys

sys.path.append('./Lekce_2/A-funkceModuly')
from mujModul import delkaPrepony  # import uživatelského modulu

# volání funkce z uživatelského modulu:
c = delkaPrepony(3, 20)
print(c)

print(1 / 0)


# handling exceptions  (zachytávání výjimek)
# Syntaxe:
# try:   # povinný blok  (pokud dojde k vyvolání výjimky, přeskočí se na blok except)
#     <kód>
# except <výjimka>:    # nepovinný blok  (pokud dojde k vyvolání výjimky, vykoná se tento blok)
#     <kód>
# else:   # nepovinný blok  (vykoná se pokud nedošlo k vyvolání výjimky)
#     <kód>
# finally:   # nepovinný blok  (vykoná se vždy)
#     <kód>


def prepona(a, b):
    try:  # pokusí se provést následující kód
        c = (a ** 2 + b ** 2) ** (1 / 2)
    except TypeError:  # pokud dojde k vyvolání výjimky TypeError
        print("Funkce přijímá pouze čísla")
    else:  # pokud nedošlo k vyvolání výjimky
        return c


prepona("a", 3)


# Ukažme příklad s použitím klíčového slova finally.

def prepona(a, b):
    try:
        c = (a ** 2 + b ** 2) ** (1 / 2)
    except TypeError:
        print("Funkce přijímá pouze čísla")
    else:  # pokud nedošlo k vyvolání výjimky
        return c
    finally:
        print("Toto se vypíše vždy")


prepona("aů", 3)


def vydel(num1, num2):
    """
    Funkce vydel() vrací výsledek dělení dvou čísel.
    Pokud je dělitel nula, vypíše se chybová hláška a funkce vrací None.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Nelze dělit nulou.")
        return None  # None je speciální hodnota, která značí prázdnou hodnotu
    else:
        print(f"Výsledek dělení je {result}.")
        return result
    finally:
        print("Funkce vydel() byla ukončena.")


# Příklad použití
result = vydel(10, 0)


# Výjimky můžeme vyvolávat i sami pomocí klíčového slova raise.
# Syntaxe:
# raise <výjimka>(<parametry>)
# Příklad:

def prepona(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("Funkce přijímá celá nebo desetinná čísla")
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c


prepona(3.14, 4)


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


# Uveďme příklad funkce, která kombinuje poziční argumenty
# a dále umožňuje předávat libovolný počet parametrů.


def udelej_pizzu(velikost, *ingredience):
    print("Velikost: ", velikost)
    print("Ingredience: ", ingredience)


udelej_pizzu("velká", "sýr", "šunka", "rajče", "houby")


# **kwargs - předává libovolný počet pojmenovaných parametrů do funkce ve formě slovníku

def udelej_pizzu(velikost, *ingredience, **dalsi_ingredience):
    print("Velikost: ", velikost)
    print("Ingredience: ", ingredience)
    print("Další ingredience: ", dalsi_ingredience)


udelej_pizzu("velká",
             "sýr", "šunka", "rajče", "houby",
             extra_syr=True, extra_sunka=True)
