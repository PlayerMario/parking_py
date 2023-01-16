from data.data import Data
from models.cliente import Cliente
from models.ocupada import Ocupada
from models.vehiculo import Vehiculo

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opTipo = -1
usuario = "user"
pswd = "1234"
parking = Data.parking

print("Bienvenido al Parking Triana.")

# for i in Data.parking.plazas:
#     if isinstance(i.ocupada, Ocupada):
#         print(i)

# MENÚ ZONA:
while opZona != 0:
    opZona = int(input("""\nSeleccione una opción:
        [1] Acceso clientes.
        [2] Adminstración.
        [0] Salir.
        > """))

    if opZona == 1:
        # MENÚ CLIENTE
        while opCliente != 0:
            opCliente = int(input("""\nSeleccione una opción:
                [1] Depositar vehículo.
                [2] Retirar vehículo.
                [3] Depositar abonados.
                [4] Retirar abonados.
                [0] Salir.
                > """))

            if opCliente == 1:
                parking.mostrar_info_plazas()
                opTipo = int(input("""\nSeleccione el tipo:
                                [1] Turismo.
                                [2] Motocicleta.
                                [3] Movilidad Reducida.
                                > """))
                if (opTipo == 1 and parking.mostrar_libres()[0] != 0) \
                        or (opTipo == 2 and parking.mostrar_libres()[1] != 0) \
                        or (opTipo == 3 and parking.mostrar_libres()[2] != 0):

                    matricula = input("Indique su matrícula: ")

                    if opTipo == 1:
                        tipo_vehiculo = "Turismo"

                    elif opTipo == 2:
                        tipo_vehiculo = "Motocicleta"

                    else:
                        tipo_vehiculo = "Movilidad Reducida"

                    parking.depositar_ocasional(Cliente(Vehiculo(matricula, tipo_vehiculo)), tipo_vehiculo)

                else:
                    print("Opción incorrecta / No hay plazas de ese tipo disponibles")

            elif opCliente == 2:
                print("Opción 2")

            elif opCliente == 3:
                print("Opción 3")

            elif opCliente == 4:
                print("Opción 4")

            elif opCliente == 0:
                print("Saliendo...")

            else:
                print("Opción incorrecta.")

    elif opZona == 2:
        # PEDIR USUARIO Y CONTRASEÑA (user - 1234)
        user = input("\nIndique su usuario: ")
        psw = input("Indique su contraseña: ")

        # MENÚ ADMINISTRADOR
        if user == usuario and psw == pswd:
            while opAdmin != 0:
                opAdmin = int(input("""\nSeleccione una opción:
                    [1] Estado del parking.
                    [2] Facturación.
                    [3] Consulta de abonados.
                    [4] Abonos.
                    [5] Caducidad de abonos.
                    [0] Salir.
                    > """))

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
