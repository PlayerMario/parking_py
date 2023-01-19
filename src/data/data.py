from datetime import datetime
import pickle
from models.abono import Abono
from models.cliente import Cliente
from models.cliente_abono import ClienteAbono
from models.cobros import Cobro
from models.cobros_abono import CobroAbono
from models.ocupada import Ocupada
from models.plaza import Plaza
from models.vehiculo import Vehiculo


class Data:
    lista_plazas = []
    num_plazas = 40
    for i in range(1, num_plazas + 1):
        if i <= round(num_plazas * 0.7):
            lista_plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Turismo", ocupada=Ocupada))
        elif i <= round(num_plazas * 0.85):
            lista_plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Motocicleta", ocupada=Ocupada))
        else:
            lista_plazas.append(Plaza(id_plaza=f"{i}", tipo_vehiculo="Movilidad Reducida", ocupada=Ocupada))

    v1 = Vehiculo(matricula="1111AAA", tipo="Turismo")
    v2 = Vehiculo(matricula="3215OGR", tipo="Movilidad Reducida")
    v3 = Vehiculo(matricula="9581BDS", tipo="Turismo")
    v4 = Vehiculo(matricula="1234AWE", tipo="Motocicleta")
    v5 = Vehiculo(matricula="6325UJM", tipo="Movilidad Reducida")
    v6 = Vehiculo(matricula="1024QWE", tipo="Motocicleta")
    v7 = Vehiculo(matricula="5214AVG", tipo="Turismo")
    v8 = Vehiculo(matricula="5677LMJ", tipo="Turismo")
    v9 = Vehiculo(matricula="4766CVF", tipo="Movilidad Reducida")
    v10 = Vehiculo(matricula="2014POK", tipo="Motocicleta")

    lista_vehiculos = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    a1 = Abono(tipo="Mensual", plaza=lista_plazas[35])
    a2 = Abono(tipo="Semestral", plaza=lista_plazas[1])
    a3 = Abono(tipo="Trimestral", plaza=lista_plazas[34])
    a4 = Abono(tipo="Anual", plaza=lista_plazas[29])
    a5 = Abono(tipo="Mensual", plaza=lista_plazas[4])
    a6 = Abono(tipo="Semestral", plaza=lista_plazas[15])
    a7 = Abono(tipo="Trimestral", plaza=lista_plazas[37])
    a8 = Abono(tipo="Anual", plaza=lista_plazas[30])

    lista_abonos = [a1, a2, a3, a4, a5, a6, a7, a8]

    c1 = Cliente(vehiculo=v1)
    c2 = ClienteAbono(vehiculo=v2, nombre="Bartolomé", apellidos="Méndez Zuluaga", dni="12345678A",
                      num_tarjeta="123-456",
                      email="bartolome@bartolome.com", abono=a3)
    coa2 = CobroAbono(c2.vehiculo.matricula, c2.abono.fecha_alta, c2.abono.fecha_cancelacion, c2.abono.precio,
                      c2.num_tarjeta)
    c3 = ClienteAbono(vehiculo=v3, nombre="Juan", apellidos="Cuesta Hurtado", dni="63258741C", num_tarjeta="365-158",
                      email="juan@juan.com", abono=a2)
    coa3 = CobroAbono(c3.vehiculo.matricula, c3.abono.fecha_alta, c3.abono.fecha_cancelacion, c3.abono.precio,
                      c3.num_tarjeta)
    c4 = Cliente(vehiculo=v4)
    c5 = ClienteAbono(vehiculo=v5, nombre="Isabel", apellidos="Ruiz García", dni="96521475B", num_tarjeta="854-032",
                      email="isabel@isabel.com", abono=a1)
    coa5 = CobroAbono(c5.vehiculo.matricula, c5.abono.fecha_alta, c5.abono.fecha_cancelacion, c5.abono.precio,
                      c5.num_tarjeta)
    c6 = ClienteAbono(vehiculo=v6, nombre="Emilio", apellidos="Delgado Martín", dni="02145876G", num_tarjeta="852-370",
                      email="emilio@emilio.com", abono=a4)
    coa6 = CobroAbono(c6.vehiculo.matricula, c6.abono.fecha_alta, c6.abono.fecha_cancelacion, c6.abono.precio,
                      c6.num_tarjeta)
    c7 = ClienteAbono(vehiculo=v7, nombre="Luis", apellidos="Verde Rodríguez", dni="65478201C", num_tarjeta="524-000",
                      email="luis@luis.com", abono=a5)
    coa7 = CobroAbono(c7.vehiculo.matricula, c7.abono.fecha_alta, c7.abono.fecha_cancelacion, c7.abono.precio,
                      c7.num_tarjeta)
    c8 = ClienteAbono(vehiculo=v8, nombre="Antonio", apellidos="López Rincón", dni="87410256V", num_tarjeta="032-552",
                      email="antonio@antonio.com", abono=a6)
    coa8 = CobroAbono(c8.vehiculo.matricula, c8.abono.fecha_alta, c8.abono.fecha_cancelacion, c8.abono.precio,
                      c8.num_tarjeta)
    c9 = ClienteAbono(vehiculo=v9, nombre="Ana", apellidos="Bascón Ruiz", dni="32147580B", num_tarjeta="201-369",
                      email="ana@ana.com", abono=a7)
    coa9 = CobroAbono(c9.vehiculo.matricula, c9.abono.fecha_alta, c9.abono.fecha_cancelacion, c9.abono.precio,
                      c9.num_tarjeta)
    c10 = ClienteAbono(vehiculo=v10, nombre="Isabel", apellidos="Avilés Pérez", dni="21478503G",
                       num_tarjeta="336-807",
                       email="isabel@isabel.com", abono=a8)
    coa10 = CobroAbono(c10.vehiculo.matricula, c10.abono.fecha_alta, c10.abono.fecha_cancelacion, c10.abono.precio,
                       c10.num_tarjeta)
    lista_clientes = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    lista_cobros_abonos = [coa2, coa3, coa5, coa6, coa7, coa8, coa9, coa10]

    lista_reservadas = []
    for cliente in lista_clientes:
        if isinstance(cliente, ClienteAbono):
            lista_reservadas.append(cliente.abono.plaza)

    o1 = Ocupada(cliente=c1)
    o2 = Ocupada(cliente=c2)
    o3 = Ocupada(cliente=c3)
    o4 = Ocupada(cliente=c4)
    o5 = Ocupada(cliente=c5)
    o6 = Ocupada(cliente=c6)

    lista_ocupadas = [o1, o2, o3, o4, o5, o6]
    for oc in lista_ocupadas:
        salir = False
        cont = 0
        while not salir:
            plaza = lista_plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == oc.cliente.vehiculo.tipo:
                    plaza.ocupada = oc
                    salir = True
            cont += 1

    co1 = Cobro(matricula="8521CFD", fecha_entrada=datetime(2022, 9, 23, 19, 12),
                fecha_salida=datetime(2022, 9, 23, 21, 5), cobro=13.56)  # Turismo
    co2 = Cobro(matricula="3214GVD", fecha_entrada=datetime(2022, 9, 25, 10, 20),
                fecha_salida=datetime(2022, 9, 25, 17, 30), cobro=34.4)  # Motocicleta
    co3 = Cobro(matricula="2147HBF", fecha_entrada=datetime(2022, 9, 11, 16, 25),
                fecha_salida=datetime(2022, 9, 11, 18, 54), cobro=14.9)  # MovRed
    co4 = Cobro(matricula="5201TGB", fecha_entrada=datetime(2022, 10, 6, 13, 3),
                fecha_salida=datetime(2022, 10, 6, 22, 10), cobro=65.64)  # Turismo
    co5 = Cobro(matricula="6324QSX", fecha_entrada=datetime(2022, 10, 30, 11, 41),
                fecha_salida=datetime(2022, 10, 30, 12, 50), cobro=5.52)  # Motocicleta
    co6 = Cobro(matricula="0142HNM", fecha_entrada=datetime(2022, 10, 23, 20, 36),
                fecha_salida=datetime(2022, 10, 23, 22, 30), cobro=11.4)  # MovRed
    co7 = Cobro(matricula="3014ERE", fecha_entrada=datetime(2022, 11, 23, 11, 29),
                fecha_salida=datetime(2022, 11, 23, 14, 24), cobro=21)  # Turismo
    co8 = Cobro(matricula="9879BNH", fecha_entrada=datetime(2022, 11, 8, 15, 1),
                fecha_salida=datetime(2022, 11, 8, 18, 28), cobro=16.56)  # Motocicleta
    co9 = Cobro(matricula="2214LMN", fecha_entrada=datetime(2022, 11, 16, 16, 12),
                fecha_salida=datetime(2022, 11, 16, 19, 5), cobro=17.3)  # MovRed
    co10 = Cobro(matricula="4152CXS", fecha_entrada=datetime(2022, 12, 23, 10, 32),
                 fecha_salida=datetime(2022, 12, 23, 13, 45), cobro=23.16)  # Turismo
    co11 = Cobro(matricula="6632BNV", fecha_entrada=datetime(2022, 12, 10, 14, 32),
                 fecha_salida=datetime(2022, 12, 10, 19, 15), cobro=22.64)  # Motocicleta
    co12 = Cobro(matricula="7456AZX", fecha_entrada=datetime(2022, 12, 20, 13, 36),
                 fecha_salida=datetime(2022, 12, 20, 15, 30), cobro=11.4)  # MovRed
    co13 = Cobro(matricula="6399NMJ", fecha_entrada=datetime(2023, 1, 3, 12, 10),
                 fecha_salida=datetime(2023, 1, 3, 17, 26), cobro=37.92)  # Turismo
    co14 = Cobro(matricula="1002EWQ", fecha_entrada=datetime(2023, 1, 14, 19, 20),
                 fecha_salida=datetime(2023, 1, 14, 21, 53), cobro=12.24)  # Motocicleta
    co15 = Cobro(matricula="3652HMK", fecha_entrada=datetime(2023, 1, 16, 17, 29),
                 fecha_salida=datetime(2023, 1, 16, 19, 35), cobro=12.6)  # MovRed
    lista_cobros = [co1, co2, co3, co4, co5, co6, co7, co8, co9, co10, co11, co12, co13, co14, co15]

    # SI NO SE METEN DATOS DE PRUEBA, AL INICIAR LA SESIÓN SOLO HABRÍA QUE HACER UN LOAD EN UNA LISTA VACÍA, POR EJEMPLO
    # f_vehiculos = open('data/lista_vehiculos.pckl', 'rb')
    #         vehiculos = pickle.load(f_vehiculos)
    #         f_vehiculos.close()
    #         return vehiculos
    # y en el main se guardaría en un vehiculos = cargar_vehiculos() para que siempre se traiga la lista actualizada
    # PROBAR A HACER UN RUN ASÍ, Y QUITAR DESPÚES LOS DATOS DE PRUEBA Y LOS DUMP AL CARGAR PARA QUE AL VOVLER A EJECUTAR
    # NO SE SOBREESCRIBAN Y SE QUEDEN AHÍ GUARDADOS
    # AL CERRAR SESIÓN, GUARDARÍA TODAS LAS LISTAS, O NO HARÍA FALTA PORQUE AL ACTUALIZARLAS YA SE HACE EL PASO DE
    # GUARDAR
    # NO BORRAR, DEJAR COMENTADO EN LOS CARGAR, LA PARTE DE .dump

    def cargar_vehiculos(self):
        f_vehiculos = open('data/lista_vehiculos.pckl', 'wb')
        pickle.dump(self.lista_vehiculos, f_vehiculos)
        f_vehiculos.close()
        f_vehiculos = open('data/lista_vehiculos.pckl', 'rb')
        vehiculos = pickle.load(f_vehiculos)
        f_vehiculos.close()
        return vehiculos

    def cargar_abonos(self):
        f_abonos = open('data/lista_abonos.pckl', 'wb')
        pickle.dump(self.lista_abonos, f_abonos)
        f_abonos.close()
        f_abonos = open('data/lista_abonos.pckl', 'rb')
        abonos = pickle.load(f_abonos)
        f_abonos.close()
        return abonos

    def cargar_clientes(self):
        f_clientes = open('data/lista_clientes.pckl', 'wb')
        pickle.dump(self.lista_clientes, f_clientes)
        f_clientes.close()
        f_clientes = open('data/lista_clientes.pckl', 'rb')
        clientes = pickle.load(f_clientes)
        f_clientes.close()
        return clientes

    def cargar_cobros_abono(self):
        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'wb')
        pickle.dump(self.lista_cobros_abonos, f_cobros_abono)
        f_cobros_abono.close()
        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'rb')
        cobros_abono = pickle.load(f_cobros_abono)
        f_cobros_abono.close()
        return cobros_abono

    def cargar_reservadas(self):
        f_reservadas = open('data/lista_reservadas.pckl', 'wb')
        pickle.dump(self.lista_reservadas, f_reservadas)
        f_reservadas.close()
        f_reservadas = open('data/lista_reservadas.pckl', 'rb')
        reservadas = pickle.load(f_reservadas)
        f_reservadas.close()
        return reservadas

    def cargar_ocupadas(self):
        f_ocupadas = open('data/lista_ocupadas.pckl', 'wb')
        pickle.dump(self.lista_ocupadas, f_ocupadas)
        f_ocupadas.close()
        f_ocupadas = open('data/lista_ocupadas.pckl', 'rb')
        ocupadas = pickle.load(f_ocupadas)
        f_ocupadas.close()
        return ocupadas

    def cargar_cobros(self):
        f_cobros = open('data/lista_cobros.pckl', 'wb')
        pickle.dump(self.lista_cobros, f_cobros)
        f_cobros.close()
        f_cobros = open('data/lista_cobros.pckl', 'rb')
        cobros = pickle.load(f_cobros)
        f_cobros.close()
        return cobros
    #
    # def cargar_parking(self):
    #     f_parking = open('data/parking.pckl', 'wb')
    #     pickle.dump(self.parking, f_parking)
    #     f_parking.close()
    #     f_parking = open('data/parking.pckl', 'rb')
    #     parking = pickle.load(f_parking)
    #     f_parking.close()
    #     return parking

    def cargar_plazas(self):
        f_plazas = open('data/lista_plazas.pckl', 'wb')
        pickle.dump(self.lista_plazas, f_plazas)
        f_plazas.close()
        f_plazas = open('data/lista_plazas.pckl', 'rb')
        plazas = pickle.load(f_plazas)
        f_plazas.close()
        return plazas
