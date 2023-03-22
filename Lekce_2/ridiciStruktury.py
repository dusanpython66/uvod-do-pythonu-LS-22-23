# Řídící konstrukce

# if-elif-else konstrukce:
x = float(input("zadejte reálné číslo x = "))
if x >= 0:
    print("|x| = ", x)
else:
    print("|x| = ", - x)

skore = int(input("Zadej výsledek testu: "))

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

########## cykly while a for ####################


# příklad na požití cyklu "for"
#  najděme součet prvních sto přirozených čísel:
# 1 + 2 + 3 + ... +100

N = 100

soucet = 0 # výchozí hodnota součtu

for n in range(1, N + 1):
    soucet = soucet + n
    print("Částečná suma je rovna: ", soucet)
print("součet je roven = ", soucet)

# příklad cyklu while

N = 100

s = 0
n = 1
while n <= N:
    s = s + n
    n += 1 # n = n + 1
print("Součet je roven číslu: ", s)

# vyjímky try-except
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Chyba: Dělení nulou není možné.")

x = int(input("Zadej číslo: "))

try:
    x = int(input("Zadej číslo: "))
except ValueError:
    print("Chyba: Zadán neplatný vstup. Zadej prosím číslo.")

print("Zadej dvě čísla a obdržíš jejich podíl")
print("Pro ukončení programu stiskni klávesu 'q' ")

while True:
    prvni_cislo = input("Dělenec  = ")
    if prvni_cislo == 'q':
        break
    druhe_cislo = input("Dělitel = ")
    if druhe_cislo == 'q':
        break
    vysledek = int(prvni_cislo) / int(druhe_cislo)
    print(vysledek)

print("Zadej dvě čísla a obdržíš jejich podíl")
print("Pro ukončení programu stiskni klávesu 'q' ")

while True:
    prvni_cislo = input("Dělenec  = ")
    if prvni_cislo == 'q':
        break
    druhe_cislo = input("Dělitel = ")
    if druhe_cislo == 'q':
        break
    try:  # pokusíme se provést následující kód
        vysledek = int(prvni_cislo) / int(druhe_cislo)
    except ZeroDivisionError:
        print("Nulou dělit nelze!")
    else:
        print(vysledek)



# další příklad na použití cyklu while
# výpočet faktoriálu čísla n
n = int(input("Zadej číslo: ")) # vyžádáme si od uživatele vstup
faktorial = 1 # výchozí hodnota faktoriálu
while n > 1:
    faktorial = faktorial * n
    n = n - 1
print("Faktoriál je roven: ", faktorial)

# další příklad na použití cyklu while
# výpočet faktoriálu čísla n
faktorial = 1 # výchozí hodnota faktoriálu

# vytvořme dva do sebe vnořené cykly for
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("") # vytiskne prázdný řádek

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
    print("") # vytiskne prázdný řádek