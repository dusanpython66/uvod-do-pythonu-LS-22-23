# Ukažme příklad na základě třídy Kniha,
# ukazující násobnou dědičnost:

class Kniha:
    def __init__(self, nazev, autor, rok):
        self.nazev = nazev
        self.autor = autor
        self.rok = rok

    """  def __str__(self):   # metoda __str__ se volá při převodu objektu na řetězec   
        return "%s, %s, %s" % (self.nazev, self.autor, self.rok)    # vrací řetězec  "nazev, autor, rok"
     """

class Knihovna:
    def __init__(self, nazevKnihovny, adresaKnihovny):
        self.nazevKnihovny = nazevKnihovny
        self.knihy = []
        self.adresaKnihovny = adresaKnihovny

    def pridej(self, kniha):
        self.knihy.append(kniha)

    def __str__(self):   # metoda __str__ se volá při převodu objektu na řetězec   
        return "%s" % (self.knihy) 
    

class KnihovnaKniha(Kniha, Knihovna):
    def __init__(self, nazev, autor, rok, nazevKnihovny, adresaKnihovny):
        Kniha.__init__(self, nazev, autor, rok)
        Knihovna.__init__(self, nazevKnihovny, adresaKnihovny)
        self.pridej(self)

    """  def __str__(self):  
        return "%s, %s, %s, %s" % (self.nazev, self.autor, self.rok, self.nazevKnihovny)
    
    """
# vytvořme několik knih a knihoven:
oKniha = Kniha("Python", "Guido van Rossum", 1991)
oKnihovna = Knihovna("Knihovna", "HK")   # vytvoříme knihovnu s názvem "Knihovna"

# vytvoříme knihovnu s názvem "Knihovna" a přidáme do ní knihu "Python":
oKnihovnaPython = KnihovnaKniha("Python", "Guido van Rossum", 1991, "Knihovna", "HK")
print(oKnihovnaPython)  # vypíše: Python, Guido van Rossum, 1991, Knihovna

# vytvoříme knihovnu s názvem "Knihovna" a přidáme do ní knihu "Perl":
oKnihovnaPerl = KnihovnaKniha("Perl", "Larry Wall", 1987, "Knihovna", "HK")
print(oKnihovnaPerl)  # vypíše: Perl, Larry Wall, 1987, Knihovna

# zobrazíme všechny knihy v knihovně:
print(oKnihovna)  # vypíše: Knihovna: [Python, Perl]

# Metoda __mro__ vrací tuple, který obsahuje všechny rodiče třídy:
# 1. rodič je třída, která je v prvním řádku v definici třídy
# 2. rodič je třída, která je v druhém řádku v definici třídy
# ... atd.

print(oKnihovnaPython.__class__.__mro__)   # vypíše: (<class '__main__.KnihovnaKniha'>, <class '__main__.Kniha'>, <class '__main__.Knihovna'>, <class 'object'>)

print(KnihovnaKniha.__mro__)   # vypíše: (<class '__main__.KnihovnaKniha'>, <class '__main__.Kniha'>, <class '__main__.Knihovna'>, <class 'object'>)

