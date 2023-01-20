from datetime import datetime
from models.cliente_abono import ClienteAbono
from models.cobros import Cobro
from models.ocupada import Ocupada
from models.plaza import Plaza
from views.parking_views import ParkingViews

parking_views = ParkingViews()


class ClienteService:
    def mostrar_libres(self, lista_plazas, reservadas):
        num_turismo = 0
        num_moto = 0
        num_mov_red = 0
        for plaza in lista_plazas:
            # Si la plaza no está ocupada ni reservada, comprueba el tipo y suma la cantidad disponible para mostrarla
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas:
                if plaza.tipo_vehiculo == "Turismo":
                    num_turismo += 1
                elif plaza.tipo_vehiculo == "Motocicleta":
                    num_moto += 1
                else:
                    num_mov_red += 1
        return num_turismo, num_moto, num_mov_red, parking_views.mostrar_disponibles(num_turismo, num_moto, num_mov_red)

    def devolver_tipo(self, opTipo, lista_plazas, reservadas):
        # Comprueba que quedan plazas disponibles del tipo que se ha indicado para poder depositar el vehículo, si no
        # devuelve un tipo vacío para mostrar que no hay libres del tipo
        if opTipo == 1 and self.mostrar_libres(lista_plazas, reservadas)[0] != 0:
            tipo_vehiculo = "Turismo"
        elif opTipo == 2 and self.mostrar_libres(lista_plazas, reservadas)[1] != 0:
            tipo_vehiculo = "Motocicleta"
        elif opTipo == 3 and self.mostrar_libres(lista_plazas, reservadas)[2] != 0:
            tipo_vehiculo = "Movilidad Reducida"
        else:
            tipo_vehiculo = ""
        return tipo_vehiculo

    def depositar_ocasional(self, lista_plazas, cliente, reservadas):
        cont = 0
        while cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            # Si la plaza no está ocupada ni reservada, y su tipo coincide con el tipo de vehículo del cliente,
            # actualiza el estado ocupado de la plaza por el cliente que se indica, y la lista de plazas, y retorna
            # la plaza
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas \
                    and plaza.tipo_vehiculo == cliente.vehiculo.tipo:
                plaza.ocupada = Ocupada(cliente)
                plaza.actualizar_listado(lista_plazas)
                return plaza
            cont += 1
        return None

    def buscar_plaza(self, matricula, lista_plazas, id_plaza, pin):
        cont = 0
        while cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            # Si la plaza está ocupada, y su ID coincide con el indicado, además de que coincida con el PIN y matricula
            # del cliente, retorna la plaza
            if isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == id_plaza and plaza.ocupada.pin == pin and \
                    plaza.ocupada.cliente.vehiculo.matricula == matricula:
                return plaza
            cont += 1
        return None

    def salida_vehiculo(self, plaza, lista_plazas, lista_cobros):
        # Si lo que se recibe es una instancia de plaza, y esta está ocupada:
        if isinstance(plaza, Plaza) and isinstance(plaza.ocupada, Ocupada):
            # Setea la fecha de salida a la del momento en que se gestiona, y produce un nuevo cobro. Además, la plaza
            # pasa a estar desocupada, y se actualiza el listado de las mismas
            ocupada = plaza.ocupada
            ocupada.fecha_salida = datetime.now()
            cobro = Cobro(ocupada.cliente.vehiculo.matricula, ocupada.fecha_deposito, ocupada.fecha_salida,
                          ocupada.coste_final)
            plaza.ocupada = None
            plaza.actualizar_listado(lista_plazas)
            # Si la plaza está ocupada por un cliente ocasional, actualiza la lista de cobros con el nuevo
            if not isinstance(ocupada.cliente, ClienteAbono):
                cobro.actualizar_listado(lista_cobros)
            return cobro
        else:
            return None

    def buscar_cliente(self, matricula, dni, lista_clientes):
        cont = 0
        while cont != len(lista_clientes):
            cliente = lista_clientes[cont]
            # Si el cliente está abonado, y coinciden la matricula y el DNI, devuelve el cliente
            if isinstance(cliente, ClienteAbono) and cliente.vehiculo.matricula == matricula and cliente.dni == dni:
                return cliente
            cont += 1
        return None

    def depositar_abonado(self, cliente, lista_plazas):
        cont = 0
        while cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            # Si la plaza no está ocupada y el ID de esta coincide con el ID de la plaza asignada al abono del cliente:
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == cliente.abono.plaza.id_plaza:
                # Ocupa la plaza y actualiza el listado
                plaza.ocupada = Ocupada(cliente)
                plaza.actualizar_listado(lista_plazas)
                return plaza
            cont += 1
        return None
