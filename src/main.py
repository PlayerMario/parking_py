from datetime import datetime

from data.data import Data
from models.cliente import Cliente
from models.cliente_abono import ClienteAbono
from models.cobros import Cobro
from models.ocupada import Ocupada
from models.plaza import Plaza
from models.vehiculo import Vehiculo

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opAbono = -1
opCad = -1
usuario = "user"
pswd = "1234"
parking = Data.parking
lista_clientes = Data.listaClientes
lista_reservadas = Data.lista_reservadas
lista_cobros = Data.listaCobros

print("Bienvenido al Parking Triana.\n")

# MENÚ ZONA:
while opZona != 0:

    # for i in parking.plazas:
    #     if isinstance(i.ocupada, Ocupada):
    #         print(i)

    opZona = int(input("\nSeleccione una opción:\n[1] Acceso clientes.\n[2] Adminstración.\n[0] Salir.\n> "))

    if opZona == 1:
        # MENÚ CLIENTE
        opCliente = -1
        while opCliente != 0:
            opCliente = int(input("\nSeleccione una opción:\n[1] Depositar vehículo.\n[2] Retirar vehículo."
                                  "\n[3] Depositar abonados.\n[4] Retirar abonados.\n[0] Salir.\n> "))

            if opCliente == 1:
                parking.mostrar_info_plazas(lista_reservadas)
                opTipo = int(input("\nSeleccione el tipo:\n[1] Turismo.\n[2] Motocicleta."
                                   "\n[3] Movilidad Reducida.\n> "))

                if (opTipo == 1 and parking.mostrar_libres(lista_reservadas)[0] != 0) \
                        or (opTipo == 2 and parking.mostrar_libres(lista_reservadas)[1] != 0) \
                        or (opTipo == 3 and parking.mostrar_libres(lista_reservadas)[2] != 0):

                    matricula = input("Indique su matrícula: ")

                    if opTipo == 1:
                        tipo_vehiculo = "Turismo"

                    elif opTipo == 2:
                        tipo_vehiculo = "Motocicleta"

                    else:
                        tipo_vehiculo = "Movilidad Reducida"

                    parking.mostrar_ticket(
                        parking.depositar_ocasional(Cliente(Vehiculo(matricula, tipo_vehiculo)), tipo_vehiculo))

                else:
                    print("Opción incorrecta / No hay plazas de ese tipo disponibles")

            elif opCliente == 2:
                matricula = input("Indique su matrícula: ")
                id_plaza = input("Indique la plaza: ")
                pin = input("Indique su pin: ")

                plaza = parking.buscar_plaza(matricula, id_plaza, pin)
                if isinstance(plaza, Plaza):
                    cobro = plaza.ocupada.salida_vehiculo()
                    if isinstance(cobro, Cobro):
                        Data.listaCobros.append(plaza.ocupada.salida_vehiculo())
                    print(plaza.ocupada.salida_vehiculo())
                    plaza.ocupada = None
                else:
                    print("Error en la operación.")

            elif opCliente == 3:
                matricula = input("Indique su matrícula: ")
                dni = input("Indique su DNI: ")

                cliente = ClienteAbono.buscar_cliente(None, matricula, dni, lista_clientes)
                if isinstance(cliente, ClienteAbono):
                    parking.mostrar_ticket(parking.depositar_abonado(cliente))
                else:
                    print("\nNo se ha encontrado cliente.")

            elif opCliente == 4:
                matricula = input("Indique su matrícula: ")
                id_plaza = input("Indique la plaza: ")
                pin = input("Indique su pin: ")

                plaza = parking.buscar_plaza(matricula, id_plaza, pin)
                if isinstance(plaza, Plaza):
                    print(plaza.ocupada.salida_vehiculo())
                    plaza.ocupada = None

            elif opCliente == 0:
                print("Saliendo...")

            else:
                print("Opción incorrecta.")

    elif opZona == 2:
        # USUARIO Y CONTRASEÑA (user - 1234)
        user = input("\nIndique su usuario: ")
        psw = input("Indique su contraseña: ")

        # MENÚ ADMINISTRADOR
        if user == usuario and psw == pswd:
            opAdmin = -1
            while opAdmin != 0:
                opAdmin = int(input("\nSeleccione una opción:\n[1] Estado del parking.\n[2] Facturación."
                                    "\n[3] Consulta de abonados.\n[4] Abonos.\n[5] Caducidad de abonos."
                                    "\n[0] Salir.\n> "))

                if opAdmin == 1:
                    parking.estado_parking(lista_reservadas)

                elif opAdmin == 2:
                    print("Indique la primera fecha: ")
                    fecha1 = datetime(int(input("Indique el año: ")), int(input("Indique el mes: ")),
                                      int(input("Indique el día: ")), int(input("Indique la hora: ")))

                    print("Indique la segunda fecha: ")
                    fecha2 = datetime(int(input("Indique el año: ")), int(input("Indique el mes: ")),
                                      int(input("Indique el día: ")), int(input("Indique la hora: ")))

                    print(f"{fecha1.strftime('%d/%m/%Y, %H:%M')} - {fecha2.strftime('%d/%m/%Y, %H:%M')}\n")

                    Cobro.mostrar_facturacion(None, Cobro.obtener_facturacion(None, fecha1, fecha2, lista_cobros))

                elif opAdmin == 3:
                    ClienteAbono.buscar_abonados(None, lista_clientes)

                elif opAdmin == 4:
                    opAbono = -1
                    while opAbono != 0:
                        opAbono = int(input("\nSeleccione una opción:\n[1] Nuevo abonado.\n[2] Modificación abonado."
                                            "\n[3] Baja de abonado.\n[0] Salir.\n> "))
                        if opAbono == 1:
                            pass
                        elif opAbono == 2:
                            pass
                        elif opAbono == 3:
                            pass
                        elif opAbono == 0:
                            print("Saliendo...")
                        else:
                            print("Opción incorrecta.")

                elif opAdmin == 5:
                    opCad = -1
                    while opCad != 0:
                        opCad = int(input("\nSeleccione una opción:\n[1] Caducidad en un mes.\n[2] Caducidad "
                                          "en próximos 10 días.\n[0] Salir.\n> "))
                        if opCad == 1:
                            pass
                        elif opCad == 2:
                            pass
                        elif opCad == 0:
                            print("Saliendo...")
                        else:
                            print("Opción incorrecta.")

                elif opAdmin == 0:
                    print("Saliendo...")

                else:
                    print("Opción incorrecta.")

        else:
            print("\nUsuario y/o contraseña errónea.")

    elif opZona == 0:
        print("Saliendo...")

    else:
        print("Opción incorrecta.")
