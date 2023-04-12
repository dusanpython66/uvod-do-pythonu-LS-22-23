# Ukažme si příklad třídy s třídovými atributy.
# Význam třídových atributů je v tom, že jsou 
# sdílené všemi instancemi třídy.
# Třídové atributy jsou přístupné přes objekt třídy.


















class Osoba:
    # Třídový atribut.
    # Třídové atributy jsou sdílené všemi instancemi třídy.
    druh = "člověk"

    def __init__(self, jmeno, prijmeni):
        # Atribut objektu.
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        

# Vytvořme instanci třídy Osoba.
oOsoba = Osoba("Pepa", "Novák")

# Zobrazme atributy objektu oOsoba.
print(oOsoba.__dict__)

# Zobrazme třídový atribut druh.
print(oOsoba.druh)   # objekt oOsoba použije svůj atribut druh
print(Osoba.druh)  # třída Osoba použije svůj atribut druh

# vytvořme další instanci třídy Osoba
oOsoba2 = Osoba("Jana", "Nováková")

# Zobrazme atributy objektu oOsoba2.
print(oOsoba2.__dict__)

# Zobrazme třídový atribut druh.
print(oOsoba2.druh)   # objekt oOsoba2 použije svůj atribut druh

