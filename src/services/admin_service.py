from datetime import datetime

from models.abono import Abono
from models.cliente_abono import ClienteAbono
from models.cobros_abono import CobroAbono
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

    def buscar_cliente_dni(self, dni, lista_clientes):
        # for cliente in listado_clientes:
        #     if isinstance(cliente, ClienteAbono):
        #         if cliente.dni == dni:
        #             return cliente
        # return None

        for i in range(len(lista_clientes)):
            if isinstance(lista_clientes[i], ClienteAbono) and lista_clientes[i].dni == dni:
                return lista_clientes[i], i
        return None

    def actualizar_plaza_ocupada(self, lista_plazas, cliente):
        for plaza in lista_plazas:
            if isinstance(plaza.ocupada, Ocupada) and isinstance(plaza.ocupada.cliente, ClienteAbono) and \
                    plaza.ocupada.cliente.dni == cliente.dni:
                plaza.ocupada.cliente = cliente
                return plaza.actualizar_listado(lista_plazas)
        return None

    def modificar_cliente(self, cliente, opcion, lista_clientes, indice, lista_plazas):
        if opcion == 1:
            lista_clientes[indice].nombre = input("Indique su nombre: ")
            return cliente, cliente.actualizar_listado(lista_clientes), self.actualizar_plaza_ocupada(lista_plazas,
                                                                                                      cliente)
        elif opcion == 2:
            lista_clientes[indice].apellidos = input("Indique sus apellidos: ")
            return cliente, cliente.actualizar_listado(lista_clientes), self.actualizar_plaza_ocupada(lista_plazas,
                                                                                                      cliente)
        elif opcion == 3:
            lista_clientes[indice].num_tarjeta = input("Indique su número de cuenta: ")
            return cliente, cliente.actualizar_listado(lista_clientes), self.actualizar_plaza_ocupada(lista_plazas,
                                                                                                      cliente)
        elif opcion == 4:
            lista_clientes[indice].email = input("Indique su email: ")
            return cliente, cliente.actualizar_listado(lista_clientes), self.actualizar_plaza_ocupada(lista_plazas,
                                                                                                      cliente)
        else:
            return None

    def renovar_abono(self, cliente, tipo, lista_clientes, lista_abonos, lista_cobros_abono):
        # Crear nuevo abono
        nuevo_abono = Abono(tipo, cliente.abono.plaza)
        nuevo_abono.pin = cliente.abono.pin

        # Setearlo al cliente
        cliente.abono = nuevo_abono

        # Constatar nuevo abono en los cobros de abonados
        cobro_abono = CobroAbono(cliente.vehiculo.matricula, nuevo_abono.fecha_alta, nuevo_abono.fecha_cancelacion,
                                 nuevo_abono.precio, cliente.num_tarjeta)

        return cliente, nuevo_abono, nuevo_abono.actualizar_listado(lista_abonos), cliente.actualizar_listado(
            lista_clientes), cobro_abono.actualizar_listado(lista_cobros_abono)

    def baja_abono(self, cliente, lista_clientes, lista_abonos, lista_plazas, reservadas_id, lista_reservadas):
        cliente.abono.plaza.ocupada = None
        # lista_reservadas.remove(cliente.abono.plaza)
        plazas_act = cliente.abono.plaza.actualizar_listado(lista_plazas)
        reservadas_id.remove(cliente.abono.plaza.id_plaza)
        #lista_abonos.remove(cliente.abono)
        reservadas_act = cliente.abono.plaza.actualizar_listado_reservadas(lista_reservadas)
        abonos_act = cliente.abono.actualizar_listado(lista_abonos)
        cliente.abono.plaza = None
        lista_clientes.remove(cliente)
        clientes_act = cliente.actualizar_listado(lista_clientes)
        cliente.__del__()
        return plazas_act, abonos_act, clientes_act, reservadas_act

    def baja(self, cliente, lista_abonos, lista_plazas):
        plaza = cliente.abono.plaza
        ocupada = plaza.ocupada
        abono = cliente.abono
        if isinstance(ocupada, Ocupada):
            plaza.ocupada = None
            plazas_act = plaza.actualizar_listado(lista_plazas)
            ocupada.__del__()
        abono.plaza = None
        abonos_act = abono.actualizar_listado(lista_abonos)
        abono.__del__()


