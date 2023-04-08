# Ukažme definici třídy s argumentem self:
class Square:
    strana = 8
    def obsah(self):   # self je argument, který je vždy předán
        return self.strana * self.strana
    def obvod(self):
        return self.strana * 4
    
# Vytvoříme objekt:
ctverec = Square()
# Zavoláme metodu .obsah():
print(ctverec.obsah())

# metodu .obsah() lze také zavolat pomocí názvu třídy:
print(Square.obsah(ctverec))   # musíme předat objekt jako argument


# Zavoláme metodu obvod:
print(ctverec.obvod())
# nebo také pomocí názvu třídy:
print(Square.obvod(ctverec))   # musíme předat objekt jako argument

ctverec.strana = 10  # změníme hodnotu atributu strana
print(ctverec.obsah())   # zavoláme metodu obsah() znovu


# Ukažme ještě jeden šikovný příklad:
class Cena:
    def konecna_cena(self, dph, sleva=0):
        """Tato metoda vrací konečnou cenu po zdanění a slevě."""
        return (self.cenovka * (1 + dph)) - sleva
    
# Vytvoříme objekt:
cena = Cena()
cena.cenovka = 100
print(cena.konecna_cena(0.20, 10))   # zavoláme metodu s argumenty
# nebo také takto:
print(Cena.konecna_cena(cena, 0.20, 10))   # musíme předat objekt jako argument


