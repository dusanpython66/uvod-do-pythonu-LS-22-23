class StringUtil:
    @staticmethod
    def is_palindrome(s, case_sensitive=True):
        # TODO: Implementujte funkci, která zjistí, zda je řetězec s palindrom.
        #  Funkce bude ignorovat mezery a interpunkci.
        #  Parametr case_sensitive určuje, zda se má zohlednit i velikost písmen.
        #  Pokud je case_sensitive=False, tak se před porovnáním převede na malá písmena.
        s = "".join(c for c in s if c.isalnum())  # odstranění interpunkce  a mezer
        if not case_sensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


print(StringUtil.is_palindrome("Radar", case_sensitive=False))

print(StringUtil.is_palindrome("Radar", case_sensitive=True))

print(
    StringUtil.get_unique_words(
        "Tohle je věta, která obsahuje několik slov, která se opakují."
    )
)  # {'se', 'která', 'je', 'Tohle', 'věta,', 'několik', 'slov,', 'obsahuje', 'opakují.'}

