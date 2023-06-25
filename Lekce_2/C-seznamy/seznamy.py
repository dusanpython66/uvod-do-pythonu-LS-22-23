# Jak se vytvoří seznam?
seznam1 = [1, 2, 3, 4, 5] # vytvoříme seznam s několika prvky
print(seznam1)


# jak získáme prvek seznamu?
# první prvek seznamu má index 0
#print(seznam1[0]) # vytiskne , index se zadává do hranatých závorek
#print(seznam1[4]) # vytiskne 5, index se zadává do hranatých závorek
#print(seznam1[-2]) # vytiskne 5, index se zadává do hranatých závorek

print(seznam1[0]) # vytiskne 1, index se zadává do hranatých závorek
print(seznam1[4]) # vytiskne 5, index se zadává do hranatých závorek
print(seznam1[-2]) # vytiskne 4, index se zadává do hranatých závorek


nakup = [] # vytvoříme prázdný seznam
print(nakup)

# přidávejme postupně prvky do seznamu
nakup.append("jablko")
nakup.append("hruska")
nakup.append("banan")
print(nakup)
print(type(nakup))

# vytvořme seznam čísel 1,...,10
# pomocí comprehension
seznam2 = [i for i in range(1, 11)] # vytvoříme seznam s několika prvky

# pomocí cyklu for
seznam3 = []
for i in range(1, 11):
    seznam3.append(i)

print("seznam2 = ", seznam2)
print("seznam3 = ", seznam3)

# spojme dva seznamy
seznam4 = seznam2 + seznam3
print("seznam4 = ", seznam4)

# metoda join
nakup2 = ["chleba", "máslo", "vejce"]
nakup3 = ",".join(nakup2)  # spojí prvky seznamu do jednoho řetězce
print(nakup3)

# metoda split
nakup4 = "chleba,máslo,vejce"
nakup5 = nakup4.split(",")  # rozdělí řetězec na seznam
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
s.sort(reverse=False)  # třídění sestupně
print(s)

# ořezání seznamu
# pomocí metody slice
s2 = s[1:3]  # ořízneme seznam od druhého prvku do třetího prvku
print(s2)
 # ořízněme seznam s od konce
s3 = s[-2:]
print(s3)

# pomocí metody pop
posledniPrvek = s.pop()  # odstraní poslední prvek seznamu
print(posledniPrvek)
print(s)