# Title: Funkce issubclass() a isinstance()
# Path: Lekce_6\issubclass_isinstance.py


# nejdrive importujme modul dedicnost.py a z něj
# třídy Auto, ZavodniAuto, F1Auto
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


# Path: Lekce_6\issubclass_isinstance.py

