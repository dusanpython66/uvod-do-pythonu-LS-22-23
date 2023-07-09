"""
Úkol 1: Vytvořte slovník s názvem 'ovoce', který bude obsahovat následující klíče a hodnoty:
    "jablko": 10
    "pomeranč": 15
    "banán": 20
    "hruška": 5
"""

# Řešení:
ovoce = {
    "jablko": 10,
    "pomeranč": 15,
    "banán": 20,
    "hruška": 5
}

"""
Úkol 2: Přístup k hodnotám vytvořeného slovníku
    Vypište na obrazovku počet hrusek a banánů ze slovníku z úkolu 1.
"""

# Řešení:
print("Počet hrušek:", ovoce["hruška"])
print("Počet banánů:", ovoce["banán"])

"""
Úkol 3: Aktualizace hodnot vytvořeného slovníku
    Přidejte do slovníku 'ovoce' 2 nové hrušky a 1 nový banán.
    Vypište upravený slovník 'ovoce' na obrazovku.
"""

# Řešení:
ovoce["hruška"] += 2
ovoce["banán"] += 1
print(ovoce)

"""
Úkol 4: Vytvoření n-tice
    Vytvořte n-tici s názvem 'barvy', která bude obsahovat následující hodnoty:
    "červená", "modrá", "zelená", "žlutá".
"""

# Řešení:
barvy = ("červená", "modrá", "zelená", "žlutá")

"""
Úkol 5: Přístup k hodnotám vytvořené n-tice
    Vypište na obrazovku první a třetí barvu ze n-tice z úkolu 4.
"""

# Řešení:
print("První barva:", barvy[0])
print("Třetí barva:", barvy[2])

"""
Úkol 6: Iterace přes slovník a n-tici
    Iterujte přes slovník 'ovoce' a vypište na obrazovku klíče a hodnoty.
    Iterujte přes n-tici 'barvy' a vypište na obrazovku index a hodnotu každé barvy.
"""

# Řešení:
# iterace přes slovník:
for klic, hodnota in ovoce.items():
    print(klic, hodnota)

# iterace přes n-tici:
start = 0
n = start
for barva in barvy:
    print(n, barva)
    n += 1

# nebo s využitím funkce enumerate():
for index, barva in enumerate(barvy):  # enumerate() vrací index a hodnotu prvků n-tice
    print(index, barva)

# transformujme objekt enumerate() na slovník:
barvy_slovnik = dict(enumerate(barvy))
print(barvy_slovnik)

"""
Úkol 7: Slovník a n-tice v sobě
    Vytvořte slovník s názvem 'barvy_pocet', který bude obsahovat následující klíče a hodnoty:
    "červená": (255, 0, 0)
    "modrá": (0, 0, 255)
    "zelená": (0, 255, 0)
    "žlutá": (255, 255, 0)

    Vypište RGB hodnoty pro barvu 'modrá' ze slovníku 'barvy_pocet'.
"""

# Řešení:
barvy_pocet = {
    "červená": (255, 0, 0),
    "modrá": (0, 0, 255),
    "zelená": (0, 255, 0),
    "žlutá": (255, 255, 0)
}

print(barvy_pocet["modrá"])

