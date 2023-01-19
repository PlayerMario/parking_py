from datetime import datetime, timedelta
from models.abono import Abono
from models.cliente_abono import ClienteAbono
from models.cobros_abono import CobroAbono
from models.ocupada import Ocupada
from views.parking_views import ParkingViews

parking_view = ParkingViews()


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

    def reservar_plaza(self, tipo, lista_plazas, reservadas_id):
        for plaza in lista_plazas:
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas_id \
                    and plaza.tipo_vehiculo == tipo:
                reservadas_id.append(plaza.id_plaza)
                return plaza
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

    def renovar_abono(self, cliente, tipo, lista_clientes, lista_cobros_abono):
        # Crear nuevo abono
        nuevo_abono = Abono(tipo, cliente.abono.plaza)
        nuevo_abono.pin = cliente.abono.pin

        # Setearlo al cliente
        cliente.abono = nuevo_abono

        # Constatar nuevo abono en los cobros de abonados
        cobro_abono = CobroAbono(cliente.vehiculo.matricula, nuevo_abono.fecha_alta, nuevo_abono.fecha_cancelacion,
                                 nuevo_abono.precio, cliente.num_tarjeta)

        return cliente, nuevo_abono, cliente.actualizar_listado(lista_clientes), \
            cobro_abono.actualizar_listado(lista_cobros_abono)

    def buscar_plaza_id(self, lista_plazas, plaza):
        for i in range(len(lista_plazas)):
            if lista_plazas[i].id_plaza == plaza.id_plaza:
                return i
        return None

    def baja_abonado(self, cliente, lista_clientes, lista_plazas, lista_reservadas_id):
        # Cargar datos
        plaza = cliente.abono.plaza
        plaza_antigua = plaza
        ocupada = plaza.ocupada
        abono = cliente.abono

        # Si la plaza está ocupada, desocuparla y borrar la instancia de ocupada
        if isinstance(ocupada, Ocupada):
            plaza.ocupada = None
            ocupada.__del__()

        # Actualizar lista de IDs de plazas reservadas para abonados
        lista_reservadas_id.remove(plaza.id_plaza)

        # Actualizar la plaza de la lista para que no esté ocupada si lo estuviera
        id = self.buscar_plaza_id(lista_plazas, plaza_antigua)
        if id is not None:
            lista_plazas[id] = plaza
            # LLAMAR A ACTUALIZAR PICKLE

        # Quitar el abono al cliente, y del abono, la plaza asociada
        cliente.abono = None
        abono.plaza = None

        # Sacar al cliente de la lista
        lista_clientes.remove(cliente)
        # LLAMAR A ACTUALIZAR PICKLE

        # Eliminar abono y cliente
        abono.__del__()
        cliente.__del__()

    def buscar_clientes_cad(self, mes, listado_clientes, opcion):
        clientes_cad = []
        for cliente in listado_clientes:
            if isinstance(cliente, ClienteAbono):
                if opcion == 1:
                    if cliente.abono.fecha_cancelacion.month == mes:
                        clientes_cad.append(cliente)
                elif opcion == 2:
                    if datetime.now() < cliente.abono.fecha_cancelacion < (datetime.now() + timedelta(days=10)):
                        clientes_cad.append(cliente)
        return clientes_cad
