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
usuario = "user"
pswd = "1234"
parking = Data.parking
lista_clientes = Data.listaClientes

print("Bienvenido al Parking Triana.\n")

# MENÚ ZONA:
while opZona != 0:

    for i in parking.plazas:
        if isinstance(i.ocupada, Ocupada):
            print(i)

    opZona = int(input("\nSeleccione una opción:\n[1] Acceso clientes.\n[2] Adminstración.\n[0] Salir.\n> "))

    if opZona == 1:
        # MENÚ CLIENTE
        opCliente = -1
        while opCliente != 0:
            opCliente = int(input("\nSeleccione una opción:\n[1] Depositar vehículo.\n[2] Retirar vehículo."
                                  "\n[3] Depositar abonados.\n[4] Retirar abonados.\n[0] Salir.\n> "))

            if opCliente == 1:
                parking.mostrar_info_plazas(Data.lista_reservadas)
                opTipo = int(input("\nSeleccione el tipo:\n[1] Turismo.\n[2] Motocicleta."
                                   "\n[3] Movilidad Reducida.\n> "))

                if (opTipo == 1 and parking.mostrar_libres(Data.lista_reservadas)[0] != 0) \
                        or (opTipo == 2 and parking.mostrar_libres(Data.lista_reservadas)[1] != 0) \
                        or (opTipo == 3 and parking.mostrar_libres(Data.lista_reservadas)[2] != 0):

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
                    print("Opción 1")

                elif opAdmin == 2:
                    print("Opción 2")

                elif opAdmin == 3:
                    print("Opción 3")

                elif opAdmin == 4:
                    print("Opción 4")

                elif opAdmin == 5:
                    print("Opción 5")

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
