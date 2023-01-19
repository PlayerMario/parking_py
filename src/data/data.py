from datetime import datetime, timedelta
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
            lista_plazas.append(Plaza(f"{i}", "Turismo", Ocupada))
        elif i <= round(num_plazas * 0.85):
            lista_plazas.append(Plaza(f"{i}", "Motocicleta", Ocupada))
        else:
            lista_plazas.append(Plaza(f"{i}", "Movilidad Reducida", Ocupada))

    v1 = Vehiculo("1111AAA", "Turismo")
    v2 = Vehiculo("3215OGR", "Movilidad Reducida")
    v3 = Vehiculo("9581BDS", "Turismo")
    v4 = Vehiculo("1234AWE", "Motocicleta")
    v5 = Vehiculo("6325UJM", "Movilidad Reducida")
    v6 = Vehiculo("1024QWE", "Motocicleta")
    v7 = Vehiculo("5214AVG", "Turismo")
    v8 = Vehiculo("5677LMJ", "Turismo")
    v9 = Vehiculo("4766CVF", "Movilidad Reducida")
    v10 = Vehiculo("2014POK", "Motocicleta")
    v11 = Vehiculo("3302DDC", "Turismo")

    a1 = Abono("Mensual", lista_plazas[35])
    a2 = Abono("Semestral", lista_plazas[1])
    a3 = Abono("Trimestral", lista_plazas[34])
    a4 = Abono("Anual", lista_plazas[29])
    a5 = Abono("Mensual", lista_plazas[4])
    a6 = Abono("Semestral", lista_plazas[15])
    a7 = Abono("Trimestral", lista_plazas[37])
    a8 = Abono("Anual", lista_plazas[30])
    a9 = Abono("Mensual", lista_plazas[10])
    a9.fecha_alta = datetime.now()
    a9.fecha_cancelacion = a9.fecha_alta + timedelta(days=6)

    c1 = Cliente(v1)
    c2 = ClienteAbono(v2, "Bartolomé", "Méndez Zuluaga", "12345678A", "123-456", "bartolome@bartolome.com", a3)
    coa2 = CobroAbono(c2.vehiculo.matricula, c2.abono.fecha_alta, c2.abono.fecha_cancelacion, c2.abono.precio,
                      c2.num_tarjeta)
    c3 = ClienteAbono(v3, "Juan", "Cuesta Hurtado", "63258741C", "365-158", "juan@juan.com", a2)
    coa3 = CobroAbono(c3.vehiculo.matricula, c3.abono.fecha_alta, c3.abono.fecha_cancelacion, c3.abono.precio,
                      c3.num_tarjeta)
    c4 = Cliente(v4)
    c5 = ClienteAbono(v5, "Isabel", "Ruiz García", "96521475B", "854-032", "isabel@isabel.com", a1)
    coa5 = CobroAbono(c5.vehiculo.matricula, c5.abono.fecha_alta, c5.abono.fecha_cancelacion, c5.abono.precio,
                      c5.num_tarjeta)
    c6 = ClienteAbono(v6, "Emilio", "Delgado Martín", "02145876G", "852-370", "emilio@emilio.com", a4)
    coa6 = CobroAbono(c6.vehiculo.matricula, c6.abono.fecha_alta, c6.abono.fecha_cancelacion, c6.abono.precio,
                      c6.num_tarjeta)
    c7 = ClienteAbono(v7, "Luis", "Verde Rodríguez", "65478201C", "524-000", "luis@luis.com", a5)
    coa7 = CobroAbono(c7.vehiculo.matricula, c7.abono.fecha_alta, c7.abono.fecha_cancelacion, c7.abono.precio,
                      c7.num_tarjeta)
    c8 = ClienteAbono(v8, "Antonio", "López Rincón", "87410256V", "032-552", "antonio@antonio.com", a6)
    coa8 = CobroAbono(c8.vehiculo.matricula, c8.abono.fecha_alta, c8.abono.fecha_cancelacion, c8.abono.precio,
                      c8.num_tarjeta)
    c9 = ClienteAbono(v9, "Ana", "Bascón Ruiz", "32147580B", "201-369", "ana@ana.com", a7)
    coa9 = CobroAbono(c9.vehiculo.matricula, c9.abono.fecha_alta, c9.abono.fecha_cancelacion, c9.abono.precio,
                      c9.num_tarjeta)
    c10 = ClienteAbono(v10, "Isabel", "Avilés Pérez", "21478503G", "336-807", "isabel@isabel.com", a8)
    coa10 = CobroAbono(c10.vehiculo.matricula, c10.abono.fecha_alta, c10.abono.fecha_cancelacion, c10.abono.precio,
                       c10.num_tarjeta)
    c11 = ClienteAbono(v11, "Jesús", "Martín Infante", "30021485B", "333-965", "jesus@jesus.com", a9)
    coa11 = CobroAbono(c11.vehiculo.matricula, c11.abono.fecha_alta, c11.abono.fecha_cancelacion, c11.abono.precio,
                       c11.num_tarjeta)
    lista_clientes = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]
    lista_cobros_abonos = [coa2, coa3, coa5, coa6, coa7, coa8, coa9, coa10, coa11]

    o1 = Ocupada(c1)
    o2 = Ocupada(c2)
    o3 = Ocupada(c3)
    o4 = Ocupada(c4)
    o5 = Ocupada(c5)
    o6 = Ocupada(c6)

    for oc in [o1, o2, o3, o4, o5, o6]:
        salir = False
        cont = 0
        while not salir:
            plaza = lista_plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == oc.cliente.vehiculo.tipo:
                    plaza.ocupada = oc
                    salir = True
            cont += 1

    co1 = Cobro("8521CFD", datetime(2022, 9, 23, 19, 12), datetime(2022, 9, 23, 21, 5), 13.56)
    co2 = Cobro("3214GVD", datetime(2022, 9, 25, 10, 20), datetime(2022, 9, 25, 17, 30), 34.4)
    co3 = Cobro("2147HBF", datetime(2022, 9, 11, 16, 25), datetime(2022, 9, 11, 18, 54), 14.9)
    co4 = Cobro("5201TGB", datetime(2022, 10, 6, 13, 3), datetime(2022, 10, 6, 22, 10), 65.64)
    co5 = Cobro("6324QSX", datetime(2022, 10, 30, 11, 41), datetime(2022, 10, 30, 12, 50), 5.52)
    co6 = Cobro("0142HNM", datetime(2022, 10, 23, 20, 36), datetime(2022, 10, 23, 22, 30), 11.4)
    co7 = Cobro("3014ERE", datetime(2022, 11, 23, 11, 29), datetime(2022, 11, 23, 14, 24), 21)
    co8 = Cobro("9879BNH", datetime(2022, 11, 8, 15, 1), datetime(2022, 11, 8, 18, 28), 16.56)
    co9 = Cobro("2214LMN", datetime(2022, 11, 16, 16, 12), datetime(2022, 11, 16, 19, 5), 17.3)
    co10 = Cobro("4152CXS", datetime(2022, 12, 23, 10, 32), datetime(2022, 12, 23, 13, 45), 23.16)
    co11 = Cobro("6632BNV", datetime(2022, 12, 10, 14, 32), datetime(2022, 12, 10, 19, 15), 22.64)
    co12 = Cobro("7456AZX", datetime(2022, 12, 20, 13, 36), datetime(2022, 12, 20, 15, 30), 11.4)
    co13 = Cobro("6399NMJ", datetime(2023, 1, 3, 12, 10), datetime(2023, 1, 3, 17, 26), 37.92)
    co14 = Cobro("1002EWQ", datetime(2023, 1, 14, 19, 20), datetime(2023, 1, 14, 21, 53), 12.24)
    co15 = Cobro("3652HMK", datetime(2023, 1, 16, 17, 29), datetime(2023, 1, 16, 19, 35), 12.6)
    lista_cobros = [co1, co2, co3, co4, co5, co6, co7, co8, co9, co10, co11, co12, co13, co14, co15]

    def reiniciar_datos(self):
        f_clientes = open('data/lista_clientes.pckl', 'wb')
        pickle.dump(self.lista_clientes, f_clientes)
        f_clientes.close()
        f_clientes = open('data/lista_clientes.pckl', 'rb')
        clientes = pickle.load(f_clientes)
        f_clientes.close()

        reservadas_id = []
        for cliente in clientes:
            if isinstance(cliente, ClienteAbono):
                reservadas_id.append(cliente.abono.plaza.id_plaza)

        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'wb')
        pickle.dump(self.lista_cobros_abonos, f_cobros_abono)
        f_cobros_abono.close()
        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'rb')
        cobros_abono = pickle.load(f_cobros_abono)
        f_cobros_abono.close()

        f_cobros = open('data/lista_cobros.pckl', 'wb')
        pickle.dump(self.lista_cobros, f_cobros)
        f_cobros.close()
        f_cobros = open('data/lista_cobros.pckl', 'rb')
        cobros = pickle.load(f_cobros)
        f_cobros.close()

        f_plazas = open('data/lista_plazas.pckl', 'wb')
        pickle.dump(self.lista_plazas, f_plazas)
        f_plazas.close()
        f_plazas = open('data/lista_plazas.pckl', 'rb')
        plazas = pickle.load(f_plazas)
        f_plazas.close()

        return clientes, cobros_abono, cobros, plazas, reservadas_id

    def cargar_datos(self):
        f_clientes = open('data/lista_clientes.pckl', 'rb')
        clientes = pickle.load(f_clientes)
        f_clientes.close()

        f_cobros_abono = open('data/lista_cobros_abono.pckl', 'rb')
        cobros_abono = pickle.load(f_cobros_abono)
        f_cobros_abono.close()

        f_cobros = open('data/lista_cobros.pckl', 'rb')
        cobros = pickle.load(f_cobros)
        f_cobros.close()

        f_plazas = open('data/lista_plazas.pckl', 'rb')
        plazas = pickle.load(f_plazas)
        f_plazas.close()

        reservadas_id = []
        for cliente in clientes:
            if isinstance(cliente, ClienteAbono):
                reservadas_id.append(cliente.abono.plaza.id_plaza)

        return clientes, cobros_abono, cobros, plazas, reservadas_id
