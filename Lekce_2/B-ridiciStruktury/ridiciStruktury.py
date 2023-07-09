# Řídící konstrukce

# Pro znázornění řídících konstrukcí se někdy používají tzv. vývojové diagramy.
# Ukázku tzv. "vývojoového diagramu" najdete na odkazu:
# https://cs.wikipedia.org/wiki/V%C3%BDvojov%C3%BD_diagram

# program pro kreslení vývojových diagramů najdete např. na odkazu:
# https://www.draw.io/

# If-příkaz
# Příkaz if je základním příkazem pro větvení programu.
# Syntaxe příkazu if je následující:
# if podmínka:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
#     příkazN+1
#     ...

# Příklad na použití if konstrukce:
# zadejte váš věk a program vypíše, zda jste dospělý nebo ne
vek = int(input("Zadejte váš věk: "))
if vek >= 18:
    print("Jste dospělý")
print("Konec programu")

# Konstrukce if-else
# Syntaxe příkazu if-else je následující:
# if podmínka:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# else:
#     příkazN+1
#     příkazN+2
#     ...


# Příklad na použití if-else konstrukce:
# zadejte číslo a program vypíše, zda je číslo kladné, záporné nebo nulové
x = float(input("zadejte reálné číslo x = "))
if x > 0:
    print("Číslo je kladné")
elif x < 0:
    print("Číslo je záporné")
else:
    print("Číslo je rovno nule")

# o absolutní hodnotě viz odkaz: https://cs.wikipedia.org/wiki/Absolutn%C3%AD_hodnota
# if-elif-else konstrukce:
x = float(input("zadejte reálné číslo x = "))
if x >= 0:
    print("|x| = ", x)
else:
    print("|x| = ", - x)

# známkování testu:

skore = int(input("Zadej výsledek testu: "))  # výsledek testu je celé číslo

if skore > 90:
    print("Známka je A")
elif 80 < skore <= 90:
    print("Známka je B")
elif 70 < skore <= 80:
    print("Známka je C")
elif 60 < skore <= 70:
    print("Známka je D")
elif 50 < skore <= 60:
    print("Známka je E")
else:
    print("Známka je F")

print("Konec programu")

# Blok else je nepovinný.

# Příklad na použití if-elif konstrukce bez bloku else:
vek = int(input("Zadejte váš věk: "))
cena = "neznámá"
if vek < 4:
    cena = 0
elif vek < 18:
    cena = 25
elif vek < 65:
    cena = 40
elif vek >= 65:  # tento poslední blok elif zachytí všechny věkové kategorie, které nejsou výše uvedeny!
    cena = 20
print(f"cena vstupenky je {cena} Kč")  # f-string

# Příklad na použití do sebe vnořených if-else konstrukcí:
vek = int(input("Zadejte váš věk: "))
if vek < 4:
    cena = 0
else:
    if vek < 18:
        cena = 25
    else:
        if vek < 65:
            cena = 40
        else:
            cena = 20
print(f"cena vstupenky je {cena} Kč")  # f-string

# Ve vašem kódu je možné, že pokud uživatel vstoupí něco,
# co není číslo, pak cena nebude definována, ale stále se
#  pokoušíme tuto proměnnou vytisknout.
# Toto by vedlo k chybě.

# Chcete-li tuto potenciální chybu opravit, můžete
# inicializovat proměnnou cena na nějakou výchozí
# hodnotu předtím, než ji použijete v podmíněném bloku.
# Například takto:

vek = input("Zadejte váš věk: ")
cena = "Neznámá"  # Nastavení výchozí hodnoty

if vek.isdigit():  # metoda isdigit() zjistí, zda je řetězec číslo
    vek = int(vek)
    if vek < 4:
        cena = 0
    elif vek < 18:
        cena = 25
    elif vek < 65:
        cena = 40
    elif vek >= 65:
        cena = 20
else:
    print("Zadaný věk musí být číslo.")

print(f"Cena vstupenky je {cena} Kč")

########## cykly while a for ####################

############# cyklus for ####################

# cyklus for se používá, pokud známe počet opakování
# syntaxe cyklu for:
# for proměnná in rozsah:
#     příkaz1
#     příkaz2
#     ...
#     příkazk

# proměnná rozsah může být např.:
# 1) rozsah celých čísel od 0 do pocetZapalek-1: range(pocetZapalek)
# 2) rozsah celých čísel od M do pocetZapalek-1: range(M, pocetZapalek)
# 3) rozsah celých čísel od M do pocetZapalek-1 s krokem K: range(M, pocetZapalek, K)


# příklad na požití cyklu "for"
#  najděme součet prvních sto přirozených čísel:
# 1 + 2 + 3 + ... +100

N = 100  # počet čísel, která chceme sečíst (včetně)

soucet = 0  # výchozí hodnota součtu

for n in range(1, N + 1):
    soucet = soucet + n
    print("Částečná suma je rovna: ", soucet)
print("součet je roven = ", soucet)

print(range(1, 11))  # vytiskne rozsah od 1 do 10
# příklad na požití cyklu "for"
for i in range(-1, 12, 3):
    print(i)

# vytvořme dva do sebe vnořené cykly for
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("")  # vytiskne prázdný řádek

########## cyklus while ####################

# cyklus while s používá, pokud neznáme počet opakování
# syntaxe cyklu while:
# while podmínka:
#     příkaz1
#     příkaz2
#     ...
#     příkazN


# příklad cyklu while

N = 100

s = 0
n = 1
while n <= N:
    s = s + n
    print("Částečná suma je rovna: ", s)  # vytiskne částečný součet
    n += 1  # n = n + 1 , += je zkrácený zápis je to operátor inkrementace
    print("n = ", n)
