import json;

class car:

    # # # Creador de constructores # # #
    def __init__(self, marca, color, puertas, tamaño):
        self.marca = marca
        self.color = color
        self.puertas = puertas
        self.tamaño = tamaño

    # # # Getters y Setters # # #
    def getMarca(self):
            return self.marca

    def setMarca(self, marca):
            self.marca = marca

    def getColor(self):
            return self.color

    def setColor(self, color):
            self.color = color

    def getPuertas(self):
            return self.puertas

    def setPuertas(self, puertas):
            self.puertas = puertas

    def getTamaño(self):
            return self.tamaño

    def setPuertas(self, puertas):
            self.puertas = puertas

    def to_dict(self):
        return {
            "marca": self.marca,
            "color": self.color,
            "puertas": self.puertas,
            "tamaño": self.tamaño
        }

    def to_dict(self):
        return {
            "marca": self.marca,
            "color": self.color,
            "puertas": self.puertas,
            "tamaño": self.tamaño
        }

    def llamada(self):
        print("La marca és: " + self.marca, + " su color és: " + self.color + "Tiene total de " + self.puertas+ " puertas" + "Té un tamaño de: " )
