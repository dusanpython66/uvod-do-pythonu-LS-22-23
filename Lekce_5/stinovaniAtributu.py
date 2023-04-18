# Ukažme si tzv. stínování atributu (shadowing).
# Stínování atributu je to, kdy se vytvoří atribut objektu
# se stejným názvem jako třídový atribut.
# V takovém případě se při přístupu k atributu objektu
# použije atribut objektu a třídový atribut se při přístupu
# k němu ignoruje.
















class Bod:
    x = 10
    y = 7

p = Bod()
print(p.x, p.y) # 10 7

# Vytvoříme si atribut objektu se stejným názvem jako třídový atribut
p.x = 5   # objekt p tak získá vlastní atribut x
print("Atribut x vázaný na instanci p je roven: ", p.x) # 5
print("Třídový atribut x = ", Bod.x) # 10 třída Bod si svůj atribut x ponechává nezměněný!


# Nyní smažme atribut objektu p.x
del p.x
print("Atribut x vázaný na instanci p je roven: ", p.x) # 10  třída Bod použije svůj atribut x

# Vytvořme objektu nový atribut p.z
p.z = 3
print("Atribut z vázaný na instanci p je roven: ", p.z) # 3
print("Třídový atribut z = ", Bod.z) # AttributeError: type object 'Bod' has no attribute 'z'



