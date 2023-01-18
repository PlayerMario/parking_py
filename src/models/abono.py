import pickle
from datetime import datetime, timedelta
import random


class Abono:

    # CONSTRUCTOR
    def __init__(self, tipo, plaza):
        self.__tipo = tipo
        self.__pin = self.generar_pin()
        self.__fecha_alta = datetime.now()
        if tipo == "Mensual":
            self.__precio = 25
            self.__fecha_cancelacion = self.__fecha_alta + timedelta(days=30)
        elif tipo == "Trimestral":
            self.__precio = 70
            self.__fecha_cancelacion = self.__fecha_alta + timedelta(days=90)
        elif tipo == "Semestral":
            self.__precio = 130
            self.__fecha_cancelacion = self.__fecha_alta + timedelta(days=180)
        else:
            self.__precio = 200
            self.__fecha_cancelacion = self.__fecha_alta + timedelta(days=365)
        self.__plaza = plaza

    # GETTERS & SETTERS
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, fecha_alta):
        self.__fecha_alta = fecha_alta

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    # TOSTRING
    def __str__(self):
        return f"-Abono {self.__tipo}\n-{self.__precio}€\n-Alta: {self.__fecha_alta.strftime('%d/%m/%Y, %H:%M')}\n" \
               f"-Fin: {self.__fecha_cancelacion.strftime('%d/%m/%Y, %H:%M')}\n-Plaza: {self.__plaza.id_plaza}\n"

    # MÉTODOS DE CLASE
    def generar_pin(self):
        pin = ""
        for i in range(1, 7):
            pin += str(random.randint(0, 9))
        return pin

    # def renovar_abono(self, abono, tipo):
    #     pin_antiguo = abono.__pin
    #     nuevo_abono = Abono(tipo, abono.__plaza)
    #     nuevo_abono.pin = pin_antiguo
    #     return nuevo_abono

    def actualizar_listado(self, lista_abonos):
        lista_abonos.append(self)

        # Actualizar lista
        f_abonos = open('data/lista_abonos.pckl', 'wb')
        pickle.dump(lista_abonos, f_abonos)
        f_abonos.close()

        # Cargar lista
        f_abonos = open('data/lista_abonos.pckl', 'rb')
        abonos = pickle.load(f_abonos)
        f_abonos.close()
        return abonos
