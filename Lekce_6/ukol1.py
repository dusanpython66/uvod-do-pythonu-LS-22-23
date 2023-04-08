"""
Úkol (a): Vytvoř třídu Auto

1. Vytvoř třídu Auto s atributy znacka, model a rok_vyroby.
2. Přidej metodu __init__ pro inicializaci atributů.
3. Přidej metodu __str__, která vrátí formátovaný řetězec 
   s informacemi o autě.
"""


class Auto:
    def __init__(self, znacka, model, rok_vyroby):
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby

    def __str__(self):
        return f"{self.znacka} {self.model} ({self.rok_vyroby})"


# oAuto = Auto("Skoda", "Octavia", 2010)
# print(oAuto)


"""
Úkol (b): Vytvoř třídu ElektrickeAuto, která dědí od třídy Auto

1. Vytvoř třídu ElektrickeAuto, která dědí od třídy Auto.
2. Přidej atribut kapacita_baterie pro třídu ElektrickeAuto.
3. Zavolej metodu __init__, aby přijímala i atribut kapacita_baterie.
4. Přidej metodu dojezd, která vypočítá dojezd auta na základě 
kapacity baterie. Dojezd je vypočítán jako kapacita baterie  * 100 km.
"""


class ElektrickeAuto(Auto):
    def __init__(self, znacka, model, rok_vyroby, kapacita_baterie):
        super().__init__(znacka, model, rok_vyroby)
        self.kapacita_baterie = kapacita_baterie

    def dojezd(self):
        return self.kapacita_baterie * 100


oElektrickeAuto = ElektrickeAuto("Tesla", "Model 3", 2019, 75)
print(oElektrickeAuto)
print(oElektrickeAuto.dojezd())
