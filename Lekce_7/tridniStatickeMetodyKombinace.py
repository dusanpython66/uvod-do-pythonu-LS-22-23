class StringUtil:
    @classmethod
    def is_palindrome(cls, s, case_sensitive=True):
        s = cls._strip_string(s)
        # je-li case_sensitive True, tak nastavíme s na malá písmena (lowercase)
        if not case_sensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_string(s):
        return "".join(c for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


class StringUtil_1:
    @staticmethod
    def is_palindrome(s, case_sensitive=True):
        s = __class__._strip_string(s)
        # je-li case_sensitive True, tak nastavíme s na malá písmena (lowercase)
        if not case_sensitive:
            s = s.lower()
        return __class__._is_palindrome(s)

    @staticmethod
    def _strip_string(s):
        return "".join(c for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
        return True

print(StringUtil_1.is_palindrome("Radar", case_sensitive=False))

print(StringUtil.is_palindrome("Radar", case_sensitive=True))

""" Porovnejte tento kód s předchozí verzí. 
Předně si všimněte, že i když je nyní is_palindrome() třídní 
metodou, voláme ji stejně, jako jsme ji volali, když byla 
statickou metodou. Důvod změny na třídní metodu spočívá v tom, že 
po oddělení některých částí logiky (_strip_string a _is_palindrome) 
potřebujeme k nim získat odkaz. Pokud bychom v naší metodě 
neměli cls, jedinou možností by bylo volat je pomocí jména 
třídy samotné, tedy StringUtil._strip_string(...) a 
StringUtil._is_palindrome(...). To však není dobrá praxe, protože 
bychom v metodě is_palindrome() pevně zakotvili jméno třídy a dostali 
bychom se do situace, kdy bychom ho museli upravit, kdykoliv bychom 
chtěli změnit jméno třídy. Použitím cls bude fungovat jako jméno 
třídy, což znamená, že náš kód nebude potřebovat žádné 
úpravy, pokud se jméno třídy změní.
 """

# Všimněte si, jak se nová logika chápe mnohem lépe než u předchozí verze. 
# Navíc si povšimněte, že pojmenováním vyčleněných metod s počátečním 
# podtržítkem naznačujeme, že tyto metody nejsou určeny k volání zvenčí 
# třídy, ale toto bude předmětem následujícího odstavce o tzv. privátních
# metodách.
