# Ukažme příklad na základě třídy Kniha,
# ukazující násobnou dědičnost:

class Kniha:
    def __init__(self, nazev, autor, rok):
        self.nazev = nazev
        self.autor = autor
        self.rok = rok

    def __str__(self):
        return "%s, %s, %s" % (self.nazev, self.autor, self.rok)
    

class Knihovna:
    def __init__(self, nazev):
        self.nazev = nazev
        self.knihy = []

    def pridej(self, kniha):
        self.knihy.append(kniha)

    def __str__(self):
        return "%s: %s" % (self.nazev, self.knihy)
    

class KnihovnaKniha(Kniha, Knihovna):
    def __init__(self, nazev, autor, rok, knihovna):
        Kniha.__init__(self, nazev, autor, rok)
        Knihovna.__init__(self, knihovna)
        self.pridej(self)

    def __str__(self):  
        return "%s, %s, %s, %s" % (self.nazev, self.autor, self.rok, self.knihovna)
    

# vytvořme několik knih a knihoven:
oKniha = Kniha("Python", "Guido van Rossum", 1991)
oKnihovna = Knihovna("Knihovna")   # vytvoříme knihovnu s názvem "Knihovna"

# vytvoříme knihovnu s názvem "Knihovna" a přidáme do ní knihu "Python":
oKnihovnaPython = KnihovnaKniha("Python", "Guido van Rossum", 1991, "Knihovna")
# vytvoříme knihovnu s názvem "Knihovna" a přidáme do ní knihu "Perl":
oKnihovnaPerl = KnihovnaKniha("Perl", "Larry Wall", 1987, "Knihovna")

# zobrazíme všechny knihy v knihovně:
print(oKnihovna)  # vypíše: Knihovna: [Python, Perl]



