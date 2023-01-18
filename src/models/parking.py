from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada
from models.plaza import Plaza


class Parking:

    # CONSTRUCTOR
    def __init__(self, num_plazas):
        self.__num_plazas = num_plazas
        #self.__plazas = self.inicializar_parking()
        # self.__clientes = None
        # self.__reservadas = None
        # self.__cobros = None
        # self.__cobros_abonos = None

    # GETTERS & SETTERS
    @property
    def num_plaza(self):
        return self.__num_plazas

    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plazas = num_plaza
        #0self.__plazas = self.inicializar_parking()

    # @property
    # def plazas(self):
    #     return self.__plazas
    #
    # @plazas.setter
    # def plazas(self, plazas):
    #     self.__plazas = plazas
    #
    # @property
    # def clientes(self):
    #     return self.__clientes
    #
    # @clientes.setter
    # def clientes(self, clientes):
    #     self.__clientes = clientes
    #
    # @property
    # def reservadas(self):
    #     return self.__reservadas
    #
    # @reservadas.setter
    # def reservadas(self, reservadas):
    #     self.__reservadas = reservadas
    #
    # @property
    # def cobros(self):
    #     return self.__cobros
    #
    # @cobros.setter
    # def cobros(self, cobros):
    #     self.__cobros = cobros
    #
    # @property
    # def cobros_abonos(self):
    #     return self.__cobros_abonos
    #
    # @cobros_abonos.setter
    # def cobros_abonos(self, cobros_abonos):
    #     self.__cobros_abonos = cobros_abonos

    # TOSTRING
    def __str__(self):
        return f"""-PLAZAS: {self.__num_plazas}"""

    # MÉTODOS DE CLASE
    # def inicializar_parking(self):
    #     plazas = []
    #     for i in range(1, self.__num_plazas + 1):
    #         if i <= round(self.__num_plazas * 0.7):
    #             plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Turismo", ocupada=Ocupada))
    #         elif i <= round(self.__num_plazas * 0.85):
    #             plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Motocicleta", ocupada=Ocupada))
    #         else:
    #             plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Movilidad Reducida", ocupada=Ocupada))
    #     return plazas

    # def mostrar_libres(self, lista_reservadas):
    #     num_turismo = 0
    #     num_moto = 0
    #     num_mov_red = 0
    #     for plaza in self.__plazas:
    #         if not isinstance(plaza.ocupada, Ocupada) and plaza not in lista_reservadas:
    #             if plaza.tipo_vehiculo == "Turismo":
    #                 num_turismo += 1
    #             elif plaza.tipo_vehiculo == "Motocicleta":
    #                 num_moto += 1
    #             else:
    #                 num_mov_red += 1
    #     return num_turismo, num_moto, num_mov_red
    #
    # def mostrar_info_plazas(self, lista_reservadas):
    #     print(f"""\t\t\t\tPLAZAS DISPONIBLES:
    #             ==========================
    #             -TURISMOS: {self.mostrar_libres(lista_reservadas)[0]}
    #             -MOTOCICLETAS: {self.mostrar_libres(lista_reservadas)[1]}
    #             -MOVILIDAD REDUCIDA: {self.mostrar_libres(lista_reservadas)[2]}""")

    # def depositar_ocasional(self, cliente, tipo_vehiculo, lista_reservadas):
    #     salir = False
    #     cont = 0
    #     while not salir and cont != len(self.__plazas):
    #         plaza = self.__plazas[cont]
    #         if not isinstance(plaza.ocupada, Ocupada) and plaza not in lista_reservadas:
    #             if plaza.tipo_vehiculo == tipo_vehiculo:
    #                 plaza.ocupada = Ocupada(cliente)
    #                 salir = True
    #                 return plaza
    #         cont += 1
    #
    # def mostrar_ticket(self, plaza):
    #     if isinstance(plaza.ocupada, Ocupada):
    #         print(f"""
    #                 ==================================
    #                 | ·PLAZA: {plaza.id_plaza}\t\t\t\t\t\t |
    #                 | ·MATRÍCULA: {plaza.ocupada.cliente.vehiculo.matricula}\t\t\t |
    #                 | ·ENTRADA: {plaza.ocupada.fecha_deposito.strftime('%d/%m/%Y, %H:%M')}\t |
    #                 | ·PIN: {plaza.ocupada.pin}\t\t\t\t\t |
    #                 ==================================
    #                 """)
    #     else:
    #         print(f"La operación no ha podido completarse.")

    # def buscar_plaza(self, matricula, id_plaza, pin):
    #     salir = False
    #     cont = 0
    #
    #     while not salir and cont != len(self.__plazas):
    #         plaza = self.__plazas[cont]
    #         if isinstance(plaza.ocupada, Ocupada):
    #             if plaza.id_plaza == id_plaza and plaza.ocupada.pin == pin and \
    #                     plaza.ocupada.cliente.vehiculo.matricula == matricula:
    #                 return plaza
    #         cont += 1

    # def depositar_abonado(self, cliente):
    #     if isinstance(cliente, ClienteAbono):
    #         salir = False
    #         cont = 0
    #         while not salir and cont != len(self.__plazas):
    #             plaza = self.__plazas[cont]
    #             if not isinstance(plaza.ocupada, Ocupada):
    #                 if plaza.id_plaza == cliente.abono.plaza.id_plaza:
    #                     plaza.ocupada = Ocupada(cliente)
    #                     salir = True
    #                     return plaza
    #             cont += 1

    # def estado_parking(self, lista_reservadas):
    #     for plaza in self.__plazas:
    #         if isinstance(plaza.ocupada, Ocupada):
    #             if isinstance(plaza.ocupada.cliente, ClienteAbono):
    #                 print("\n=============================\n\t\tCLIENTE ABONADO\n=============================")
    #                 print(plaza)
    #             else:
    #                 print("\n=============================\n\t\tCLIENTE NO ABONADO\n=============================")
    #                 print(plaza)
    #         elif plaza in lista_reservadas:
    #             print("\n=============================\n\t\tPLAZA RESERVADA\n=============================")
    #             print(plaza)
    #         else:
    #             print("\n=============================\n\t\tPLAZA LIBRE\n=============================")
    #             print(plaza)

    def reservar_plaza(self, tipo, lista_reservadas):
        for plaza in self.__plazas:
            if not isinstance(plaza.ocupada, Ocupada) and plaza not in lista_reservadas and plaza.tipo_vehiculo == tipo:
                return plaza
        return None
