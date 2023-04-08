# Dědičnost znamená, že se vytvoří nová třída,
#  která bude mít všechny vlastnosti
#  a metody z předka (třídy, ze které dědí)
#  a může mít i vlastní vlastnosti a metody
#  a může je přepsat


# Třída Motor  (třída, ze které se dědí)
# - atributy a metody, které mají všechny motory
class Motor:
    def start(self):
        pass

    def stop(self):
        pass


class ElektroMotor(Motor):    # ElektroMotor dědí všechny vlastnosti od Motor
    pass


class BenzinMotor(Motor):    # BenzinMotor dědí všechny vlastnosti od Motor
    pass


# Třída Auto  (třída, ze které se dědí)   
# - atributy a metody, které mají všechny auta
# Každá instance třídy Auto má vlastní instanci třídy Motor!
class Auto:
    motor_cls = Motor  # třída motoru  (defaultně Motor)

    def __init__(self):   # konstruktor třídy Auto  
        self.motor = self.motor_cls()  # vytvoříme instanci motoru  

    def start(self):
        print(
            "Startuje motor {0} pro auto {1}".format(
                self.motor.__class__.__name__, self.__class__.__name__
            )
        )
        self.motor.start()  # zavoláme metodu start() motoru na instanci motoru

    def stop(self):
        self.motor.stop()  # zavoláme metodu stop() motoru  na instanci motoru


class ZavodniAuto(Auto): # ZavodniAuto dědí všechny vlastnosti od Auto
    motor_cls = ElektroMotor  # třída motoru 

class MestoAuto(Auto):    # MestoAuto dědí všechny vlastnosti od Auto
    motor_cls = BenzinMotor  # třída motoru 

class F1Auto(ZavodniAuto):
    pass  # F1Auto dědí všechny vlastnosti od ZavodniAuto, motor_cls = ElektroMotor

# díky tranzitivitě dědičnosti F1Auto dědí jednak z třídy ZavodniAuto, tak i z třídy Auto

# Vytvoříme objekty:
oAuto = Auto()
oZavodniAuto = ZavodniAuto()
oMestoAuto = MestoAuto()
oF1Auto = F1Auto()
auta = [oAuto, oZavodniAuto, oMestoAuto, oF1Auto]

for auto in auta:   # pro každé auto v seznamu auta
    auto.start()    # zavoláme metodu start() na instanci auto
    auto.stop()     # zavoláme metodu stop() na instanci auto
    print()         # vypíšeme prázdný řádek


