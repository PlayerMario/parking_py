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
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas:
                if plaza.tipo_vehiculo == "Turismo":
                    num_turismo += 1
                elif plaza.tipo_vehiculo == "Motocicleta":
                    num_moto += 1
                else:
                    num_mov_red += 1
        return num_turismo, num_moto, num_mov_red, parking_views.mostrar_disponibles(num_turismo, num_moto, num_mov_red)

    def devolver_tipo(self, opTipo, lista_plazas, reservadas):
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
            if isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == id_plaza and plaza.ocupada.pin == pin and \
                    plaza.ocupada.cliente.vehiculo.matricula == matricula:
                return plaza
            cont += 1
        return None

    def salida_vehiculo(self, plaza, lista_plazas, lista_cobros):
        if isinstance(plaza, Plaza) and isinstance(plaza.ocupada, Ocupada):
            ocupada = plaza.ocupada
            ocupada.fecha_salida = datetime.now()
            cobro = Cobro(ocupada.cliente.vehiculo.matricula, ocupada.fecha_deposito, ocupada.fecha_salida,
                          ocupada.coste_final)
            plaza.ocupada = None
            plaza.actualizar_listado(lista_plazas)
            if not isinstance(ocupada.cliente, ClienteAbono):
                cobro.actualizar_listado(lista_cobros)
            return cobro
        else:
            return None

    def buscar_cliente(self, matricula, dni, lista_clientes):
        cont = 0
        while cont != len(lista_clientes):
            cliente = lista_clientes[cont]
            if isinstance(cliente, ClienteAbono) and cliente.vehiculo.matricula == matricula and cliente.dni == dni:
                return cliente
            cont += 1
        return None

    def depositar_abonado(self, cliente, lista_plazas):
        cont = 0
        while cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == cliente.abono.plaza.id_plaza:
                plaza.ocupada = Ocupada(cliente)
                plaza.actualizar_listado(lista_plazas)
                return plaza
            cont += 1
        return None
