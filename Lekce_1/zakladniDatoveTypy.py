 # Základní datové typy
# Celá čísla  pythonovský typ je "int"

type(25)

print(2 - 3)  # sčítání a odečítání celých čísel

print(type(2+3))

print(3*9)   # násobení
print(25 / 5)   # dělení

print(10 // 3)  # neúplný podíl

# modulární dělení:

print(10 % 3)

# umocňování :
print(2**10)  # 2 na desátou
print(pow(2, 10))

########## Desetinná čísla ##############

print(type(3.14))  # pythonovský typ je "float"
print(type(round(3.14)))  # funkce "round" zaokrouhlí číslo na celé číslo
from math import pi  # importujeme z modulu "math" konstantu "pi"
print(pi)

########## boolovské hodnoty ############
# True, False
print(1 < 2)  
print(1 >= 5)
print(1 == 2)  # relační operátor rovnosti
print(1 <= 2)
print(1 < 2 or 1 == 2) # "or" je logická spojka "nebo"
print(1 < 2 and 1 == 2) # "and" je logická spojka "a zároveň"
print(True or False)
print((True or False) and (False or False))
print(1 != 2) # "!=" "není rovno"

################# Řetězce ################
# Definice řetězce: Řetězce se definují jako posloupnost znaků
# uzavřených v
# jednoduchých nebo dvojitých uvozovkách (např. 'hello' nebo "world").

print("Toto je řetězec")

### Spojování konkatenace řetězců

print("Ahoj" + " Karle.")  # spojili jsme dva řetězce "Ahoj" a " Karle."
print("Ahoj", "Petře!")
print("ABCD" + "ABCD" + "ABCD" + "ABCD" + "ABCD")
print("ABCD" * 5)
print("-" * 50)
print("+" * 5)
# indexování řetězců

"Ahoj"[0]
"Ahoj"[3]
"Ahoj bcbcbcbcbcbcbcbcbcbcbcb"[-1]
"Ahoj bcbcbcbcbcbcbcbcbcbcbcb"[-2]
"Ahoj bcbcbcbcbcbcbcbcbcbcbcb"[-3]
len("Ahoj bcbcbcbcbcbcbcbcbcbcbcb") # funkce "len" nám vrátí počet znaků řetězce
"Ahoj bcbcbcbcbcbcbcbcbcbcbcb"[27]


# Slicing řetězců:
"Ahoj"[1:3]
"Ahoj"[1:-1]
"Ahoj"[:-1]
"Ahoj"[1:]

# Funkce pro práci s řetězci:
len("Ahoj")  # délka řetězce

# upper("karel")
"karel".upper()
"Karel".lower()

# funkce "type"
type(555)
type(3.14)
type("řetězec")
type(True)
type(1 < 2)
type((1 <= -1) or (1 == 2))

