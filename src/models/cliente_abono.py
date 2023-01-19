from datetime import datetime, timedelta

from models.cliente import Cliente


class ClienteAbono(Cliente):

    # CONSTRUCTOR
    def __init__(self, vehiculo, nombre, apellidos, dni, num_tarjeta, email, abono):
        super().__init__(vehiculo)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__num_tarjeta = num_tarjeta
        self.__email = email
        self.__abono = abono

    # DESTRUCTOR
    def __del__(self):
        # print("Baja realiza con éxito.")
        pass

    # GETTERS & SETTERS
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono

    # TOSTRING
    def __str__(self):
        return f"-{self.__nombre} {self.__apellidos}\n-DNI: {self.__dni}\n{self.vehiculo}"
