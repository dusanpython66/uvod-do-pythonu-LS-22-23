# vytvořme uspořádanou trojici
t = (1, 2, 3)

# vytvořme uspořádanou pětici
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))

# spojíme dvě n-tice:
t = t + (6, 7)  # t += (6, 7)  # t = t + 6, 7
print(t)

# vytvoříme n-tici z listu (seznamu), lze kombinovat různé datové typy:
seznam = ["Karel", 5, [1, 2, 3]]
t = tuple(seznam)
print(t)

# vytvoříme n-tici z řetězce:
retezec = "Karel"
t = tuple(retezec)
print(t)

# jak přistoupíme k prvkům n-tice?
print(t[0])
print(t[1])
print(t[2])
print(t[-1])
print(t[-2])

# Iterace přes n-tici:
for prvek in t:
    print(prvek)

# n-tice jsou nezměnitelné (immutable)
t[0] = 5
print(t)

# přidejme položku do n-tice:
t = t + (5,)
print(t)

# vytvořme n-tici postupným přidáváním prvků:
t = ()
t += (1,)
t += (2,)
t += (3,)
print(t)

# technicky vzato n-tice je definována přítomností čárek, nikoliv závorek:
t = 1, 2, 3
print(t)

# n-tice může obsahovat pouze jednu položku:
t = (1,)  # v definici n-tice s jednou položkou musí být čárka na konci

s = 1,
print(s)