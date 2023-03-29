
# význam syntaxe __nazev__ v Pythonu:
# Metody, které začínají a končí dvojitým podtržítkem, jsou tzv. speciální metody.
# Tyto metody jsou volány automaticky v určitých situacích.
# Např. metoda __init__ je volána automaticky při vytváření objektu.
# Metoda __str__ je volána automaticky při zavolání funkce print().

# předvedeme si použití speciální metody __init__ a __str__
class Clovek:
    def __init__(self, sJmeno, sPrijmeni, iVek):
        self.sJmeno = sJmeno   # atribut objektu 
        self.sPrijmeni = sPrijmeni   # atribut objektu
        self.iVek = iVek   # atribut objektu

    def vypisJmeno(self):
        print("Jméno: ", self.sJmeno)

    def vypisPrijmeni(self):
        print("Příjmení: ", self.sPrijmeni)

    def vypisVek(self):
        print("Věk: ", self.iVek)

    def vypisCelkoveJmeno(self):
        print("Celkové jméno: ", self.sJmeno, self.sPrijmeni)

    def __str__(self):
        return "Jméno: " + self.sJmeno + ", Příjmení: " + self.sPrijmeni + ", Věk: " + str(self.iVek)
    
# vytvořme instanci třídy Clovek
oClovek = Clovek("Pepa", "Novák", 25)

# zavolejme metodu __str__
print(oClovek)

# výstup:
# Jméno: Pepa, Příjmení: Novák, Věk: 25
