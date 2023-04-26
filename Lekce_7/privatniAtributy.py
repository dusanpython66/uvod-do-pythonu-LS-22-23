class A:
    def __init__(self, factor):
        self._factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))

class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor {}...'.format(self._factor))

obj = B(100)
obj.op1()  # Op1 with factor 100...
obj.op2(200)  # Op2 with factor 200...
obj.op1()  # Op1 with factor 200... <<<< toto je nechtěné chování

# Přepišme třídu B tak, aby se při volání metody op2() nezměnil atribut _factor

class A:
    def __init__(self, factor):
        self.__factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))

obj = B(100)
obj.op1()  # Op1 with factor 100...
obj.op2(200)  # Op2 with factor 200...
obj.op1()  # Op1 with factor 100... <<<< toto je chování, které chceme!!!

print(obj.__dict__)  # dict_keys(['_A__factor', '_B__factor'])           