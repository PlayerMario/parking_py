from models.vehiculo import Vehiculo


class Cliente:

    # CONSTRUCTOR
    def __init__(self, vehiculo=Vehiculo):
        self.__vehiculo = vehiculo

    # GETTERS & SETTERS
    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    # TOSTRING
    def __str__(self):
        return f"{self.__vehiculo}"
