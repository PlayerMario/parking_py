from datetime import datetime, timedelta
from models.cliente_abono import ClienteAbono
import random
from models.cobros import Cobro


class Ocupada:
    __fecha_salida = ""
    __coste_final = 0

    # CONSTRUCTOR
    def __init__(self, cliente):
        self.__cliente = cliente
        if isinstance(self.__cliente, ClienteAbono):
            self.__pin = self.__cliente.abono.pin
        else:
            self.__pin = f"{self.generar_pin()}"
        self.__fecha_deposito = datetime.now()

    # DESTRUCTOR
    def __del__(self):
        pass

    # GETTERS & SETTERS
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

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
        if isinstance(self.__cliente, ClienteAbono):
            self.__coste_final = 0
        else:
            self.__coste_final = self.calcular_precio()

    @property
    def coste_final(self):
        return self.__coste_final

    @coste_final.setter
    def coste_final(self, coste_final):
        self.__coste_final = coste_final

    # TOSTRING
    def __str__(self):
        return f"{self.__cliente}\n-Pin: {self.__pin}\n-Entrada: {self.__fecha_deposito.strftime('%d/%m/%Y, %H:%M')}"

    # MÉTODOS DE CLASE
    def generar_pin(self):
        pin = ""
        for i in range(1, 7):
            pin += str(random.randint(0, 9))
        return pin

    def calcular_precio(self):
        if self.__cliente.vehiculo.tipo == "Turismo":
            precio_mins = 0.12
        elif self.__cliente.vehiculo.tipo == "Motocicleta":
            precio_mins = 0.08
        else:
            precio_mins = 0.1

        return round(((self.__fecha_salida - self.__fecha_deposito).total_seconds() / 60) * precio_mins, 2)
