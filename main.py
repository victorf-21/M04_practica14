#Hecho por Victor
from B import cat as ct

c1 = ct.cat("Michu","callejero","hembra","tricolor","3kg")
c1.llamada()

from B import cat as ca
c2 = ca.cat("Anubis","Sphynx","macho","calvo","2,5kg")
c2.llamada()

cats_list = [u.to_dict() for u in cats]

data = {"cats":cats_list}

with open("json_API/cats.json", "w") as file:
    json.dump(data, file)

#Hecho por Albert (falta coses)
from A.Car import car

Cars = [
        car("Toyota", "Azul", "Quatro", "Mediano"),
        car("Audi", "Negro", "Cinco", "Deportivo")
    ]

car_list = [u.to_dict() for u in car]

data = {"car":car_list, "car":car_list}
