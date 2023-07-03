# Vytvořme slovník
# syntaxe:
# <název_slovníku> = {<klíč_1>: <hodnota_1>, <klíč_2>: <hodnota_2>, ...}
# klíč - musí být unikátní, hodnota - může se opakovat (může být i slovník)

slovnik = {"jedna": 1, "jedna": 2}  # program si vezme poslední hodnotu, tj. 2
print(slovnik)

a = {"jedna": 1, "dva": 2, "tři": 3}  # Klíč: hodnota (key: value)
print(a)

# Vytvořme slovník jako tel. seznam
# slovník obsahuje podobná data, proto používáme formátování slovníku
# tak, že každou dvojici key-value píšeme na samostatný řádek
telSeznam = {
    "Karel": 123456789,
    "Petr": 987654321,
    "Jana": 123456789
}

# Co může být klíčem?
# Klíčem může být jakýkoliv objekt, který je immutable (nezměnitelný). Např. číslo, řetězec, tuple.

# Přístup k hodnotě podle klíče
print(telSeznam["Karel"])

# Pokud klíč neexistuje, dojde k vyvolání výjimky KeyError
print(telSeznam["Pavel"])

# Zjištění, zda klíč existuje
print("Pavel" in telSeznam)

# Zjištění, zda hodnota existuje
print(123456789 in telSeznam.values())

# Použití metody get()
# get() vrací hodnotu podle klíče, pokud klíč neexistuje, vrací None
# Hodnota None je speciální objekt, který značí, že hodnota neexistuje

print(telSeznam.get("Pavel"))

# V případě, že klíč neexistuje, můžeme specifikovat, co má metoda get() vrátit:
print(telSeznam.get("Pavel", "Klíč neexistuje"))

# Přidání položky do slovníku
telSeznam["Pavel"] = 123456789
print(telSeznam)

# Změna hodnoty podle klíče
telSeznam["Petr"] = 987654388
print(telSeznam)

# Odstranění položky ze slovníku
del telSeznam["Pavel"]
print(telSeznam)

# Zobrazení všech klíčů
print(telSeznam.keys())
# dict_keys je iterovatelný objekt, který obsahuje všechny klíče slovníku

# Zobrazení všech hodnot
print(telSeznam.values())
# dict_values je iterovatelný objekt, který obsahuje všechny hodnoty slovníku

# Iterace přes slovník
for klic in telSeznam:
    print(klic, telSeznam[klic])

# Iterace přes klíče
for klic in telSeznam.keys():
    print(klic)

# Iterace přes hodnoty slovníku
for hodnota in telSeznam.values():
    print(hodnota)

# Iterace přes dvojice key-value
print(telSeznam)
print(telSeznam.items())
for klic, hodnota in telSeznam.items():
    print(klic, hodnota)

# Vytvoření slovníku z iterovatelného objektu
# syntaxe:
# <název_slovníku> = dict(<iterovatelný_objekt>)
# iterovatelný objekt - seznam dvojic key-value

slovnik = dict([("jedna", 1), ("dva", 2), ("tři", 3)])
print(slovnik)

# Generování slovníku automaticky přidáváním dvojic key-value
# do prázného slovníku

slovnik = {}
for i in range(10):
    slovnik[i] = i ** 2
print(slovnik)
