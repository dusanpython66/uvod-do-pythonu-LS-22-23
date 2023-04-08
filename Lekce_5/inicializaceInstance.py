# Jako ukázku použití inicializace instance
# Vytvoříme třídu s konstruktorem

class Obdelnik:
    def __init__(self, stranaA, stranaB):  # konstruktor
        self.stranaA = stranaA
        self.stranaB = stranaB
    def obsah(self):
        return self.stranaA * self.stranaB
    def obvod(self):
        return 2 * (self.stranaA + self.stranaB)
    
# Vytvoříme objekt:
oObdelnik = Obdelnik(10, 5)

# Zobrazíme hodnoty atributů:
print(f"Strana A: {oObdelnik.stranaA}")
print(f"Strana B: {oObdelnik.stranaB}")

# Zavoláme metody:
print(f"Obsah: {oObdelnik.obsah()}")
print(f"Obvod: {oObdelnik.obvod()}")