import pickle


class Cobro:

    # CONSTRUCTOR
    def __init__(self, matricula, fecha_entrada, fecha_salida, cobro):
        self.__matricula = matricula
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__cobro = cobro

    # GETTERS & SETTERS
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def cobro(self):
        return self.__cobro

    @cobro.setter
    def cobro(self, cobro):
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

    # MÉTODOS DE CLASE:
    def actualizar_listado(self, lista_cobros):
        lista_cobros.append(self)

        # Actualizar lista
        f_cobros = open('data/lista_cobros.pckl', 'wb')
        pickle.dump(lista_cobros, f_cobros)
        f_cobros.close()

        # Cargar lista
        f_cobros = open('data/lista_cobros.pckl', 'rb')
        cobros = pickle.load(f_cobros)
        f_cobros.close()
        return cobros

    # def obtener_facturacion(self, fecha1, fecha2, lista_cobros):
    #     cobros = {}
    #     for cobro in lista_cobros:
    #         if fecha1 < cobro.__fecha_salida < fecha2:
    #             cobros[cobro.__fecha_salida] = cobro.__cobro
    #     return cobros
    #
    # def mostrar_facturacion(self, cobros):
    #     total = 0
    #     for fecha, cobro in cobros.items():
    #         print(f"\t· {fecha.strftime('%d/%m/%Y, %H:%M')} -> {cobro}€.")
    #         total += cobro
    #     print(f"\t===============================\n\tRecaudado: {total}€\n")
