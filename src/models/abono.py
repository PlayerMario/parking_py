from datetime import datetime, timedelta


class Abono:

    # CONSTRUCTOR
    def __init__(self, tipo):
        self.__tipo = tipo
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

    # GETTERS & SETTERS
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

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

    # TOSTRING
    def __str__(self):
        return f"""
                \t\t-TIPO: {self.__tipo}
                \t\t-PRECIO: {self.__precio}€
                \t\t-FECHA ALTA: {self.__fecha_alta.strftime('%d/%m/%Y, %H:%M')}                
                \t\t-FECHA FIN: {self.__fecha_cancelacion.strftime('%d/%m/%Y, %H:%M')} 
                      """
