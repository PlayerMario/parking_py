from models.cobros import Cobro


class CobroAbono(Cobro):

    # CONSTRUCTOR
    def __init__(self, matricula, fecha_alta, fecha_baja, cobro, num_tarjeta):
        super().__init__(matricula, fecha_alta, fecha_baja, cobro)
        self.__num_tarjeta = num_tarjeta

    # GETTERS & SETTERS
    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

        # TOSTRING
        def __str__(self):
            return f"""
                    ==================================
                    | ·MATRÍCULA: {self.__matricula}\t\t\t |
                    | ·ENTRADA: {self.__fecha_alta.strftime('%d/%m/%Y, %H:%M')}\t |
                    | ·SALIDA: {self.__fecha_baja.strftime('%d/%m/%Y, %H:%M')}\t |
                    | ·A PAGAR: {self.__cobro}€\t\t\t\t |
                    ==================================
                    """

    # MÉTODOS DE CLASE:
    def calcular_historico(self, lista_cobros_abonados):
        total = 0
        for cobro in lista_cobros_abonados:
            total += cobro.__cobro
        return total