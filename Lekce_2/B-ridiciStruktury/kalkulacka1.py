cis1 = float(input("Zadejte první číslo: "))

operace = input("Zadejte operaci (+, -, *, /): ")

cis2 = float(input("Zadejte druhé číslo: "))

if operace == "+":
    print(cis1 + cis2)
elif operace == "-":
    print(cis1 - cis2)
elif operace == "*":
    print(cis1 * cis2)
elif operace == "/":
    if cis2 == 0:
        print("Nulou nelze dělit")
    else:
        print(cis1 / cis2)
else:
    print("Neznámá operace")


# přidejme validaci vstupu pro operaci dělení "/"

cis1 = float(input("Zadejte první číslo: "))
operace = input("Zadejte operaci (+, -, *, /): ")
cis2 = float(input("Zadejte druhé číslo: "))

if operace == "+":
    print(cis1 + cis2)
elif operace == "-":
    print(cis1 - cis2)
elif operace == "*":
    print(cis1 * cis2)
elif operace == "/":
    while cis2 == 0:
        print("Nulou nelze dělit")
        cis2 = float(input("Zadejte druhé číslo: "))
    print(cis1 / cis2)
else:
    print("Neznámá operace")

# přidejme ještě další operaci "mocnina" "**"

cis1 = float(input("Zadejte první číslo: "))
operace = input("Zadejte operaci (+, -, *, /, **): ")
cis2 = float(input("Zadejte druhé číslo: "))

if operace == "+":
    print(cis1 + cis2)
elif operace == "-":
    print(cis1 - cis2)
elif operace == "*":
    print(cis1 * cis2)
elif operace == "/":
    while cis2 == 0:
        print("Nulou nelze dělit")
        cis2 = float(input("Zadejte druhé číslo: "))
    print(cis1 / cis2)
elif operace == "**":
    print(cis1 ** cis2)
else:
    print("Neznámá operace")

    