print("Součet je roven číslu: ", s)

# Příklad na použití cyklu while:

print("Zadej dvě čísla a obdržíš jejich podíl")
print("Pro ukončení programu stiskni klávesu 'q' ")

while True:
    prvni_cislo = input("Dělenec  = ")
    if prvni_cislo == 'q':
        break  # ukončí cyklus while
    druhe_cislo = input("Dělitel = ")
    if druhe_cislo == 'q':
        break  # ukončí cyklus while
    vysledek = int(prvni_cislo) / int(druhe_cislo)
    print(vysledek)

# Příklad cyklu while kde uživatel rozhoduje, kdy chce ukončit program:

promt = "Napiš něco a já to zopakuji. "
promt += "\nPro ukončení programu napiš 'quit': "

message = ""
while message != 'quit':
    message = input(promt)  # uloží obsah proměnné promt do proměnné message

    if message != 'quit':
        print(message)

# vyjímky try-except
# syntaxe:
# try:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# except typ_chyby:
#     příkaz1
#     příkaz2
#     ...
#     příkazN

# příklad na použití try-except
# v tomto příkladě se pokusíme vydělit číslo 5 nulou
try:  # pokusíme se provést následující kód
    x = 5 / 0
except ZeroDivisionError:  # pokud se vyskytne chyba, provede se následující kód
    print("Chyba: Dělení nulou není možné.")

# příklad na použití try-except
# v tomto příkladě se pokusíme převést řetězec na číslo
# pokud se vyskytne chyba, vypíše se chybová hláška

try:
    x = int(input("Zadej číslo: "))
except ValueError:
    print("Chyba: Zadán neplatný vstup. Zadej prosím číslo.")

# příklad na použití try-except
# program si bude žádat o zadání dvou čísel a vypíše jejich podíl
# pokud se vyskytne chyba, vypíše se chybová hláška

print("Zadej dvě čísla a obdržíš jejich podíl")
print("Pro ukončení programu stiskni klávesu 'q' ")

while True:
    prvni_cislo = input("Dělenec  = ")
    if prvni_cislo == 'q':
        break  # ukončí cyklus while
    druhe_cislo = input("Dělitel = ")
    if druhe_cislo == 'q':
        break  # ukončí cyklus while
    try:  # pokusíme se provést následující kód
        vysledek = int(prvni_cislo) / int(druhe_cislo)
    except ZeroDivisionError:
        print("Nulou dělit nelze!")
    else:  # pokud se nevznikne žádná chyba, provede se následující kód:
        print(vysledek)

# další příklad na použití cyklu while
# výpočet faktoriálu čísla n, kde n je zadané číslo od uživatele
# n! = 1 * 2 * 3 * ... * n

n = int(input("Zadej číslo: "))  # vyžádáme si od uživatele vstup
faktorial = 1  # výchozí hodnota faktoriálu
while n > 1:
    faktorial = faktorial * n
    n -= 1  # n = n - 1 , -= je zkrácený zápis pro operátor dekrementace
print("Faktoriál je roven: ", faktorial)

# další příklad na použití cyklu while
# výpočet faktoriálu čísla n

faktorial = 1  # výchozí hodnota faktoriálu

# vytvořme dva do sebe vnořené cykly while
while True:
    print("Zadej číslo pro výpočet faktoriálu:")
    print("(Pro ukončení programu stiskni klávesu 'q'.)")
    n = input()
    if n == 'q':
        break
    faktorial = 1
    i = 1
    while i <= int(n):
        faktorial = faktorial * i
        i += 1
    print("Faktoriál čísla", n, "je roven", faktorial)
    print("")  # vytiskne prázdný řádek

# další příklad na použití cyklu while

i = 0

while i < 10:
    i += 1
    if i == 5:
        print("Číslo 5 se nevypíše.")
        continue   # pokračuje se dalším průchodem cyklu !!!
    print(i)

# V tomto kódu se cyklus while opakuje, dokud i není rovno 10.
# Pokud je i rovno 5, klíčové slovo continue způsobí, že
# se zbytek cyklu přeskočí a pokračuje se dalším průchodem cyklu.
# To znamená, že číslo 5 se nevypíše.

# ukažme jak funguje klíčové slovo finally
# finally se používá vždy společně s try-except
# finally se používá pro uvolnění zdrojů, které jsme používali v try-except
# finally se vždy provede, ať už se v try-except vyskytla chyba nebo ne

try:
    x = int(input("Zadej číslo: "))
except ValueError:
    print("Chyba: Zadán neplatný vstup. Zadej prosím číslo.")

else:
    print("Výsledek je: ", x)

finally:
    print("finally se provede vždy, ať už se v try-except vyskytla chyba nebo ne")

# ukažme konstrukci try-except-else-finally uvnitř cyklu while

print("Zadej dvě čísla a obdržíš jejich podíl")
print("Pro ukončení programu stiskni klávesu 'q' ")

while True:
    prvni_cislo = input("Dělenec  = ")
    if prvni_cislo == 'q':
        break  # ukončí cyklus while
    druhe_cislo = input("Dělitel = ")
    if druhe_cislo == 'q':
        break  # ukončí cyklus while
    try:  # pokusíme se provést následující kód
        vysledek = int(prvni_cislo) / int(druhe_cislo)
    except ZeroDivisionError:
        print("Nulou dělit nelze!")
    else:  # pokud se nevznikne žádná chyba, provede se následující kód:
        print("podíl je roven číslu: ", vysledek)
    finally:
        print("finally se provede vždy, ať už se v try-except vyskytla chyba nebo ne")