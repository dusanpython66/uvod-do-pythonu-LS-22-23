# vytvořme dvě třídy, které budou dědit od třídy Clovek
# třída Student bude mít atribut iRocnik a metodu vypisRocnik
# třída Ucitel bude mít atribut sPredmet a metodu vypisPredmet

# vytvořme třídu člověk
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

# vytvořme třídu student
class Student(Clovek):     # třída Student dědí od třídy Clovek
    def __init__(self, sJmeno, sPrijmeni, iVek, iRocnik):
        super().__init__(sJmeno, sPrijmeni, iVek)   # voláme konstruktor třídy Clovek
        self.iRocnik = iRocnik

    def vypisRocnik(self):
        print("Ročník: ", self.iRocnik)

# vytvořme třídu učitel
class Ucitel(Clovek):    # třída Ucitel dědí od třídy Clovek
    def __init__(self, sJmeno, sPrijmeni, iVek, sPredmet):
        super().__init__(sJmeno, sPrijmeni, iVek)   # voláme konstruktor třídy Clovek
        self.sPredmet = sPredmet

    def vypisPredmet(self):
        print("Předmět: ", self.sPredmet)

# vytvořme instanci třídy Student
oStudent = Student("Pepa", "Novák", 25, 2)

# zobrazme atributy objektu oStudent
print(oStudent.sJmeno)
print(oStudent.sPrijmeni)
print(oStudent.iVek)
print(oStudent.iRocnik)

# zavolejme metody objektu oStudent
oStudent.vypisJmeno()
oStudent.vypisPrijmeni()
oStudent.vypisVek()
oStudent.vypisCelkoveJmeno()
oStudent.vypisRocnik()

# vytvořme instanci třídy Ucitel
oUcitel = Ucitel("Pepa", "Novák", 25, "Matematika")

# zobrazme atributy objektu oUcitel
print(oUcitel.sJmeno)
print(oUcitel.sPrijmeni)
print(oUcitel.iVek)
print(oUcitel.sPredmet)

# zavolejme metody objektu oUcitel
oUcitel.vypisJmeno()
oUcitel.vypisPrijmeni()
oUcitel.vypisVek()
oUcitel.vypisCelkoveJmeno()
oUcitel.vypisPredmet()

