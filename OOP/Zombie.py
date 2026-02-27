from Enemigo import *

class Zombie:
    def __init__(self, tipo, puntos_energia, ataque):
        self.tipo = tipo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.tipo
    def habla(self):
            print("Hummm.....")

    def propagar_enfermedades(self):
            print("El Zombie esta tratando de propagar la enfermedad!!")
