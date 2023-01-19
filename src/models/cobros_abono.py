import pickle

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
                | ·ENTRADA: {self.fecha_entrada.strftime('%d/%m/%Y, %H:%M')}\t |
                | ·SALIDA: {self.fecha_salida.strftime('%d/%m/%Y, %H:%M')}\t |
                | ·A PAGAR: {self.__cobro}€\t\t\t\t |
                ==================================
                """

    # MÉTODOS DE CLASE:
    def calcular_historico(self, lista_cobros_abonados):
        total = 0
        for cobro in lista_cobros_abonados:
            total += cobro.__cobro
        return total

    def actualizar_listado(self, lista_cobro_abonos):
        lista_cobro_abonos.append(self)
        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'wb')
        pickle.dump(lista_cobro_abonos, f_cobros_abono)
        f_cobros_abono.close()
