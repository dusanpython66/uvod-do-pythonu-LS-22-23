# Použití tzv. f-řetězců

jmeno = "petr"
prijmeni = "svoboda"

print(f"Pan {jmeno} {prijmeni}")
print(f"Pan {jmeno} {prijmeni} je na řadě.")

# formátování řetězce pomocí metody format()
# {} tvoří tzv. "placeholder" - místo, kam se vloží hodnota
print("Pan {} {}".format(jmeno, prijmeni))

jmeno = input("Napiš svoje jméno: ")
prijmeni = input("Napiš svoje příjmení: ")
print(f"{jmeno} {prijmeni}".title())

print(f"{jmeno} {prijmeni}".upper())

print(f"{jmeno} {prijmeni}".lower())