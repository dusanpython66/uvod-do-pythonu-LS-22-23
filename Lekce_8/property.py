# Path: Lecke_8\property.py

class Person:
    def __init__(self, age):
        self.age = age  # každý může přistupovat k atributu age a měnit ho

class PersonWithAccessors:
    def __init__(self, age):
        self._age = age   # atribut _age je "protected", měl by být používán jen uvnitř třídy

    def get_age(self):       # můžeme přistupovat k atributu age
        return self._age
    
    def set_age(self, age):    # můžeme nastavit atribut age   
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Invalid age")
        
osoba = PersonWithAccessors(39)   # vytvoříme instanci třídy PersonWithAccessors
print(osoba.get_age())            # 39
osoba.set_age(40)                 # nastavíme atribut age
print(osoba.get_age())            # 40

###############################################################################
class PersonPythonic:
    def __init__(self, age):
        self._age = age   # atribut _age je "protected", měl by být používán jen uvnitř třídy

    @property
    def age(self):  # getter  - můžeme přistupovat k atributu age
        return self._age  
    
    @age.setter
    def age(self, age):  # setter  - můžeme nastavit atribut age  
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Invalid age")
        

person = PersonPythonic(39)
print(person.age)  # 39   - můžeme přistupovat k atributu age
person.age = 40    # můžeme nastavit atribut age
print(person.age)  # 40
person.age = 17    # ValueError: Invalid age

"""
Tento kód demonstruje použití dekorátorů @property a @age.setter v třídě 
PersonPythonic. Třída PersonPythonic má atribut _age, který je 
"protected", což znamená, že by měl být používán pouze uvnitř třídy. 
Dekorátory @property a @age.setter nám umožňují získat a nastavit hodnotu 
tohoto atributu zvenčí třídy, ale s kontrolou platnosti hodnoty.

1. Dekorátor @property:
@property je dekorátor, který umožňuje používat metodu jako atribut třídy. 
V tomto kódu je použit dekorátor @property pro metodu age(self), která 
slouží jako "getter" pro atribut _age. Díky tomu lze hodnotu _age získat 
pomocí person.age, aniž bychom museli volat metodu age().

2. Dekorátor @age.setter:
@age.setter je další dekorátor, který se používá k vytvoření 
"setteru" pro atribut. V tomto kódu je použit dekorátor @age.setter pro 
metodu age(self, age), která slouží jako "setter" pro atribut _age. 
Tato metoda umožňuje nastavit hodnotu atributu _age pouze v případě, že 
je v rozmezí 18 až 99 let. 
Pokud hodnota nesplňuje tuto podmínku, je vyvolána výjimka ValueError.
V kódu je dále ukázáno, jak lze vytvořit instanci třídy PersonPythonic s 
věkem 39 a poté přistupovat a měnit hodnotu atributu age. 
Přístup k atributu age je možný pomocí person.age, což vrátí hodnotu 
atributu _age. Nastavení nové hodnoty pro atribut age je možné pomocí 
person.age = 40. Pokud bychom se pokusili nastavit neplatnou hodnotu, například 
person.age = 17, vyvolá se výjimka ValueError.
"""