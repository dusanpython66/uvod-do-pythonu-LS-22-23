# Začněme s definicí prazdné třídy bez atributů a metod.

class NejjednodussiTrida:
    pass

# Vytvořme instanci třídy NejjednodussiTrida.
oNejjednodussiTrida = NejjednodussiTrida()


# Zobrazme typ objektu oNejjednodussiTrida.
print(type(oNejjednodussiTrida))

# přidejme objektu oNejjednodussiTrida atribut s názvem "jmeno" a hodnotou "Pepa".
oNejjednodussiTrida.jmeno = "Pepa"

# přidejme objektu oNejjednodussiTrida atribut s názvem "prijmeni" a hodnotou "Novak".
oNejjednodussiTrida.prijmeni = "Novák"

print(oNejjednodussiTrida.jmeno + " " + oNejjednodussiTrida.prijmeni)

# smažme atribut prijmeni z objektu oNejjednodussiTrida.
del oNejjednodussiTrida.prijmeni

# Zobrazme atributy objektu oNejjednodussiTrida.
print(oNejjednodussiTrida.__dict__)

# Vytvořme nový objekt oNejjednodussiTrida2.
oNejjednodussiTrida2 = NejjednodussiTrida()
print(oNejjednodussiTrida2.__dict__)

# Napišme definici třídy s konstruktorem (metoda __init__).
class TridaSKonstruktorem:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

# Vytvořme instanci třídy TridaSKonstruktorem.
oTridaSKonstruktorem = TridaSKonstruktorem("Pepa", "Novák")

# Vytvořme další instanci třídy TridaSKonstruktorem.
oTridaSKonstruktorem2 = TridaSKonstruktorem("Jana", "Nováková")

# Zobrazme atributy objektu oTridaSKonstruktorem.
print(oTridaSKonstruktorem.__dict__)

oTridaSKonstruktorem2.prijmeni = "Horáková"
print(oTridaSKonstruktorem2.__dict__)


