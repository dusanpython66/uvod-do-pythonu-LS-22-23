# Úkol 3
# Napište funkci, která bude řešit binární vyhledávání (binary search).
# Binární vyhledávání (binary search) je algoritmus pro nalezení určitého 
#prvku v setříděném seznamu prvků.
# Princip binárního vyhledávání spočívá v rozdělení 
#seznamu na dvě poloviny a porovnání
#
# hledaného prvku s prvkem uprostřed seznamu.
# Pokud je hledaný prvek menší než prvek uprostřed seznamu,
# pak víme, že se musí nacházet v levé polovině a můžeme se 
#omezit pouze na tuto polovinu.
# Pokud je hledaný prvek větší než prvek uprostřed seznamu, 
#pak víme, že se musí nacházet v
# pravé polovině a můžeme se omezit na tuto polovinu.
#
# Tento proces opakujeme tak dlouho, dokud nenajdeme hledaný prvek, nebo
# dokud není seznam prázdný. Pokud hledaný prvek není v seznamu, pak vracíme
# informaci o tom, že prvek není nalezen.
#
# Funkce pro binární vyhledávání obvykle přijímá dva argumenty:
# setříděný seznam a hledaný prvek. Funkce poté vrací buď index nalezeného prvku
# v seznamu, nebo informaci o tom, že prvek nebyl nalezen.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return "Prvek nebyl nalezen."

a = [1, 4, 74, 89]
indx = binary_search(a, x = 5)
print(indx)
""" 
# napišme funkci, která vezme jeden parametr a vrátí jeho druhou mocninu
def mocnina2(x):
    return x**2 """


# vytvořme dva do sebe vnořené cykly for
""" for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("") # vytiskne prázdný řádek

# vytvořme dva do sebe vnořené cykly while
i = 1
while i < 11:
    # vnořený cyklus
    j = 1
    while j < 11:  # vnořený cyklus
        # příkaz

        j = j + 1
    i = i + 1 """


# q: How can we create a dictionary?
# a: We can create a dictionary by using curly brackets {} and
# separating key-value pairs by commas.
# We can also create a dictionary by using the dict() function.
# The dict() function takes a list of key-value pairs as an argument.
# Each key-value pair is a tuple.
# We can also create a dictionary by using the dict() function.
#slovnik = {"jmeno": "Petr", "prijmeni": "Novak", "vek": 25}
#print(slovnik)


