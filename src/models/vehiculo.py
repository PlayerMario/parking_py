import pickle


class Vehiculo:

    # CONSTRUCTOR
    def __init__(self, matricula, tipo):
        self.__matricula = matricula
        self.__tipo = tipo

    # GETTERS & SETTERS
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    # TOSTRING
    def __str__(self):
        return f"-Matrícula: {self.__matricula}\n-Tipo: {self.__tipo}"

    # # MÉTODOS DE CLASE
    # def actualizar_listado(self, lista_vehiculos):
    #     if self is not None:
    #         lista_vehiculos.append(self)
    #
    #     # Actualizar lista
    #     f_vehiculos = open('data/lista_vehiculos.pckl', 'wb')
    #     pickle.dump(lista_vehiculos, f_vehiculos)
    #     f_vehiculos.close()
    #
    #     # Cargar lista
    #     f_vehiculos = open('data/lista_vehiculos.pckl', 'rb')
    #     vehiculos = pickle.load(f_vehiculos)
    #     f_vehiculos.close()
    #
    #     return vehiculos

