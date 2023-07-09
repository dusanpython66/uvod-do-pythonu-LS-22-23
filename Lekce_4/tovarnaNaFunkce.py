# Popis: Továrna na funkce (function factory) je funkce, která vytváří funkce.
# funkce tvořené jinou funkcí dynamicky jsou tzv. uzávěry (closures)

def tovarna_na_funkce(x):
    def uzaver(y):
        return x + y
    return uzaver


# Vytvoříme uzávěru s hodnotou x = 10
# tedy funkci, která se jmenuje "pricti_deset" a 
# která přičte 10 k danému číslu
pricti_deset = tovarna_na_funkce(10)   # pricti_deset je uzávěra (closure)

print(pricti_deset(5))  # vypíše 15  (10 + 5)



# Vytvoříme uzávěru s hodnotou x = 20
pricti_dvacet = tovarna_na_funkce(20)   # pricti_dvacet je uzávěra (closure)
print(pricti_dvacet(5))  # vypíše 25  (20 + 5)

# Vytvoříme uzávěru s hodnotou x = 30 na jeden řádek:
print(tovarna_na_funkce(30)(5))  # vypíše 35  (30 + 5)