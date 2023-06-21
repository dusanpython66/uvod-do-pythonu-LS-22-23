# Použití tzv. f-řetězců

jmeno = "karel"
prijmeni = "novák"

# print(f"Pan {jmeno} {prijmeni}")

# formátování řetězce pomocí metody format()
# {} tvoří tzv. "placeholder" - místo, kam se vloží hodnota
print("Pan {} {}".format(jmeno, prijmeni))

jmeno = input("Napiš svoje jméno: ")
prijmeni = input("Napiš svoje příjmení: ")
print(f"{jmeno} {prijmeni}".title())

print(f"{jmeno} {prijmeni}".upper())
