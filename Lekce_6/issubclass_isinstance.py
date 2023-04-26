# Title: Funkce issubclass() a isinstance()
# Path: Lekce_6\issubclass_isinstance.py


# nejdrive importujme modul dedicnost.py a z něj
# třídy Auto, ZavodniAuto, F1Auto
import sys  
sys.path.append("../Lekce_5")

from dedicnost import Auto, ZavodniAuto, F1Auto   

oAuto = Auto()
oZavodniAuto = ZavodniAuto()
oF1Auto = F1Auto()

auta = [(oAuto, "auto"), (oZavodniAuto, "závodní auto"), (oF1Auto, "F1 auto")]
tridy_aut = [Auto, ZavodniAuto, F1Auto]

for auto, nazev in auta:
    for trida_ in tridy_aut:  # pro každou třídu v seznamu tridy_aut
        belongs = isinstance(
            auto, trida_
        )  # zjistíme, zda je auto instance třídy trida_
        msg = "je" if belongs else "není"
        print(f"{nazev} {msg} instance třídy {trida_.__name__}")

# Výstup:
# auto je instance třídy Auto
# auto není instance třídy ZavodniAuto
# auto není instance třídy F1Auto
# závodní auto je instance třídy Auto
# závodní auto je instance třídy ZavodniAuto
# závodní auto není instance třídy F1Auto
# F1 auto je instance třídy Auto
# F1 auto je instance třídy ZavodniAuto
# F1 auto je instance třídy F1Auto

# Výstup je stejný, jako v případě předchozího příkladu, ale tentokrát
# používáme funkci isinstance().
# Funkce isinstance() je podobná funkci issubclass(), ale místo toho, aby
# zjistila, zda je třída trida_ přímým potomkem třídy trida, zjistí,
# zda je objekt objekt_ instance třídy trida_.


# Nyní ještě prověříme dědičnost tříd pomocí funkce issubclass()
for trida_1 in tridy_aut:
    for trida_2 in tridy_aut:
        belongs = issubclass(trida_1, trida_2)
        msg = "je" if belongs else "není"
        print(f"{trida_1.__name__} {msg} potomek třídy {trida_2.__name__}")

# Výstup:
# Auto je potomek třídy Auto
# Auto není potomek třídy ZavodniAuto
# Auto není potomek třídy F1Auto
# ZavodniAuto je potomek třídy Auto
# ZavodniAuto je potomek třídy ZavodniAuto
# ZavodniAuto není potomek třídy F1Auto
# F1Auto je potomek třídy Auto
# F1Auto je potomek třídy ZavodniAuto
# F1Auto je potomek třídy F1Auto


# Výstup je stejný, jako v případě předchozího příkladu, ale tentokrát
# používáme funkci issubclass().
# Funkce issubclass() zjistí, zda je třída trida_1 potomkem třídy trida_2.

# __name__ je atribut třídy, který obsahuje název třídy.  V případě
# třídy Auto je to "Auto", v případě třídy ZavodniAuto je to
# "ZavodniAuto" a v případě třídy F1Auto je to "F1Auto".

