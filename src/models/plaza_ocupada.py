from datetime import datetime
from models.cliente import Cliente
import random


class PlazaOcupada:

    # CONSTRUCTOR
    def __init__(self, cliente=Cliente, abonado=False):
        self.__cliente = cliente
        self.__abonado = abonado
        if abonado:
            self.__pin = f"{cliente.vehiculo.matricula}" + f"{self.generar_codigo(1)}"
        else:
            self.__pin = f"{self.generar_codigo(2)}"
        self.__fecha_deposito = datetime.now()
        self.__fecha_salida = None
        self.__coste_final = 0

    # GETTERS & SETTERS
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente=Cliente):
        self.__cliente = cliente

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, abonado):
        self.__abonado = abonado

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, fecha_deposito):
        self.__fecha_deposito = fecha_deposito

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def coste_final(self):
        return self.__coste_final

    @coste_final.setter
    def coste_final(self, coste_final):
        self.__coste_final = coste_final

    # TOSTRING
    def __str__(self):
        return f"""
                -CLIENTE: {self.__cliente}
                -ENTRADA: {self.__fecha_deposito}
                      """

    # MÉTODOS DE CLASE
    def generar_codigo(self, opcion):
        pin = ""
        if opcion == 1:
            for i in range(1, 3):
                pin += str(random.randint(0, 9))
        else:
            for i in range(1, 7):
                pin += str(random.randint(0, 9))

        return pin
