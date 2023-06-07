""" 
Polymorfismus je základní koncept v objektově orientovaném programování(OOP), 
který umožňuje objektům různých tříd mít stejné rozhraní a být tak použity stejným způsobem. 
V kontextu programovacího jazyka Python se polymorfismus vyskytuje ve dvou hlavních formách: 
duck typing a dědičnost.

"""

# Duck typing
"""
Duck typing je způsob, jakým Python zpracovává objekty, pokud se snažíme zavolat metodu,
která v objektu neexistuje. Python se nesnaží zjistit, zda objekt je určitého typu,
ale zda má požadované metody. Pokud ano, pak je objekt považován za vhodný.
"""

"""
V praxi to znamená, že funkce nebo metoda může pracovat s různými objekty, pokud 
tyto objekty implementují očekávané metody nebo atributy.

Příklad duck typingu:
"""
def plocha_utvaru(utvar):
    return utvar.plocha()

class Kruh:
    def __init__(self, polomer):
        self.polomer = polomer

    def plocha(self):
        return 3.14 * (self.polomer ** 2)

class Ctverec:
    def __init__(self, strana):
        self.strana = strana

    def plocha(self):
        return self.strana * self.strana

kruh = Kruh(5)
ctverec = Ctverec(4)

print(plocha_utvaru(kruh))  # Vypíše plochu kruhu
print(plocha_utvaru(ctverec))  # Vypíše plochu čtverce


# Dědičnost
"""
Polymorfismus pomocí dědičnosti využívá vztah mezi základními a odvozenými třídami. 
Odvozená třída může přepsat nebo rozšířit metody a atributy základní třídy, což 
umožňuje vytvářet různé implementace stejného rozhraní.

Příklad polymorfismu pomocí dědičnosti:
"""
class Utvar:
    def plocha(self):
        pass

class Kruh(Utvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def plocha(self):
        return 3.14 * (self.polomer ** 2)

class Ctverec(Utvar):
    def __init__(self, strana):
        self.strana = strana

    def plocha(self):
        return self.strana * self.strana

def plocha_utvaru(utvar):
    return utvar.plocha()

kruh = Kruh(5)
ctverec = Ctverec(4)

print(plocha_utvaru(kruh))  # Vypíše plochu kruhu
print(plocha_utvaru(ctverec))  # Vypíše plocu čtverce




