from datetime import datetime, timedelta
from models.cliente_abono import ClienteAbono
import random


class Ocupada:

    # CONSTRUCTOR
    def __init__(self, cliente):
        self.__cliente = cliente
        if isinstance(self.__cliente, ClienteAbono):
            self.__pin = f"{self.__cliente.vehiculo.matricula}-" + f"{self.generar_pin(1)}"
        else:
            self.__pin = f"{self.generar_pin(2)}"
        self.__fecha_deposito = datetime.now()
        self.__fecha_salida = datetime.now() + timedelta(days=1)
        if isinstance(self.__cliente, ClienteAbono):
            self.__coste_final = 0
        else:
            self.__coste_final = self.calcular_precio()

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

    @property
    def coste_final(self):
        return self.__coste_final

    @coste_final.setter
    def coste_final(self, coste_final):
        self.__coste_final = coste_final

    # TOSTRING
    def __str__(self):
        return f"""-CLIENTE: {self.__cliente}
                -PIN: {self.__pin}
                -ENTRADA: {self.__fecha_deposito.strftime('%d/%m/%Y, %H:%M')}
                -SALIDA: {self.__fecha_salida.strftime('%d/%m/%Y, %H:%M')}
                -COSTE: {self.__coste_final}€"""

    # MÉTODOS DE CLASE
    def generar_pin(self, opcion):
        pin = ""
        if opcion == 1:
            for i in range(1, 3):
                pin += str(random.randint(0, 9))
        else:
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
