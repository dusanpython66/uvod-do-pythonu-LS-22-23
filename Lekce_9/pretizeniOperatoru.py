""" Přetížení operátorů v Pythonu
Jako příklad vytvořme třídu, která uchovává řetězec a
vyhodnocuje se na True, pokud je '42' součástí tohoto řetězce,
a na False v opačném případě.  Též dejme třídě vlastnost délky,
která odpovídá délce uchovávaného řetězce: """


class Weird:
    def __init__(self, s):
        self._s = s

    def __len__(self):
        return len(self._s)

    def __bool__(self):
        return '42' in self._s


weird = Weird('Hello! I am 42 years old!')
print(len(weird))
print(bool(weird))


"""Operator overloading je koncept v programovacích jazycích, 
jako je Python, který umožňuje třídám měnit chování základních 
operátorů, jako jsou sčítání, odčítání, násobení, dělení a další. To znamená, že můžete definovat, jak mají operátory fungovat pro objekty vašich vlastních tříd, což umožňuje intuitivnější interakci s objekty a zlepšuje čitelnost kódu.
V Pythonu můžete provést operator overloading pomocí speciálních 
metod (také nazývaných "magic methods" nebo "dunder methods" 
kvůli jejich jménům obsahujícím dvojitá podtržítka). 
Tyto metody mají předdefinovaná jména a syntaxi, která 
začíná a končí dvojitým podtržítkem, například __add__ pro 
sčítání.
Představme si, že máme třídu Vector, která reprezentuje 
vektor ve 2D prostoru. Chceme, aby se objekty třídy Vector 
mohly sčítat pomocí základního operátoru +. 
Můžeme to provést pomocí operator overloadingu následovně:"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # v3 bude nový objekt Vector s hodnotami (4, 6)
print(v3.x, v3.y)