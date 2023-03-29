# vytvořme nejjednodušší třídu jejíž jméno je MojePrvniTrida
class MojePrvniTrida:
    pass    # třída je prázdná  - nic nedělá

# vytvořme instanci třídy MojePrvniTrida
oMojePrvniTrida = MojePrvniTrida()

# vytvořme třídu s konstruktorem
class MojeDruhaTrida:
    def __init__(self):
        print("Vytvořena instance třídy MojeDruhaTrida")

# vytvořme instanci třídy MojeDruhaTrida
oMojeDruhaTrida = MojeDruhaTrida()

# vytvořme třídu s konstruktorem a parametrem
class MojeTretiTrida:
    def __init__(self, sJmeno):    # konstruktor s parametrem
        self.sJmeno = sJmeno  # uložíme parametr do atributu objektu
        print("Vytvořena instance třídy MojeTretiTrida s parametrem: ", sJmeno)

# vytvořme instanci třídy MojeTretiTrida
oMojeTretiTrida = MojeTretiTrida("Pepa")

# zobrazme parametr sJmeno objektu oMojeTretiTrida
print(oMojeTretiTrida.sJmeno)


# vytvořme třídu s konstruktorem, parametry a atributy
# třída bude reprezentovat člověka a bude mít různé metody
class Clovek:
    def __init__(self, sJmeno, sPrijmeni, iVek):
        self.sJmeno = sJmeno
        self.sPrijmeni = sPrijmeni
        self.iVek = iVek

    def vypisJmeno(self):
        print("Jméno: ", self.sJmeno)

    def vypisPrijmeni(self):
        print("Příjmení: ", self.sPrijmeni)

    def vypisVek(self):
        print("Věk: ", self.iVek)

    def vypisCelkoveJmeno(self):
        print("Celkové jméno: ", self.sJmeno, self.sPrijmeni)

# vytvořme instanci třídy Clovek
oClovek = Clovek("Pepa", "Novák", 25)

# zobrazme atributy objektu oClovek
print(oClovek.sJmeno)
print(oClovek.sPrijmeni)
print(oClovek.iVek)

# zavolejme metody objektu oClovek
oClovek.vypisJmeno()
oClovek.vypisPrijmeni()
oClovek.vypisVek()
oClovek.vypisCelkoveJmeno()





