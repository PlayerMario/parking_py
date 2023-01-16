class Cobro:

    # CONSTRUCTOR
    def __init__(self, matricula, fecha_entrada, fecha_salida, cobro):
        self.__matricula = matricula
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__cobro = cobro

    # TOSTRING
    def __str__(self):
        return f"""
                ==================================
                | ·MATRÍCULA: {self.__matricula}\t\t\t |
                | ·ENTRADA: {self.__fecha_entrada.strftime('%d/%m/%Y, %H:%M')}\t |
                | ·SALIDA: {self.__fecha_salida.strftime('%d/%m/%Y, %H:%M')}\t |
                | ·A PAGAR: {self.__cobro}€\t\t\t\t |
                ==================================
                """
