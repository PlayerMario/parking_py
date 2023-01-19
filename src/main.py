from datetime import datetime
from data.data import Data
from models.abono import Abono
from models.cliente import Cliente
from models.cliente_abono import ClienteAbono
from models.cobros_abono import CobroAbono
from models.vehiculo import Vehiculo
from services.admin_service import AdminService
from services.clientes_service import ClienteService
from views.menu_views import MenuViews
from views.parking_views import ParkingViews

# CARGAR DATOS INICIALES:
menu_views = MenuViews()
parking_views = ParkingViews()
cliente_service = ClienteService()
admin_service = AdminService()
data = Data()
clientes = data.cargar_clientes()
cobros_abono = data.cargar_cobros_abono()
cobros = data.cargar_cobros()
reservadas = data.cargar_reservadas()
vehiculos = data.cargar_vehiculos()
abonos = data.cargar_abonos()
# ocupadas = data.cargar_ocupadas()
plazas = data.cargar_plazas()
plazas_reservadas = admin_service.cargar_plazas_reservadas_id(reservadas)

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opAbono = -1
opCad = -1
opModif = -1
opDato = -1
opTipo = -1
tipo_a = -1
tipo_v = -1
usuario = "admin"
pswd = "1234"

print("Bienvenido al Parking Triana.")

