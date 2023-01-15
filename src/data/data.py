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

    listaVehiculos = [v1, v2, v3, v4, v5, v6]

    a1 = Abono(tipo="Mensual")
    a2 = Abono(tipo="Semestral")
    a3 = Abono(tipo="Trimestral")
    a4 = Abono(tipo="Anual")

    listaAbonos = [a1, a2, a3, a4]

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

    listaClientes = [c1, c2, c3, c4, c5, c6]

    o1 = Ocupada(cliente=c1)
    o2 = Ocupada(cliente=c2)
    o3 = Ocupada(cliente=c3)
    o4 = Ocupada(cliente=c4)
    o5 = Ocupada(cliente=c5)
    o6 = Ocupada(cliente=c6)

    listaOcupada = [o1, o2, o3, o4, o5, o6]

    # parking.plazas[0].ocupada = o1
    # parking.plazas[34].ocupada = o2
    # parking.plazas[1].ocupada = o3
    # parking.plazas[28].ocupada = o4
    # parking.plazas[35].ocupada = o5
    # parking.plazas[29].ocupada = o6

    for oc in listaOcupada:
        for plaza in parking.plazas:
            if not isinstance(plaza.ocupada, Ocupada):
                if plaza.tipo_vehiculo == oc.cliente.vehiculo.tipo:
                    plaza.ocupada = oc
                    break
