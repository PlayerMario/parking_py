import pickle

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

    # MÉTODOS DE CLASE
    def actualizar_listado(self, lista_clientes):
        lista_clientes.append(self)
        f_clientes = open('data/lista_clientes.pckl', 'wb')
        pickle.dump(lista_clientes, f_clientes)
        f_clientes.close()
        #
        # # Cargar lista
        # f_clientes = open('data/lista_clientes.pckl', 'rb')
        # clientes = pickle.load(f_clientes)
        # f_clientes.close()
        #
        # return clientes
