import pickle

from models.ocupada import Ocupada
from views.parking_views import ParkingViews

# CARGAR TODAS LAS LISTAS AL PRINCIPIO

# f_parking = open('../data/parking.pckl', 'rb')
# parking = pickle.load(f_parking)
# f_parking.close()
#
# def cargar_datos():
#     f_clientes = open('../data/lista_clientes.pckl', 'rb')
#     clientes = pickle.load(f_clientes)
#     f_clientes.close()
#
#     f_cobros_abono = open('../data/lista_cobros_abono.pckl', 'rb')
#     cobros_abono = pickle.load(f_cobros_abono)
#     f_cobros_abono.close()
#
#     f_reservadas = open('../data/lista_reservadas.pckl', 'rb')
#     reservadas = pickle.load(f_reservadas)
#     f_reservadas.close()
#
#     f_cobros = open('../data/lista_cobros.pckl', 'rb')
#     cobros = pickle.load(f_cobros)
#     f_cobros.close()
#
#     parking.clientes = clientes
#     parking.cobros_abonos = cobros_abono
#     parking.reservadas = reservadas
#     parking.cobros = cobros
#
#     return parking

parking_views = ParkingViews()


class ParkingService:
    def mostrar_libres(self, parking, lista_reservadas):
        num_turismo = 0
        num_moto = 0
        num_mov_red = 0
        for plaza in parking.plazas:
            if not isinstance(plaza.ocupada, Ocupada) and plaza not in lista_reservadas:
                if plaza.tipo_vehiculo == "Turismo":
                    num_turismo += 1
                elif plaza.tipo_vehiculo == "Motocicleta":
                    num_moto += 1
                else:
                    num_mov_red += 1
        return num_turismo, num_moto, num_mov_red, parking_views.mostrar_disponibles(num_turismo, num_moto, num_mov_red)

    def devolver_tipo(self, opTipo, parking, reservadas):
        if opTipo == 1 and self.mostrar_libres(parking, reservadas)[0] != 0:
            tipo_vehiculo = "Turismo"
        elif opTipo == 2 and self.mostrar_libres(parking, reservadas)[1] != 0:
            tipo_vehiculo = "Motocicleta"
        elif opTipo == 3 and self.mostrar_libres(parking, reservadas)[2] != 0:
            tipo_vehiculo = "Movilidad Reducida"
        else:
            tipo_vehiculo = ""
        return tipo_vehiculo

    def depositar_ocasional(self, parking, cliente, reservadas):
        salir = False
        cont = 0
        while not salir and cont != len(parking.plazas):
            plaza = parking.plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada) and plaza not in reservadas:
                if plaza.tipo_vehiculo == cliente.vehiculo.tipo:
                    plaza.ocupada = Ocupada(cliente)
                    salir = True
                    return plaza
            cont += 1
