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
        return f"""
                -PLAZAS: {self.__num_plazas}
                -ENTRADA: {self.__plazas}
                      """

    # MÉTODOS DE CLASE
    def inicializar_parking(self):
        plazas = []
        for i in range(1, self.__num_plazas + 1):
            if i <= round(self.__num_plazas * 0.7):
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Turismo"))
            elif i <= round(self.__num_plazas * 0.85):
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Motocicleta"))
            else:
                plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Movilidad Reducida"))
        return plazas
