import random


class Plaza:

    # CONSTRUCTOR
    def __init__(self, id_plaza, tipo_vehiculo, ocupada):
        self.__id_plaza = id_plaza
        self.__tipo_vehiculo = tipo_vehiculo
        if tipo_vehiculo == "Turismo":
            self.__precio_mins = 0.12
        elif tipo_vehiculo == "Motocicleta":
            self.__precio_mins = 0.08
        else:
            self.__precio_mins = 0.1
        self.__ocupada = ocupada

    # GETTERS & SETTERS
    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo

    @property
    def precio_mins(self):
        return self.__precio_mins

    @precio_mins.setter
    def precio_mins(self, precio_mins):
        self.__precio_mins = precio_mins

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    # TOSTRING
    def __str__(self):
        return f"""\t\t\t\tPLAZA {self.__id_plaza}:
        ==========================
        -TIPO: {self.__tipo_vehiculo}
        -PRECIO/MIN: {self.__precio_mins}€/min
        ==========================
        -OCUPADA: {self.__ocupada}
              """
