import pickle
import random

from models.ocupada import Ocupada


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
        if isinstance(self.__ocupada, Ocupada):
            return f"\t\t Plaza {self.__id_plaza}\n=============================\n-{self.__tipo_vehiculo}\n" \
                   f"-{self.__precio_mins}€/min\n=============================\n{self.__ocupada}\n" \
                   f"=============================\n"
        else:
            return f"\t\t Plaza {self.__id_plaza}\n=============================\n-{self.__tipo_vehiculo}\n" \
                   f"-{self.__precio_mins}€/min\n=============================\n"

    # MÉTODOS DE CLASE
    def actualizar_listado(self, lista_plazas):
        lista_plazas.append(self)

        # Actualizar lista
        f_plazas = open('data/lista_plazas.pckl', 'wb')
        pickle.dump(lista_plazas, f_plazas)
        f_plazas.close()

        # Cargar lista
        f_plazas = open('data/lista_plazas.pckl', 'rb')
        plazas = pickle.load(f_plazas)
        f_plazas.close()
        return plazas