# Jak se vytvoří seznam?
seznam1 = [1, 2, 3, 4, 5] # vytvoříme seznam s několika prvky
print(seznam1)


# jak získáme prvek seznamu?
# první prvek seznamu má index 0
# poslední prvek seznamu má index -1

print(seznam1[0]) # vytiskne 1, index se zadává do hranatých závorek
print(seznam1[4]) # vytiskne 5, index se zadává do hranatých závorek
print(seznam1[-1]) # vytiskne 5, index se zadává do hranatých závorek
print(seznam1[-2]) # vytiskne 4, index se zadává do hranatých závorek
 

nakup = [] # vytvoříme prázdný seznam
print(nakup)

# přidávejme postupně prvky do seznamu
nakup.append("jablko")
nakup.append("hruska")
nakup.append("banan")
print(nakup)

# vytvořme seznam čísel 1,...,10
seznam2 = []
for i in range(1, 11):
    seznam2.append(i)
print(seznam2)

# pomocí "list comprehensions" vytvoříme seznam čísel 1,...,10
seznam3 = [i for i in range(1, 11)] # vytvoříme seznam s několika prvky
print(seznam3)

suda_cisla = [i for i in range(1, 11) if i % 2 == 0] # vytvoříme seznam s několika prvky
print(suda_cisla)

# spojení seznamů pomocí operátoru +
seznam4 = seznam2 + seznam3
print("seznam4 = ", seznam4)

# metoda extend
# syntakticky stejná jako metoda append
# rozdíl je v tom, že metoda append přidává do seznamu jeden prvek
# použití operátoru + je také možné použít pro spojení seznamů
seznam5 = [1, 2, 3]
seznam6 = [4, 5, 6]
seznam5.extend(seznam6)
print("seznam5 = ", seznam5)

# metoda join
# spojí prvky seznamu do jednoho řetězce pomocí zadaného oddělovače
# metoda join je dostupná pouze pro řetězce (tj. pro datový typ str)
nakup2 = ["chleba", "máslo", "vejce"]
nakup3 = ",".join(nakup2)  # spojí prvky seznamu do jednoho řetězce
print(nakup3)
print(type(nakup3))

# metoda split - rozdělí řetězec na seznam
nakup4 = "chleba,máslo,vejce, mléko"
nakup5 = nakup4.split(",")  
print(nakup5)

# změna prvku seznamu, změníme první prvek seznamu nakup5
nakup5[0] = "rohlíky"
print(nakup5)

# smažme například poslední prvek seznamu
del nakup5[-1]
print(nakup5)

# třídění seznamu
# třídění pomocí metody sort

s = [5, 3, 1, 2, 4]
s.sort()  # třídění vzestupně
print(s)
s.sort(reverse=True)  # třídění sestupně
print(s)

# třídění pomocí funkce sorted  - vrací nový seznam
s2 = sorted(s)
print(s2)
print(s)  # seznam s zůstává nezměněn

# použití metody reverse pro seznamy
print(s)
s.reverse()  # obrátí pořadí prvků v seznamu  - změní seznam s permanentně
print(s)


# ořezání seznamu
# pomocí metody slice
s2 = s[1:3]  # ořízneme seznam od druhého prvku do třetího prvku
print(s2)

 # ořízněme seznam s od konce
s3 = s[-2:]
print(s3)

# pomocí metody pop odstraníme poslední prvek seznamu
posledniPrvek = s.pop()  # odstraní poslední prvek seznamu
print(posledniPrvek)
print(s)

# pomocí metody pop odstraníme první prvek seznamu:
prvniPrvek = s.pop(0)  # odstraní první prvek seznamu
print(prvniPrvek)
print(s)

# smažme prvek seznamu pomocí metody remove
s.remove(3)  # odstraní prvek 3 ze seznamu
print(s)

# klíčové slovo in a jeho použití pro seznamy

# zjistíme, zda je prvek 5 v seznamu s
print(s)
print(5 in s)

# ukažme, jak lze vytvořit kopii seznamu
# pomocí operátoru =
s4 = s
print(s4)
s4[0] = 100
print(s4)
print(s)  # změna se projeví i v seznamu s - toto není kopie seznamu

# vytvořme kopii seznamu pomocí metody copy
s5 = s.copy()
print(s5)
s5[0] = 200
print(s5)
print(s)  # změna se neprojeví v seznamu s - toto je kopie seznamu!

# for cyklus pro seznamy - procházení seznamu
print(s)
for prvek in s:
    print(prvek)

# Příklad: vytvořme seznam čísel 1,...,10
# potom sečtěme druhé mocniny těchto čísel
# použijeme cyklus for přes prvky seznamu

seznam6 = [i for i in range(1, 11)]
print(seznam6)

soucet = 0
for prvek in seznam6:
    soucet += prvek**2
print(soucet)


