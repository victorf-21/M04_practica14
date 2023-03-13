import json

class cat:
    def __init__(self, nombre, raza, sexo, color, peso):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.color = color
        self.peso = peso

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getRaza(self):
        return self.raza
    def setRaza(self, raza):
        self.raza = raza

    def getSexo(self):
        return self.sexo
    def setSexo(self, sexo):
        self.sexo = sexo

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso

    def to_dict(self):
        return {
        "nombre": self.nombre,
        "raza": self.raza,
        "sexo": self.sexo,
        "color": self.color,
        "peso": self.peso,
    }

    def llamada(self):
        print("EL gato se llama" + self.nombre + " la raza es" + self.raza + ", su sexo es " + self.sexo + ", su color es" + self.color + " y su peso es " + self.peso)

cats = [
    cat("Michu","callejero","hembra","tricolor","3kg"),
    cat("Anubis","Sphynx","macho","calvo","2,5kg")
]

cats_list = [u.to_dict() for u in cats]

data = {"cats":cats_list}

with open("json_API/cats.json", "w") as file:
    json.dump(data, file)