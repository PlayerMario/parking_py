from datetime import datetime


class AdminService:
    def generar_fecha(self):
        try:
            anio = int(input("Indique el año: "))
            mes = int(input("Indique el mes: "))
            dia = int(input("Indique el día: "))
            hora = int(input("Indique la hora: "))
            return datetime(anio, mes, dia, hora)
        except ValueError:
            print("\nError, introduzca un número.")


    def obtener_facturacion(self, fecha1, fecha2, lista_cobros):
        cobros = {}
        for cobro in lista_cobros:
            if fecha1 < cobro.fecha_salida < fecha2:
                cobros[cobro.fecha_salida] = cobro.cobro
        return cobros
