# Vytvořme slovník
a = {"jedna": 1, "dva": 2, "tři": 3}  # Klíč: hodnota (key: value)   
print(a)

# Vytvořme slovník jako tel. seznam
telSeznam = {"Karel": 123456789, "Petr": 987654321, "Jana": 123456789}

# Co může být klíčem?
# Klíčem může být jakýkoliv objekt, který je immutable (nezměnitelný).

# Přístup k hodnotě podle klíče
print(telSeznam["Karel"])

# Přidání položky do slovníku
telSeznam["Pavel"] = 123456789
print(telSeznam)

# Změna hodnoty podle klíče
telSeznam["Petr"] = 987654388
print(telSeznam)

# Zobrazení všech klíčů
print(telSeznam.keys())

# Zobrazení všech hodnot
print(telSeznam.values())

# Iterace přes slovník
for klic in telSeznam:
    print(klic, telSeznam[klic])

# Iterace přes klíče
for klic in telSeznam.keys():
    print(klic)

# Iterace přes hodnoty
for hodnota in telSeznam.values():
    print(hodnota)


