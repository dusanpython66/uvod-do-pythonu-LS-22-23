# decorator factory
# q: Význam slova "decorator factory" je, že
# vytváříme dekorátor, který vytváří dekorátor.
# q: Jaký je význam toho, že dekorátor vytváří dekorátor?
# a: Vytvoříme si dekorátor, který bude mít parametr, kterým
# bude maximální povolený výsledek.

from functools import wraps


def max_result(threshold):  # dekorátor factory
    """
       Tato funkce je továrna na dekorátory, která
       přijímá parametr threshold a vytváří dekorátor s tímto limitem.
    """

    def decorator(funkce):  # dekorátor vytváří dekorátor
        @wraps(funkce)  # zachováme název a dokumentaci dekorované funkce
        def wrapper(*args, **kwargs):
            """
            Wrapper funkce je vnitřní funkce, která
            přijímá libovolný počet argumentů a klíčových
            slov, které budou předány dekorované funkci.
            """
            result = funkce(*args, **kwargs)  # zavoláme dekorovanou funkci
            if result > threshold:
                print(f"{result} je moc velký!  Maximálně je povoleno {threshold}.")
                # Pokud je výsledek větší než limit, vypíše se varování.
            return result   # Wrapper vrací výsledek dekorované funkce.

        return wrapper  # dekorátor vrací wrapper funkci

    return decorator   # dekorátor factory vrací dekorátor



@max_result(75)    # dekorátor factory se používá před definicí dekorované funkce, je aplikován jako první
def dekorovanaFunkce(*args, **kwargs):
    """Toto je dekorovaná funkce, 
       která přijímá libovolný počet argumentů a klíčových slov a 
       vrací jejich součet."""
    return sum(args)


# Zavoláme dekorovanou funkci s několika čísly a vypíšeme její výsledek.
print(dekorovanaFunkce(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

# vypíše se:
# 550 je moc velký! Maximálně je povoleno 75.
# 550
