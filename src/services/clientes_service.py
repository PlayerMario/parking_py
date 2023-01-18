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
        salir = False
        cont = 0
        while not salir and cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza not in reservadas \
                    and plaza.tipo_vehiculo == cliente.vehiculo.tipo:
                plaza.ocupada = Ocupada(cliente)
                salir = True
                return plaza
            cont += 1

    def buscar_plaza(self, matricula, lista_plazas, id_plaza, pin):
        salir = False
        cont = 0

        while not salir and cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            if isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == id_plaza and plaza.ocupada.pin == pin and \
                    plaza.ocupada.cliente.vehiculo.matricula == matricula:
                return plaza
            cont += 1
        return None

    def salida_vehiculo(self, plaza, lista_plazas):
        if isinstance(plaza, Plaza):
            ocupada = plaza.ocupada
            if isinstance(ocupada, Ocupada):
                ocupada.fecha_salida = datetime.now()
                cobro = Cobro(matricula=ocupada.cliente.vehiculo.matricula, fecha_entrada=ocupada.fecha_deposito,
                              fecha_salida=ocupada.fecha_salida, cobro=ocupada.coste_final)
                if isinstance(ocupada.cliente, ClienteAbono):
                    plaza.ocupada = None
                    return cobro, plaza.actualizar_listado(lista_plazas)
                else:
                    ocupada.__del__()
                    return cobro
        else:
            return None

    def generar_cobro(self, plaza, lista_cobros, lista_plazas):
        if isinstance(plaza, Plaza):
            cobro = self.salida_vehiculo(plaza, lista_plazas)
            if isinstance(cobro, Cobro):
                plaza.ocupada = None
                return cobro, cobro.actualizar_listado(lista_cobros), \
                    plaza.actualizar_listado(lista_plazas)
            else:
                return None

    def buscar_cliente(self, matricula, dni, lista_clientes):
        salir = False
        cont = 0
        while not salir and cont != len(lista_clientes):
            cliente = lista_clientes[cont]
            if isinstance(cliente, ClienteAbono) and cliente.vehiculo.matricula == matricula and cliente.dni == dni:
                salir = True
                return cliente
            cont += 1
        return None

    def depositar_abonado(self, cliente, lista_plazas):
        salir = False
        cont = 0
        while not salir and cont != len(lista_plazas):
            plaza = lista_plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada) and plaza.id_plaza == cliente.abono.plaza.id_plaza:
                plaza.ocupada = Ocupada(cliente)
                salir = True
                return plaza, plaza.actualizar_listado(lista_plazas)
            cont += 1
        return None
