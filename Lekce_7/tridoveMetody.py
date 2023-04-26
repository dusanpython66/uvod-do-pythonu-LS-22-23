# Path: Lekce_7\tridoveMetody.py
# ukažme si použití tzv. třídních metod
# (metod, které jsou společné pro všechny instance dané třídy)


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(
        cls, xy
    ):  # třídní metoda  - vytvoří instanci třídy z tuple  cls je třída, která je právě vytvářena
        return cls(xy[0], xy[1])


b = Bod.from_tuple((1, 2))  # vytvoření instance pomocí třídní metody
print(b.x, b.y)  # 1 2


"""
Třídní metody jsou speciální typ metod, které přijímají objekt třídy 
jako svůj první argument, na rozdíl od instančních metod, které přijímají 
objekt instance. Třídní metody umožňují definovat alternativní způsoby 
vytváření instancí třídy, což se někdy označuje jako "tovární metody" 
nebo "factory methods".

Podrobněji si můžeme popsat třídní metody následovně:

První argument: Třídní metoda přijímá objekt třídy jako svůj první argument. 
Tento argument se obvykle označuje jako "cls" (zkráceně z "class") namísto "self", 
který se používá pro instanční metody. "cls" je odkaz na samotnou třídu, nikoli 
na konkrétní instanci třídy.

Dekorátor @classmethod: Pro definování třídní metody v Pythonu je třeba 
použít dekorátor "@classmethod" před definicí metody. 
Dekorátor informuje interpret Pythonu, že metoda je třídní metoda, a ne 
instanční nebo statická metoda.

Tovární metody: Jeden z běžných případů použití třídních metod je 
poskytnutí alternativních způsobů vytváření instancí třídy. 
To může být užitečné, pokud chceme vytvářet instance třídy s různými 
konfiguracemi nebo počátečními hodnotami.

Příklad třídní metody v Pythonu:
"""


class Auto:
    def __init__(self, pocet_dveri):
        self.pocet_dveri = pocet_dveri

    @classmethod
    def sedan(cls):
        return cls(pocet_dveri=4)

    @classmethod
    def hatchback(cls):
        return cls(pocet_dveri=5)


# Vytvoření instancí třídy Auto pomocí třídních metod
auto1 = Auto.sedan()
auto2 = Auto.hatchback()
print(auto1.pocet_dveri)  # Výstup: 4


"""
V tomto příkladě máme třídu "Auto" s atributem "pocet_dveri". 
Vytvořili jsme dvě třídní metody, "sedan" a "hatchback", které nám 
umožňují vytvářet instance třídy Auto s předdefinovaným počtem dveří. 
Tímto způsobem můžeme snadno vytvářet instance třídy Auto bez nutnosti 
explicitně zadávat počet dveří při vytváření nových instancí.

Pokračujeme v příkladu:
"""

auto3 = Auto(3)  # Vytvoření instance třídy Auto pomocí konstruktoru __init__
print(auto3.__class__.)
print(auto1.pocet_dveri)  # Výstup: 4
print(auto2.pocet_dveri)  # Výstup: 5
print(auto3.pocet_dveri)  # Výstup: 3


"""
Zde vidíme, jak jsme vytvořili další instanci třídy Auto, tentokrát 
přímo pomocí konstruktoru __init__, který vyžaduje explicitní zadání 
počtu dveří. Poté jsme vypsali počet dveří u všech tří instancí, které 
jsme vytvořili.
Třídní metody jsou flexibilní, protože umožňují třídám poskytovat 
různé způsoby vytváření instancí na základě různých parametrů nebo konfigurací. 
Tímto způsobem můžeme snadno rozšířit naši třídu o další metody, které 
poskytují různé způsoby vytváření instancí bez nutnosti měnit 
samotnou implementaci třídy.

Shrnutí:

-Třídní metody v Pythonu přijímají objekt třídy jako svůj 
první argument a používají dekorátor "@classmethod".

-Třídní metody se liší od instančních a statických metod, protože 
pracují s objektem třídy, nikoli s objektem instance.

-Běžným případem použití třídních metod je poskytnutí 
alternativních způsobů vytváření instancí třídy, někdy 
nazývaných "tovární metody" nebo "factory methods".
"""

