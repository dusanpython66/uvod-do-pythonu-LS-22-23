# příklad cyklu while s klíčovým slovem break

print("Zadej dvě čísla a obdržíš jejich podíl.")
print("Pro ukončení programu stiskni klávesu 'q'.")

while True:
    delenec = input("Zadej delence: ")
    if delenec == "q":
        break  # cyklus je ukončen
    delitel = input("Zadej delitele: ")
    if delitel == "q":
        break  # ukončí se cyklus while

    vysledek = float(delenec) / float(delitel)
    print(vysledek)

    # try-except
    # syntaxe:
    # try:
    příkaz1
    příkaz2
    příkaz3
    ...
except < typ
chyby >:
příkaz1
příkaz2
příkaz3
...

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Chyba: nulou dělit nelze!")

# Konstrukce try-except-else

while True:
    try:
        delenec = input("Zadej delence: ")
        if delenec == "q":
            break  # cyklus je ukončen
        delitel = input("Zadej delitele: ")
        if delitel == "q":
            break  # ukončí se cyklus while
        vysledek = float(delenec) / float(delitel)
        print(vysledek)
    except ZeroDivisionError:
    print("Nulou dělit nelze!")

# Konstrukce try-except-else-finally

# Příklad

try:
    x = int(input("Zadej celé číslo: "))
except ValueError:
    print("Chyba: zadána nesprávná hodnota!")
else:
    print("Výsledek je: ", x)
finally:
    print("Nakonec se provede to, co je v bloku finally ať už nastala chyba nebo ne.")

# použití klíčového "continue"

# Vypíšeme na konzoli všechna čísla od 1 do 10 s vyjímkou čísla 5

for k in range(1, 11):
    print(k)

k = 0

while k < 10:
    k += 1  # k = k + 1
    if k == 5:
        continue  # vracíme se zpátky na začátek cyklu while
    print(k)

