# Decorator cached_property je implementován v modulu 
# functools a funguje tak, že při prvním volání metody (nebo funkce) 
# označené tímto dekorátorem se její výsledek uloží do 
# mezipaměti (cache) a při dalších voláních se místo opětovného 
# výpočtu vrátí již uložený výsledek. 
# Tímto způsobem se šetří čas a výpočetní prostředky.
# Použití cached_property je jednoduché. Zde je příklad:

from functools import cached_property

class MyClass:
    def __init__(self, value):
        self._value = value

    @cached_property
    def expensive_operation(self):
        print("Provádím nákladnou operaci...")
        return self._value ** 2

obj = MyClass(5)
print(obj.expensive_operation)  # Provádím nákladnou operaci... 25
print(obj.expensive_operation)  # 25 (tentokrát se operace neprovádí)


