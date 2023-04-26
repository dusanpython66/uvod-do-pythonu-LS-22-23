# První příklad

class Kniha:
    def __init__(self, nazev, autor, rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani


class EKniha(Kniha):
    def __init__(self, nazev, autor, rok_vydani, format_):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani
        self.format_ = format_


"""
Podívejte se na předchozí kód. Tři vstupní parametry pro třídu Kniha jsou
duplikovány v třídě EKniha. To je docela špatná praxe, protože nyní máme dvě sady
instrukcí, které dělají totéž. Navíc, jakákoli změna v těle metody
Kniha.init() nebude promítnuta v třídě EKniha. Víme, že EKniha je typem knihy (Kniha) a
proto pravděpodobně chceme, aby se změny odrážely i v odvozených třídách.
Podívejme se na jeden způsob, jak tento problém vyřešit:
"""

class Kniha:
    def __init__(self, nazev, autor, rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani

class EKniha(Kniha):
    def __init__(self, nazev, autor, rok_vydani, format_):
        Kniha.__init__(self, nazev, autor, rok_vydani)   # voláme metodu init() třídy Kniha
        self.format_ = format_

oEKniha = EKniha("Python", "Guido van Rossum", 1991, "pdf")
print(oEKniha.nazev)
print(oEKniha.autor)
print(oEKniha.rok_vydani)
print(oEKniha.format_)

"""
Teď je to lepší. Odstranili jsme tu nepříjemnou duplikaci. V podstatě říkáme Pythonu,
aby zavolal metodu init() třídy Kniha; posíláme self do tohoto volání, čímž se ujistíme,
že toto volání navážeme na aktuální instanci.
Pokud změníme logiku v metodě init() třídy Kniha, nemusíme sahat na
EKniha; automaticky se přizpůsobí změně.
Tento přístup je dobrý, ale stále to můžeme udělat o něco lépe. Řekněme, že změníme název
třídy Kniha na Liber, protože jsme se zamilovali do latiny. Potom bychom museli
změnit metodu init() třídy EKniha, aby odrážela tuto změnu. Tomu se můžeme vyhnout
použitím super:
"""

class Kniha:
    def __init__(self, nazev, autor, rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani


class EKniha(Kniha):
    def __init__(self, nazev, autor, rok_vydani, format_):
        super().__init__(nazev, autor, rok_vydani)    # super() je zkratka pro Kniha
        self.format_ = format_


# vytvořme instanci třídy EKniha
oEKniha = EKniha("Python", "Guido van Rossum", 1991, "pdf")
print("-----------------")
print(oEKniha.nazev)
print(oEKniha.autor)
print(oEKniha.rok_vydani)
print(oEKniha.format_)
