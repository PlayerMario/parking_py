from models.abono import Abono
from models.cliente import Cliente
from models.cliente_abono import ClienteAbono
from models.parking import Parking
from models.plaza_ocupada import PlazaOcupada
from models.vehiculo import Vehiculo

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opDepo = -1
usuario = "user"
pswd = "1234"

# DATOS DE PRUEBA
parking = Parking(num_plazas=40)
c1 = Cliente(vehiculo=Vehiculo(matricula="1111AAA", tipo="Turismo"))
c2 = ClienteAbono(vehiculo=Vehiculo(matricula="1234AWE", tipo="Motocicleta"))
c2.nombre = "Mario"
c2.apellidos = "Ruiz López"
c2.dni = "12345678A"
c2.num_tarjeta = "123-456"
c2.email = "mario@mario.com"
c2.abono = Abono("Trimestral")
parking.plazas[1].ocupado(PlazaOcupada(cliente=c1, abonado=False))

print("Bienvenido al Parking Triana.")

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
                # DEPOSITAR VEHÍCULO
                while opDepo != 0:
                    opDepo = int(input("""\nSeleccione una opción:
                        [1] Cliente abonado.
                        [2] Cliente sin abono.
                        [0] Salir.
                        > """))

                    if opDepo == 1:
                        pass

                    elif opDepo == 2:
                        pass

                    else:
                        print("Opción incorrecta.")

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
            while opCliente != 0:
                opCliente = int(input("""\nSeleccione una opción:
                    [1] Estado del parking.
                    [2] Facturación.
                    [3] Consulta de abonados.
                    [4] Abonos.
                    [5] Caducidad de abonos.
                    [0] Salir.
                    > """))

                if opCliente == 1:
                    print("Opción 1")

                elif opCliente == 2:
                    print("Opción 2")

                elif opCliente == 3:
                    print("Opción 3")

                elif opCliente == 4:
                    print("Opción 4")

                elif opCliente == 5:
                    print("Opción 5")

                elif opCliente == 0:
                    print("Saliendo...")

                else:
                    print("Opción incorrecta.")

        else:
            print("\nUsuario y/o contraseña errónea.")

    elif opZona == 0:
        print("Saliendo...")

    else:
        print("Opción incorrecta.")
