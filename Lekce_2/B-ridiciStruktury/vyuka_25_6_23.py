# if-příkaz
# syntaxe tohoto příkazu je následující:
# if podmínka:
#     příkaz1
#     příkaz2
#     ...
#     příkazN

# příklad:

# syntaxe příkazu if-else je následující:
# if podmínka:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# else:
#     příkaz1
#     příkaz2
#     ...
#     příkazN

# vek = int(input("Zadej svůj věk: "))
# if vek >= 18 and vek <= 65:
#     print("Jsi pracující")
# else:
#     print("Jsi nepracující")

# print("Konec programu")

# konstrukce if-elif-else
# syntaxe příkazu if-elif-else je následující:
# if podmínka1:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# elif podmínka2:
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# elif podmínka3:   
#     příkaz1
#     příkaz2
#     ...
#     příkazN
# else:
#     příkaz1
#     příkaz2
#     ...
#     příkazN

# příklad: známlka z testu
# známky budou udělovány podle následujícího klíče:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 50-59
# F: 0-59

# vstup od uživatele
# znamka = "neznámá"
# skore = int(input("Zadej své skóre: "))  # skore je v rozsahu 0-100

# # výpočet známky
# if skore >= 90:
#     znamka = "A"

# elif skore >= 80:
#     znamka = "B"

# elif skore >= 70:
#     znamka = "C"

# elif skore >= 60:
#     znamka = "D"

# elif skore >= 50:
#     znamka = "E"

# else:
#     znamka = "F"

# výstup
# print("Tvoje známka je: " + znamka)

# do vnořené podmínky if-else
vek = int(input("Zadej svůj věk: "))
if vek < 4:
    cena = 0
else:
    if vek < 18:
        cena = 25
    else:
        if vek < 65:
            cena = 40
        else:
            cena = 20

print('Cena vstupenky je: ' + str(cena) + " Kč")

print(f"Cena vstupenky je: {cena} Kč")  # f-string

a = 5
b = 10
print(a)
print(b)

# výměna hodnot
# pomocí pouze proměnných vyměnily obsah proměnné a a b

c=a
a=b
b=c


