# Vytváření proměnných
jmeno = "Petr"
print(jmeno)

# obsah proměnné lze později změnit
jmeno = "Pavel"
print(jmeno)

# použití proměnné lze zkrátit příkazy
print(jmeno + " je programátor.")


# delka odvěsny a
a = input("Zadej délku odvěsny a: ")
a = float(a)

# délka odvěsny b
b = input("zadej délku odvěsny b: ")
b = float(b)

c = (a**2 + b**2)**(1/2) # c je délka přepony

print("c = ", c)

# 3jmena = "karel, petr, jan"  # název proměnné by neměl začínat číslem  !!!
# print(3jmena)

# $$&& = 3

jmena_studentu = "karel, petr, jan"
print(jmena_studentu)

jmenaStudentuUniversity = "petr, honza, eliška"
print(jmenaStudentuUniversity)

# Vytvořme pozdrav s použitím f-stringu
jmeno = "Petr"
prijmeni = "Novák"
print(f"Vítej {jmeno} {prijmeni} v naší aplikaci.")

# switching values of variables
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

# switching variables using third variable
a = 1
b = 2
print(a, b)
c = a
a = b
b = c
print(a, b)





