from datetime import datetime

from models.ocupada import Ocupada


class AdminService:
    def cargar_plazas_reservadas_id(self, lista_reservadas):
        plazas_reservadas = []
        for r in lista_reservadas:
            plazas_reservadas.append(r.id_plaza)
        return plazas_reservadas

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

    def elegir_tipo_abono(self, opcion):
        tipo_abono = ""
        if opcion == 1:
            tipo_abono = "Mensual"
        elif opcion == 2:
            tipo_abono = "Trimestral"
        elif opcion == 3:
            tipo_abono = "Semestral"
        elif opcion == 4:
            tipo_abono = "Anual"
        return tipo_abono

    def elegir_tipo_vehiculo(self, opcion):
        tipo_vehiculo = ""
        if opcion == 1:
            tipo_vehiculo = "Turismo"
        elif opcion == 2:
            tipo_vehiculo = "Motocicleta"
        elif opcion == 3:
            tipo_vehiculo = "Movilidad Reducida"
        return tipo_vehiculo

    def reservar_plaza(self, tipo, lista_plazas, reservadas_id, lista_reservadas):
        for plaza in lista_plazas:
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas_id \
                    and plaza.tipo_vehiculo == tipo:
                return plaza, plaza.actualizar_listado_reservadas(lista_reservadas), self.cargar_plazas_reservadas_id(
                    lista_reservadas)
        return None
