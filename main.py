from A.Car import car

Cars = [
        car("Toyota", "Azul", "Quatro", "Mediano"),
        car("Audi", "Negro", "Cinco", "Deportivo")
    ]

car_list = [u.to_dict() for u in car]

data = {"car":car_list, "car":car_list}