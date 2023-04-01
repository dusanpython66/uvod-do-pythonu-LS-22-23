from time import time, sleep


def f():
    sleep(0.3)


def g():
    sleep(0.5)


t = time()  # zjistíme aktuální čas
f()  # zavoláme funkci f
print("f took", time() - t)  # zjistíme, kolik času trvalo zavolání funkce f


# dekorátor je funkce, která přijímá funkci jako argument a vrací funkci
# dekorátor se používá pro rozšíření funkcionalit existující funkce
# dekorátor se používá pro přidání nové funkcionality k existující funkci
# ukažme si jednoduchý dekorátor

# dekorátor
def dekorator(funkce):
    def vnitrek():
        print("Začátek funkce")
        funkce()
        print("Konec funkce")

    return vnitrek  # vracíme funkci vnitrek


# q: co se stane, když vracíme funkci vnitrek()?
# a: vracíme ji jako hodnotu, ne jako volání funkce
#   tedy vracíme objekt funkce, nikoliv její výsledek
# q: co je smyslem vracet funkci vnitrek()?
# a: vracíme ji jako hodnotu, ne jako volání funkce
# q: lze napsat dekorátor bez vnitřní funkce vnitrek()?
# a: ano, lze, ale pak se dekorátor používá jinak
#   viz. https://www.python.org/dev/peps/pep-0318/

# dekorovaná funkce
@dekorator
def dekorovana_funkce():
    print("Toto je dekorovaná funkce")


# zavolejme dekorovanou funkci
dekorovana_funkce()


########### syntaxe bez použití znaku @ ###########

# importujme funkce sleep a time z modulu time
from time import sleep, time

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
from time import sleep, time


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
from time import sleep, time

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
