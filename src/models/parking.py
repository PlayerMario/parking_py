from models.ocupada import Ocupada
from models.plaza import Plaza


class Parking:

    # CONSTRUCTOR
    def __init__(self, num_plazas):
        self.__num_plazas = num_plazas
        self.__plazas = self.inicializar_parking()

    # GETTERS & SETTERS
    @property
    def num_plaza(self):
        return self.__num_plazas

    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plazas = num_plaza
        self.__plazas = self.inicializar_parking()

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    # TOSTRING
    def __str__(self):
        return f"""-PLAZAS: {self.__num_plazas}"""

    # MÉTODOS DE CLASE
    def inicializar_parking(self):
        plazas = []
        for i in range(1, self.__num_plazas + 1):
            if i <= round(self.__num_plazas * 0.7):
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Turismo", ocupada=Ocupada))
            elif i <= round(self.__num_plazas * 0.85):
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Motocicleta", ocupada=Ocupada))
            else:
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Movilidad Reducida", ocupada=Ocupada))
        return plazas

    def mostrar_libres(self):
        num_turismo = 0
        num_moto = 0
        num_mov_red = 0
        for plaza in self.__plazas:
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == "Turismo":
                    num_turismo += 1
                elif plaza.tipo_vehiculo == "Motocicleta":
                    num_moto += 1
                else:
                    num_mov_red += 1
        return num_turismo, num_moto, num_mov_red

    def mostrar_info_plazas(self):
        print(f"""\t\t\t\tPLAZAS DISPONIBLES:
                ==========================
                -TURISMOS: {self.mostrar_libres()[0]}
                -MOTOCICLETAS: {self.mostrar_libres()[1]}
                -MOVILIDAD REDUCIDA: {self.mostrar_libres()[2]}""")

    def depositar_ocasional(self, cliente, tipo_vehiculo):
        for plaza in self.__plazas:
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == tipo_vehiculo:
                    plaza.ocupada = Ocupada(cliente)
                    print(plaza)

        salir = False
        cont = 0

        while not salir:
            plaza = self.__plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada):
                plaza.ocupada = Ocupada(cliente)
                # MOSTRAR TICKET, LLAMAR A MÉTODO TICKET

