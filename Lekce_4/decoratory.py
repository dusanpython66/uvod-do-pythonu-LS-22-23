from time import sleep, time  # importujeme funkce time a sleep z modulu time


def f():
    sleep(0.3)


def g():
    sleep(0.5)


t = time()  # zjistíme aktuální čas

f()  # zavoláme funkci f
print("f zavolání trvalo: ", time() - t, "sekundy")  # zjistíme, kolik času trvalo zavolání funkce f

t = time()  # zjistíme aktuální čas

g()  # zavoláme funkci g
print("g zavolání trvalo: ", time() - t, "sekundy")  # zjistíme, kolik času trvalo zavolání funkce g

# výše uvedený kód lze zjednodušit pomocí dekorátorů:

def mira(funkce):
    cas = time()
    funkce()
    print(funkce.__name__, "zavolání trvalo: ", time() - cas, "sekundy")
    # funkce.__name__ je jméno funkce  (funkce je objekt, který má atribut __name__)
mira(f)


# dekorátor je funkce, která přijímá funkci jako argument a vrací funkci
# dekorátor se používá pro rozšíření funkcionalit existující funkce
# dekorátor se používá pro přidání nové funkcionality k existující funkci
# ukažme si jednoduchý dekorátor

# dekorátor


def dekorator(funkce):
    def wrapper():
        print("Začátek funkce")
        funkce()
        print("Konec funkce")

    return wrapper  # vracíme funkci wrapper



# dekorovaná funkce
@dekorator
def dekorovana_funkce():
    print("Toto je dekorovaná funkce")


# zavolejme dekorovanou funkci
dekorovana_funkce()

# Tedy funkce dekorovana_funkce() byla "obalena" funkcí wrapper(),
# což je typické chování dekorátorů. Dekorátor je v podstatě funkce, která
# "obaluje" jinou funkci a může tak ovlivňovat její chování.


########### syntaxe bez použití znaku @ ###########

# importujme funkce sleep a time z modulu time
# from time import sleep, time

# napišme definici dekorované funkce
def f(sleep_time=0.1):
    sleep(sleep_time)


# napišme definici dekorátoru
def dekorator(funkce):
    def wrapper(*args, **kwargs):
        t = time()
        funkce(*args, **kwargs)
        print("funkce", funkce.__name__, "took", time() - t)

    return wrapper


# dekorujeme funkci f
f = dekorator(f)

# zavolejme dekorovanou funkci
f(0.2)
f(sleep_time=0.3)  # použijeme pojmenovaný argument
print("f.__name__:", f.__name__)  # vypíše se wrapper!


########### syntaxe s použitím znaku @ ###########
########### jeden dekorátor ###########

# importujme funkce sleep a time z modulu time
# from time import sleep, time


# dekorujeme funkci f
@dekorator  # dekorátor se používá před definicí dekorované funkce
def f(sleep_time=0.1):
    sleep(sleep_time)


# napišme definici dekorátoru
def dekorator(funkce):
    def wrapper(*args, **kwargs):
        t = time()
        funkce(*args, **kwargs)
        print("funkce", funkce.__name__, "took", time() - t)

    return wrapper


# zavolejme dekorovanou funkci
f(0.2)
f(sleep_time=0.3)  # použijeme pojmenovaný argument
print("f.__name__:", f.__name__)  # vypíše se wrapper!


########### syntaxe s použitím znaku @ ###########
########### více dekorátorů ###########

# importujme funkce sleep a time z modulu time
# from time import sleep, time

# napišme definice dekorátorů
def dekorator1(funkce):
    def wrapper(*args, **kwargs):
        t = time()
        funkce(*args, **kwargs)
        print("funkce", funkce.__name__, "took", time() - t)

    return wrapper


def dekorator2(funkce):
    def wrapper(*args, **kwargs):
        print("funkce", funkce.__name__, "was called")
        funkce(*args, **kwargs)

    return wrapper


@dekorator1  # dekorátor se používá před definicí dekorované funkce, je aplikován jako poslední
@dekorator2  # dekorátor se používá před definicí dekorované funkce, je aplikován jako první
def f(sleep_time=0.1):
    sleep(sleep_time)


# zavolejme dekorovanou funkci
f(0.2)
f(sleep_time=0.3)  # použijeme pojmenovaný argument
print("f.__name__:", f.__name__)  # vypíše se wrapper!


########### syntaxe s použitím znaku @ ###########

# importujme funkce sleep a time z modulu time
from time import sleep, time
from functools import wraps  # importujeme funkci wraps  z modulu functools


def measure(funkce):  # dekorátor measure
    @wraps(
        funkce
    )  # použijeme funkci wraps, která zajišťuje, že se zachová název a dokumentace dekorované funkce
    def wrapper(*args, **kwargs):  # vnitřní funkce wrapper
        t = time()
        vysledek = funkce(*args, **kwargs)
        print(
            "funkce", funkce.__name__, "took", time() - t
        )  # vypíše se název dekorované funkce
        return vysledek

    return wrapper


def max_result(funkce):
    @wraps(
        funkce
    )  # použijeme funkci wraps, která zajišťuje, že se zachová název a dokumentace dekorované funkce
    def wrapper(*args, **kwargs):
        vysledek = funkce(*args, **kwargs)
        if vysledek > 100:
            print(f"Výsledek {vysledek} je větší než 100. 'Maximum je 100.'")
        return vysledek

    return wrapper


@measure
@max_result
def cube(n):
    """Vrátí třetí mocninu čísla n."""
    return n**3


print(cube(2))
print(cube(5))
print(cube.__name__, cube.__doc__)  # vypíše se název dekorované funkce
# q: __doc__ je atribut funkce, který 
# obsahuje dokumentaci funkce


