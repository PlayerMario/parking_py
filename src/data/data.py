from models.abono import Abono
from models.cliente import Cliente
from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada
from models.parking import Parking
from models.vehiculo import Vehiculo


class Data:
    parking = Parking(num_plazas=40)

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

    listaVehiculos = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]

    a1 = Abono(tipo="Mensual", plaza=parking.plazas[35])
    a2 = Abono(tipo="Semestral", plaza=parking.plazas[1])
    a3 = Abono(tipo="Trimestral", plaza=parking.plazas[34])
    a4 = Abono(tipo="Anual", plaza=parking.plazas[29])
    a5 = Abono(tipo="Mensual", plaza=parking.plazas[4])
    a6 = Abono(tipo="Semestral", plaza=parking.plazas[15])
    a7 = Abono(tipo="Trimestral", plaza=parking.plazas[37])
    a8 = Abono(tipo="Anual", plaza=parking.plazas[30])

    listaAbonos = [a1, a2, a3, a4, a5, a6, a7, a8]

    c1 = Cliente(vehiculo=v1)
    c2 = ClienteAbono(vehiculo=v2, nombre="Bartolomé", apellidos="Méndez Zuluaga", dni="12345678A",
                      num_tarjeta="123-456",
                      email="bartolome@bartolome.com", abono=a3)
    c3 = ClienteAbono(vehiculo=v3, nombre="Juan", apellidos="Cuesta Hurtado", dni="63258741C", num_tarjeta="365-158",
                      email="juan@juan.com", abono=a2)
    c4 = Cliente(vehiculo=v4)
    c5 = ClienteAbono(vehiculo=v5, nombre="Isabel", apellidos="Ruiz García", dni="96521475B", num_tarjeta="854-032",
                      email="isabel@isabel.com", abono=a1)
    c6 = ClienteAbono(vehiculo=v6, nombre="Emilio", apellidos="Delgado Martín", dni="02145876G", num_tarjeta="852-370",
                      email="emilio@emilio.com", abono=a4)
    c7 = ClienteAbono(vehiculo=v7, nombre="Luis", apellidos="Verde Rodríguez", dni="65478201C", num_tarjeta="524-000",
                      email="luis@luis.com", abono=a5)
    c8 = ClienteAbono(vehiculo=v8, nombre="Antonio", apellidos="López Rincón", dni="87410256V", num_tarjeta="032-552",
                      email="antonio@antonio.com", abono=a6)
    c9 = ClienteAbono(vehiculo=v9, nombre="Ana", apellidos="Bascón Ruiz", dni="32147580B", num_tarjeta="201-369",
                      email="ana@ana.com", abono=a7)
    c10 = ClienteAbono(vehiculo=v10, nombre="Isabel", apellidos="Avilés Pérez", dni="21478503G",
                       num_tarjeta="336-807",
                       email="isabel@isabel.com", abono=a8)

    listaClientes = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    lista_reservadas = []
    for cliente in listaClientes:
        if isinstance(cliente, ClienteAbono):
            lista_reservadas.append(cliente.abono.plaza)

    o1 = Ocupada(cliente=c1)
    o2 = Ocupada(cliente=c2)
    o3 = Ocupada(cliente=c3)
    o4 = Ocupada(cliente=c4)
    o5 = Ocupada(cliente=c5)
    o6 = Ocupada(cliente=c6)

    listaOcupada = [o1, o2, o3, o4, o5, o6]

    for oc in listaOcupada:
        salir = False
        cont = 0
        while not salir:
            plaza = parking.plazas[cont]
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == oc.cliente.vehiculo.tipo:
                    plaza.ocupada = oc
                    salir = True
            cont += 1

    listaCobros = []