while opZona != 0:
    try:
        opZona = int(input(menu_views.menu_ppal()))
    except ValueError:
        print("\nError, introduzca un número.")
    if opZona == 1:
        opCliente = -1
        while opCliente != 0:
            try:
                opCliente = int(input(menu_views.menu_cliente()))
            except ValueError:
                print("\nError, introduzca un número.")
            if opCliente == 1:
                print(cliente_service.mostrar_libres(plazas, plazas_reservadas)[3])
                try:
                    opTipo = int(input(menu_views.menu_tipo_vehiculo()))
                except ValueError:
                    print("\nError, introduzca un número.")
                tipo_vehiculo = cliente_service.devolver_tipo(opTipo, plazas, plazas_reservadas)
                if tipo_vehiculo != "":
                    matricula = input("Indique su matrícula: ")
                    v = Vehiculo(matricula, tipo_vehiculo)
                    vehiculos = v.actualizar_listado(vehiculos)
                    c = Cliente(v)
                    clientes = c.actualizar_listado(clientes)
                    plaza_depo = cliente_service.depositar_ocasional(plazas, c, plazas_reservadas)
                    if plaza_depo is not None:
                        plazas = plaza_depo[1]
                    parking_views.mostrar_ticket(plaza_depo[0])
                else:
                    print("Opción incorrecta / No hay plazas de ese tipo disponibles")

            elif opCliente == 2:
                matricula = input("Indique su matrícula: ")
                id_plaza = input("Indique la plaza: ")
                pin = input("Indique su pin: ")
                plaza = cliente_service.buscar_plaza(matricula, plazas, id_plaza, pin)
                salida = cliente_service.generar_cobro(plaza, cobros, plazas)
                if salida is not None:
                    cobros = salida[1]
                    plazas = salida[2]
                    print(salida[0])
                else:
                    print("\nError en la operación.")

            elif opCliente == 3:
                matricula = input("Indique su matrícula: ")
                dni = input("Indique su DNI: ")
                cliente = cliente_service.buscar_cliente(matricula, dni, clientes)
                if cliente is not None:
                    deposito = cliente_service.depositar_abonado(cliente, plazas)
                    if deposito is not None:
                        plazas = deposito[1]
                        parking_views.mostrar_ticket(deposito[0])
                else:
                    print("\nAbonado no encontrado.")

            elif opCliente == 4:
                matricula = input("Indique su matrícula: ")
                id_plaza = input("Indique la plaza: ")
                pin = input("Indique su pin: ")
                plaza = cliente_service.buscar_plaza(matricula, plazas, id_plaza, pin)
                salida = cliente_service.salida_vehiculo(plaza, plazas)
                if salida is not None:
                    plazas = salida[1]
                    print(salida[0])
                else:
                    print("\nAbonado no encontrado.")

            elif opCliente == 0:
                print("Saliendo...")
            else:
                print("Opción incorrecta.")

    elif opZona == 2:
        user = input("Indique su usuario: ")
        psw = input("Indique su contraseña: ")

        if user == usuario and psw == pswd:
            opAdmin = -1
            while opAdmin != 0:
                try:
                    opAdmin = int(input(menu_views.menu_admin()))
                except ValueError:
                    print("\nError, introduzca un número.")

                if opAdmin == 1:
                    parking_views.estado_parking(plazas, plazas_reservadas)
                    print(cliente_service.mostrar_libres(plazas, plazas_reservadas)[3])

                elif opAdmin == 2:
                    print("Indique la primera fecha: ")
                    fecha1 = admin_service.generar_fecha()
                    if isinstance(fecha1, datetime):
                        print("Indique la segunda fecha: ")
                        fecha2 = admin_service.generar_fecha()
                        if isinstance(fecha2, datetime):
                            print(f"{fecha1.strftime('%d/%m/%Y, %H:%M')} - {fecha2.strftime('%d/%m/%Y, %H:%M')}\n")
                            parking_views.mostrar_facturacion(admin_service.obtener_facturacion(fecha1, fecha2, cobros))

                elif opAdmin == 3:
                    parking_views.buscar_abonados(clientes)

                elif opAdmin == 4:
                    opAbono = -1
                    while opAbono != 0:
                        try:
                            opAbono = int(input(menu_views.menu_abono()))
                        except ValueError:
                            print("\nError, introduzca un número.")

                        if opAbono == 1:
                            try:
                                tipo_a = int(input(menu_views.menu_tipo_abono()))
                            except ValueError:
                                print("\nError, introduzca un número.")
                            tipo_abono = admin_service.elegir_tipo_abono(tipo_a)
                            if tipo_abono != "":
                                matricula = input("Introduzca su matrícula: ")
                                try:
                                    tipo_v = int(input(menu_views.menu_tipo_vehiculo()))
                                except ValueError:
                                    print("\nError, introduzca un número.")
                                tipo_vehiculo = admin_service.elegir_tipo_vehiculo(tipo_v)
                                if tipo_vehiculo != "":
                                    v = Vehiculo(matricula, tipo_vehiculo)
                                    vehiculos = v.actualizar_listado(vehiculos)
                                    reserva = admin_service.reservar_plaza(tipo_vehiculo, plazas, plazas_reservadas,
                                                                           reservadas)
                                    if reserva is not None:
                                        plaza = reserva[0]
                                        reservadas = reserva[1]
                                        plazas_reservadas = reserva[2]
                                        abono = Abono(tipo_abono, plaza)
                                        abono.actualizar_listado(abonos)

                                        nombre = input("Indique su nombre: ")
                                        apellidos = input("Indique sus apellidos: ")
                                        dni = input("Indique su DNI: ")
                                        num_tarjeta = input("Indique su número de cuenta: ")
                                        email = input("Indique su email: ")

                                        c = ClienteAbono(v, nombre, apellidos, dni, num_tarjeta, email, abono)
                                        c.actualizar_listado(clientes)
                                        cobro_abono = CobroAbono(c.vehiculo.matricula, c.abono.fecha_alta,
                                                                 c.abono.fecha_cancelacion, c.abono.precio,
                                                                 c.num_tarjeta)
                                        cobro_abono.actualizar_listado(cobros_abono)
                                        print(f"{c}\n-Plaza {plaza.id_plaza}")
                                    else:
                                        print("No hay plazas disponibles para reservar.")
                                else:
                                    print("Tipo de vehículo incorrecto.")
                            else:
                                print("Tipo de abono incorrecto.")

                        elif opAbono == 2:
                            opModif = -1
                            dni = input("Indique su DNI: ")
                            cliente_dni = admin_service.buscar_cliente_dni(dni, clientes)
                            if cliente_dni is not None:
                                cliente = cliente_dni[0]
                                indice_cliente = cliente_dni[1]
                                while opModif != 0:
                                    try:
                                        opModif = int(input(menu_views.menu_modificar_abono()))
                                    except ValueError:
                                        print("\nError, introduzca un número.")
                                    if opModif == 1:
                                        opDato = -1
                                        while opDato != 0:
                                            try:
                                                opDato = int(input(menu_views.menu_opcion_dato()))
                                            except ValueError:
                                                print("\nError, introduzca un número.")
                                            cliente_mod = admin_service.modificar_cliente(cliente, opDato, clientes,
                                                                                          indice_cliente, plazas)
                                            if cliente_mod is not None and cliente_mod[2] is not None:
                                                clientes = cliente_mod[1]
                                                plazas = cliente_mod[2]
                                                print(cliente_mod[0])
                                            elif opDato == 0:
                                                print("Saliendo...")
                                            else:
                                                print("Opción incorrecta.")

                                    elif opModif == 2:
                                        try:
                                            tipo_a = int(input(menu_views.menu_tipo_abono()))
                                        except ValueError:
                                            print("\nError, introduzca un número.")
                                        tipo_abono = admin_service.elegir_tipo_abono(tipo_a)
                                        if tipo_abono != "":
                                            reno = admin_service.renovar_abono(cliente, tipo_abono, clientes, abonos,
                                                                               cobros_abono)
                                            abonos = reno[2]
                                            clientes = reno[3]
                                            cobros_abono = reno[4]
                                            print(reno[0])
                                            print(reno[1])
                                        else:
                                            print("Tipo de abono incorrecto.")

                                    elif opModif == 0:
                                        print("Saliendo...")
                                    else:
                                        print("Opción incorrecta.")
                            else:
                                print("No se ha encontrado el cliente.")

                        elif opAbono == 3:
                            dni = input("Indique su DNI: ")
                            cliente_dni = admin_service.buscar_cliente_dni(dni, clientes)
                            if cliente_dni is not None:
                                cliente = cliente_dni[0]
                                baja = admin_service.baja_abonado(cliente, clientes, abonos, plazas, plazas_reservadas,
                                                                  reservadas)

                                # REPASAR ESTE Y SI SE ACTUALIZA TO-DO. ACTUALIZAR LISTAS????

                                print("Abono eliminado correctamente.")
                            else:
                                print("No se ha encontrado el cliente.")

                        elif opAbono == 0:
                            print("Saliendo...")
                        else:
                            print("Opción incorrecta.")

                elif opAdmin == 5:
                    opCad = -1
                    while opCad != 0:
                        try:
                            opCad = int(input(menu_views.menu_caducidad()))
                        except ValueError:
                            print("\nError, introduzca un número.")
                        if opCad == 1:
                            mes = 0
                            while mes < 1 or mes > 13:
                                try:
                                    mes = int(input("Indique el mes: "))
                                except ValueError:
                                    print("\nError, introduzca un número.")
                                parking_views.mostrar_abonados(admin_service.buscar_clientes_cad(mes, clientes, opCad))

                        elif opCad == 2:
                            parking_views.mostrar_abonados(admin_service.buscar_clientes_cad(0, clientes, opCad))
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
