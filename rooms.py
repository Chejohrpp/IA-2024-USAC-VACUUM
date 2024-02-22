class Types_Room:
    A = "Cuarto A"
    B = "Cuarto B"

class States_Room:
    CLEAN = "Habitación limpia"
    DIRTY = "Habitación sucia"

class Room:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def to_string(self):
        return (f"{self.name} : {self.state}")


def get_list_of_rooms():
    # Lista para almacenar las instancias de la clase Room
    lista_habitaciones = []

    # Iteramos sobre cada atributo de la clase Types_Room
    for name, value in Types_Room.__dict__.items():
        # Filtramos solo los atributos que no empiezan con '__' para evitar los atributos especiales
        if not name.startswith("__"):
            # Creamos una nueva instancia de la clase Room con el nombre y el estado específicos
            nueva_habitacion = Room(value, States_Room.CLEAN)
            # Añadimos la instancia a la lista
            lista_habitaciones.append(nueva_habitacion)
    return lista_habitaciones

# # Imprimimos la lista de habitaciones
# for habitacion in lista_habitaciones:
#     print(f"Habitación: {habitacion.name}, Estado: {habitacion.state}")
