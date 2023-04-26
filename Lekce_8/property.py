# Path: Lecke_8\property.py

class Person:
    def __init__(self, age):
        self.age = age  # každý může přistupovat k atributu age a měnit ho

class PersonWithAccessors:
    def __init__(self, age):
        self._age = age   # atribut _age je "protected", měl by být používán jen uvnitř třídy

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Invalid age")

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