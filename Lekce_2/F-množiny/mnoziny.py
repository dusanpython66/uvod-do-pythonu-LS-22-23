# Vytvořme prázdnou množinu a přidejme do ní několik prvků:

mnozina = set()  # prázdná množina
mnozina.add(1)
mnozina.add(2)
mnozina.add(3)
mnozina.add(4)
mnozina.add(5)
mnozina.add(6)
mnozina.add(7)
mnozina.add(8)
mnozina.add(9)
mnozina.add(10)
print(mnozina)

# Vytvořme množinu s několika prvky:

mnozina2 = {11, 12, 13}

# Vytvořme sjednocení obou množin:

sjednoceni = mnozina.union(mnozina2)
print(sjednoceni)

# Vytvořme průnik obou množin:

prunik = mnozina.intersection(mnozina2)
print(prunik)  # prázdná množina !

# Vytvořme rozdíl obou množin:

rozdil = mnozina.difference(mnozina2)
print(rozdil)  # prvky z mnoziny mnozina, které nejsou v množině s názvem mnozina2 !



