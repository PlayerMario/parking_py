from datetime import datetime
from data.data import Data
from models.abono import Abono
from models.cliente import Cliente
from models.vehiculo import Vehiculo
from services.admin_service import AdminService
from services.clientes_service import ClienteService
from services.validar_service import ValidarService
from views.menu_views import MenuViews
from views.parking_views import ParkingViews
from views.pruebas_views import PruebasView

# VARIABLES APLICACIÓN:
menu_views = MenuViews()
parking_views = ParkingViews()
pruebas = PruebasView()
cliente_service = ClienteService()
admin_service = AdminService()
validar_service = ValidarService()
data = Data()
usuario = "admin"
pswd = "1234"

# REINICIAR DATOS INICIALES:
# clientes, cobros_abono, cobros, plazas, reservadas_id = data.reiniciar_datos()

# CARGAR DATOS INICIALES:
clientes, cobros_abono, cobros, plazas, reservadas_id = data.cargar_datos()

print("Bienvenido al Parking Triana.")

opZona = -1
while opZona != 0:
    try:
        opZona = int(input(menu_views.menu_ppal()))
        if opZona == 1:
            opCliente = -1
            while opCliente != 0:
                try:
                    opCliente = int(input(menu_views.menu_cliente()))
                    if opCliente == 1:
                        print(cliente_service.mostrar_libres(plazas, reservadas_id)[3])
                        try:
                            opTipo = int(input(menu_views.menu_tipo_vehiculo()))
                            tipo_vehiculo = cliente_service.devolver_tipo(opTipo, plazas, reservadas_id)
                            if tipo_vehiculo != "":
                                matricula = input("Indique su matrícula (1234ABC): ").upper()
                                if validar_service.comprobar_matricula_existe(matricula, plazas, clientes):
                                    c = Cliente(Vehiculo(matricula, tipo_vehiculo))
                                    c.actualizar_listado(clientes)
                                    plaza = cliente_service.depositar_ocasional(plazas, c, reservadas_id)
                                    if plaza is not None:
                                        parking_views.mostrar_ticket(plaza)
                                    else:
                                        print("Error al asignar una plaza.")
                                else:
                                    print("\nMatricula existente o errónea.")
                            else:
                                print("Opción incorrecta / No hay plazas disponibles.")
                        except ValueError:
                            print("\nError, introduzca un número.")

                    elif opCliente == 2 or opCliente == 4:
                        matricula = input("Indique su matrícula (1234ABC): ").upper()
                        id_plaza = input("Indique la plaza: ")
                        pin = input("Indique su pin: ")
                        plaza = cliente_service.buscar_plaza(matricula, plazas, id_plaza, pin)
                        cobro = cliente_service.salida_vehiculo(plaza, plazas, cobros)
                        if cobro is not None:
                            print(cobro)
                        else:
                            print("\nError en la operación.")

                    elif opCliente == 3:
                        matricula = input("Indique su matrícula (1234ABC): ").upper()
                        dni = input("Indique su DNI (12345678A): ").upper()
                        cliente = cliente_service.buscar_cliente(matricula, dni, clientes)
                        if cliente is not None:
                            plaza = cliente_service.depositar_abonado(cliente, plazas)
                            if plaza is not None:
                                parking_views.mostrar_ticket(plaza)
                            else:
                                print("\nNo se ha podido completar la operación.")
                        else:
                            print("\nAbonado no encontrado.")

                    elif opCliente == 0:
                        print("Saliendo...")
                    else:
                        print("Opción incorrecta.")
                except ValueError:
                    print("\nError, introduzca un número.")

        elif opZona == 2:
            user = input("Indique su usuario: ")
            psw = input("Indique su contraseña: ")

            if user == usuario and psw == pswd:
                opAdmin = -1
                while opAdmin != 0:
                    try:
                        opAdmin = int(input(menu_views.menu_admin()))
                        if opAdmin == 1:
                            parking_views.estado_parking(plazas, reservadas_id)

                        elif opAdmin == 2:
                            print("Indique la primera fecha: ")
                            fecha1 = admin_service.generar_fecha()
                            if isinstance(fecha1, datetime):
                                print("Indique la segunda fecha: ")
                                fecha2 = admin_service.generar_fecha()
                                if isinstance(fecha2, datetime):
                                    print(
                                        f"{fecha1.strftime('%d/%m/%Y, %H:%M')} - {fecha2.strftime('%d/%m/%Y, %H:%M')}\n")
                                    parking_views.mostrar_facturacion(
                                        admin_service.obtener_facturacion(fecha1, fecha2, cobros))

                        elif opAdmin == 3:
                            parking_views.buscar_abonados(clientes)

                        elif opAdmin == 4:
                            opAbono = -1
                            while opAbono != 0:
                                try:
                                    opAbono = int(input(menu_views.menu_abono()))
                                    if opAbono == 1:
                                        try:
                                            tipo_a = int(input(menu_views.menu_tipo_abono()))
                                            tipo_abono = admin_service.elegir_tipo_abono(tipo_a)
                                            if tipo_abono != "":
                                                matricula = input("Introduzca su matrícula (1234ABC): ").upper()
                                                if validar_service.comprobar_matricula_existe(matricula, plazas,
                                                                                              clientes):
                                                    try:
                                                        tipo_v = int(input(menu_views.menu_tipo_vehiculo()))
                                                        tipo_vehiculo = admin_service.elegir_tipo_vehiculo(tipo_v)
                                                        if tipo_vehiculo != "":
                                                            v = Vehiculo(matricula, tipo_vehiculo)
                                                            dni = input("Indique su DNI (12345678A): ").upper()
                                                            if validar_service.comprobar_dni_existe(dni, clientes):
                                                                plaza = admin_service.reservar_plaza(
                                                                    tipo_vehiculo, plazas, reservadas_id)
                                                                if plaza is not None:
                                                                    abono = Abono(tipo_abono, plaza)
                                                                    nombre = input("Indique su nombre: ")
                                                                    apellidos = input("Indique sus apellidos: ")
                                                                    num_tarjeta = input("Indique su número de cuenta: ")
                                                                    email = input("Indique su email: ")
                                                                    cliente = admin_service.nuevo_cliente_abono(
                                                                        v, nombre, apellidos, dni, num_tarjeta, email,
                                                                        abono, clientes, cobros_abono)
                                                                    print(f"{cliente}\n-Plaza {plaza.id_plaza}")
                                                                else:
                                                                    print("No hay plazas disponibles para reservar.")
                                                            else:
                                                                print("\nDNI existente o erróneo.")
                                                        else:
                                                            print("Tipo de vehículo incorrecto.")
                                                    except ValueError:
                                                        print("\nError, introduzca un número.")
                                                else:
                                                    print("\nMatricula existente o errónea.")
                                            else:
                                                print("Tipo de abono incorrecto.")
                                        except ValueError:
                                            print("\nError, introduzca un número.")

                                    elif opAbono == 2:
                                        opModif = -1
                                        dni = input("Indique su DNI (12345678A): ").upper()
                                        cliente_dni = admin_service.buscar_cliente_dni(dni, clientes)
                                        if cliente_dni is not None:
                                            cliente, indice_cliente = cliente_dni
                                            while opModif != 0:
                                                try:
                                                    opModif = int(input(menu_views.menu_modificar_abono()))
                                                    if opModif == 1:
                                                        opDato = -1
                                                        while opDato != 0:
                                                            try:
                                                                opDato = int(input(menu_views.menu_opcion_dato()))
                                                                if 0 < opDato < 5:
                                                                    cliente_mod = admin_service.modificar_cliente(
                                                                        cliente, opDato, clientes, indice_cliente,
                                                                        plazas)
                                                                    print(cliente_mod)
                                                                elif opDato == 0:
                                                                    print("Saliendo...")
                                                                else:
                                                                    print("Opción incorrecta.")
                                                            except ValueError:
                                                                print("\nError, introduzca un número.")
                                                    elif opModif == 2:
                                                        try:
                                                            tipo_a = int(input(menu_views.menu_tipo_abono()))
                                                            tipo_abono = admin_service.elegir_tipo_abono(tipo_a)
                                                            if tipo_abono != "":
                                                                parking_views.mostrar_nuevo_abono(
                                                                    admin_service.renovar_abono(
                                                                        cliente, tipo_abono, clientes, cobros_abono))
                                                            else:
                                                                print("Tipo de abono incorrecto.")
                                                        except ValueError:
                                                            print("\nError, introduzca un número.")

                                                    elif opModif == 0:
                                                        print("Saliendo...")
                                                    else:
                                                        print("Opción incorrecta.")
                                                except ValueError:
                                                    print("\nError, introduzca un número.")
                                        else:
                                            print("\nNo se ha encontrado el cliente.")

                                    elif opAbono == 3:
                                        dni = input("Indique su DNI (12345678A): ").upper()
                                        cliente_dni = admin_service.buscar_cliente_dni(dni, clientes)
                                        if cliente_dni is not None:
                                            cliente = cliente_dni[0]
                                            admin_service.baja_abonado(cliente, clientes, plazas, reservadas_id)
                                            print("\nAbono eliminado correctamente.")
                                        else:
                                            print("\nNo se ha encontrado el cliente.")

                                    elif opAbono == 0:
                                        print("Saliendo...")
                                    else:
                                        print("Opción incorrecta.")
                                except ValueError:
                                    print("\nError, introduzca un número.")

                        elif opAdmin == 5:
                            opCad = -1
                            while opCad != 0:
                                try:
                                    opCad = int(input(menu_views.menu_caducidad()))
                                    if opCad == 1:
                                        mes = 0
                                        while mes < 1 or mes > 13:
                                            try:
                                                mes = int(input("Indique el mes: "))
                                                parking_views.mostrar_abonados(
                                                    admin_service.buscar_clientes_cad(mes, clientes, opCad))
                                            except ValueError:
                                                print("\nError, introduzca un número.")

                                    elif opCad == 2:
                                        parking_views.mostrar_abonados(
                                            admin_service.buscar_clientes_cad(0, clientes, opCad))
                                    elif opCad == 0:
                                        print("Saliendo...")
                                    else:
                                        print("Opción incorrecta.")
                                except ValueError:
                                    print("\nError, introduzca un número.")
                        elif opAdmin == 0:
                            print("Saliendo...")
                        else:
                            print("Opción incorrecta.")
                    except ValueError:
                        print("\nError, introduzca un número.")
            else:
                print("\nUsuario y/o contraseña errónea.")

        elif opZona == 3:
            opView = -1
            while opView != 0:
                try:
                    opView = int(input(menu_views.menu_pruebas()))
                    pruebas.mostrar_info(opView, clientes, plazas, reservadas_id, cobros, cobros_abono)
                except ValueError:
                    print("Error, introduzca un número.")
        elif opZona == 0:
            print("Saliendo...")
        else:
            print("Opción incorrecta.")
    except ValueError:
        print("\nError, introduzca un número.")

print("\n¡Muchas gracias, vuelva pronto!")
