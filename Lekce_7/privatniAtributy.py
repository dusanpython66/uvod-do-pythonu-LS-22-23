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

print(obj.__dict__)   # {'_A__factor': 100, '_B__factor': 200}   

# Všimněte si, že výsledkem je slovník, který obsahuje dva klíče.

# V Pythonu se privátní proměnné vytváří pomocí dvojitého podtržítka
# na začátku názvu proměnné. Výsledkem je, že Python přejmenuje
# proměnnou tak, aby obsahovala i název třídy. Tento proces se nazývá
# name mangling (přejmenování názvů). Výsledkem je, že se vytvoří
# privátní proměnná, která je přístupná pouze uvnitř třídy a jejích
# metod.

# Pojďme nyní okomentovat přímo kód, kde jsme použili privátní proměnnou
# __faktor:

"""
V tomto kódu je třída A s privátním atributem __factor, který je 
nastaven v konstruktoru __init__. Třída A má také metodu op1, která 
vypisuje hodnotu atributu __factor. Třída B je potomkem třídy A a 
má vlastní metodu op2, která se pokouší nastavit a vypsat hodnotu 
atributu __factor.
Vzhledem k tomu, že atribut __factor v třídě A je privátní, Python 
použije "name mangling" pro změnu jeho názvu, aby se zabránilo 
přímému přístupu z potomkových tříd (child class) nebo vnějšího kódu. 
V našem případě se název proměnné __factor změní na _A__factor 
(přidává se název třídy s jedním podtržítkem před dvojitým podtržítkem).
Když vytvoříme objekt třídy B s hodnotou factor 100, konstruktor 
třídy A (tedy metoda __init__) nastaví privátní atribut _A__factor 
na 100. Metoda op1 pracuje s tímto atributem, proto vypisuje 
"Op1 with factor 100...".
Když voláme metodu op2 s hodnotou factor 200, metoda se pokouší 
nastavit privátní atribut __factor třídy A. 
Avšak kvůli "name mangling" se ve skutečnosti vytvoří nový 
atribut _B__factor v třídě B, který je nastaven na hodnotu 200. 
Metoda op2 vypisuje "Op2 with factor 200...", protože pracuje s 
atributem _B__factor.
Nakonec, když znovu zavoláme metodu op1, stále pracuje s 
původním privátním atributem _A__factor, jehož hodnota je 
stále 100. Proto výstup zní "Op1 with factor 100...".
Výsledkem je, že privátní atribut __factor třídy A je chráněn 
před nechtěným přístupem a změnou, a to i přesto, že 
třída B se pokouší tento atribut změnit. Tímto 
způsobem kód demonstruje koncept zapouzdření a použití 
privátních atributů v Pythonu.
"""



"""
V programovacím jazyce Python se privátní proměnné používají k 
omezení přístupu k určitým datům nebo funkcím uvnitř třídy, což je 
základní princip  tzv. zapouzdření (encapsulation). Zapouzdření je 
důležitý koncept 
objektově orientovaného programování, který zajišťuje, že interní 
stav objektu a jeho implementační detaily jsou chráněny a 
skryty před vnějším přístupem.
V Pythonu neexistuje přísné vynucení privátnosti proměnných, jako je 
tomu v některých jiných programovacích jazycích. Místo toho 
Python používá konvenci pojmenování k označení privátních proměnných. 
Proměnná se považuje za privátní, pokud je její název začíná 
podtržítkem (např. _private_variable). Dvojitá podtržítka na 
začátku názvu proměnné (např. __private_variable) způsobí, že 
Python provede tzv. "name mangling", který změní název proměnné 
tak, aby byl méně přístupný z vnějšího kódu.
Je důležité poznamenat, že i když tato konvence chrání 
proměnné před nechtěným přístupem, stále je možné je 
přistupovat přímo. Python tedy spoléhá na "gentleman's 
agreement" mezi programátory, kteří by měli respektovat tuto 
konvenci a nezasahovat do privátních proměnných ostatních tříd.
"""

