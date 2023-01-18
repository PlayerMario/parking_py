from datetime import datetime

from data.data import Data
from models.cliente import Cliente
from models.vehiculo import Vehiculo
from services.admin_service import AdminService
from services.clientes_service import ClienteService
from views.menu_views import MenuViews
from views.parking_views import ParkingViews

# CARGAR DATOS INICIALES:
data = Data()
parking = data.cargar_parking()
clientes = data.cargar_clientes()
cobros_abono = data.cargar_cobros_abono()
cobros = data.cargar_cobros()
reservadas = data.cargar_reservadas()
vehiculos = data.cargar_vehiculos()
abonos = data.cargar_abonos()
# ocupadas = data.cargar_ocupadas()
plazas = data.cargar_plazas()

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opAbono = -1
opCad = -1
opModif = -1
opDato = -1
opTipo = -1
usuario = "admin"
pswd = "1234"
menu_views = MenuViews()
parking_views = ParkingViews()
cliente_service = ClienteService()
admin_service = AdminService()
plazas_reservadas = []
for r in reservadas:
    plazas_reservadas.append(r.id_plaza)

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
                    parking_views.mostrar_ticket(
                        cliente_service.depositar_ocasional(plazas, c, plazas_reservadas))
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
#
#                     Cobro.mostrar_facturacion(None, Cobro.obtener_facturacion(None, fecha1, fecha2, lista_cobros))
#
#                 elif opAdmin == 3:
#                     ClienteAbono.buscar_abonados(None, lista_clientes)
#
#                 elif opAdmin == 4:
#                     opAbono = -1
#                     while opAbono != 0:
#                         opAbono = int(input("\nSeleccione una opción:\n[1] Nuevo abonado.\n[2] Modificación abonado."
#                                             "\n[3] Baja de abonado.\n[0] Salir.\n> "))
#                         if opAbono == 1:
#                             tipo_a = int(
#                                 input("\nSeleccione el tipo de abono:\n[1] Mensual (25€).\n[2] Trimestral (70€)."
#                                       "\n[3] Semestral (130€).\n[4] Anual (200€).\n> "))
#                             if tipo_a == 1:
#                                 tipo_abono = "Mensual"
#                             elif tipo_a == 2:
#                                 tipo_abono = "Trimestral"
#                             elif tipo_a == 3:
#                                 tipo_abono = "Semestral"
#                             elif tipo_a == 4:
#                                 tipo_abono = "Anual"
#
#                             matricula = input("Introduzca su matrícula: ")
#                             tipo_v = int(
#                                 input("\nSeleccione el tipo de vehículo:\n[1] Turismo.\n[2] Motocicleta."
#                                       "\n[3] Movilidad Reducida.\n> "))
#                             if tipo_v == 1:
#                                 tipo_vehiculo = "Turismo"
#                             elif tipo_v == 2:
#                                 tipo_vehiculo = "Motocicleta"
#                             elif tipo_v == 3:
#                                 tipo_vehiculo = "Movilidad Reducida"
#
#                             vehiculo = Vehiculo(matricula, tipo_vehiculo)
#                             lista_vehiculos.append(vehiculo)
#
#                             plaza = parking.reservar_plaza(tipo_vehiculo, lista_reservadas)
#                             if isinstance(plaza, Plaza):
#                                 abono = Abono(tipo_abono, plaza)
#                                 lista_abonos.append(abono)
#
#                                 # CREACIÓN CLIENTE:
#                                 nombre = input("Indique su nombre: ")
#                                 apellidos = input("Indique sus apellidos: ")
#                                 dni = input("Indique su DNI: ")
#                                 num_tarjeta = input("Indique su número de cuenta: ")
#                                 email = input("Indique su email: ")
#                                 cliente = ClienteAbono(vehiculo, nombre, apellidos, dni, num_tarjeta, email, abono)
#                                 cobro_abono = CobroAbono(cliente.vehiculo.matricula, cliente.abono.fecha_alta,
#                                                          cliente.abono.fecha_cancelacion, cliente.abono.precio,
#                                                          cliente.num_tarjeta)
#                                 lista_clientes.append(cliente)
#                                 lista_cobros_abonados.append(cobro_abono)
#                                 print(cliente)
#                             else:
#                                 print("No hay plazas disponibles para reservar.")
#
#                         elif opAbono == 2:
#                             opModif = -1
#                             dni = input("Indique su DNI: ")
#                             cliente = ClienteAbono.buscar_cliente_dni(None, dni, lista_clientes)
#                             if isinstance(cliente, ClienteAbono):
#                                 while opModif != 0:
#                                     opModif = int(input("\nSeleccione una opción:\n[1] Datos del abonado.\n[2] "
#                                                         "Renovar abono.\n[0] Salir.\n> "))
#                                     if opModif == 1:
#                                         opDato = -1
#                                         while opDato != 0:
#                                             opDato = int(input("\nSeleccione una opción:\n[1] Nombre.\n[2] "
#                                                                "Apellidos.\n[3] Número de cuenta.\n[4] Email."
#                                                                "\n[0] Salir.\n> "))
#                                             if opDato == 1:
#                                                 nombre = input("Indique su nombre: ")
#                                                 cliente.nombre = nombre
#                                                 print(cliente)
#                                             elif opDato == 2:
#                                                 apellidos = input("Indique sus apellidos: ")
#                                                 cliente.apellidos = apellidos
#                                                 print(cliente)
#                                             elif opDato == 3:
#                                                 num_tarjeta = input("Indique su número de cuenta: ")
#                                                 cliente.num_tarjeta = num_tarjeta
#                                                 print(cliente)
#                                             elif opDato == 4:
#                                                 email = input("Indique su email: ")
#                                                 cliente.email = email
#                                                 print(cliente)
#                                             elif opDato == 0:
#                                                 print("Saliendo...")
#                                             else:
#                                                 print("Opción incorrecta.")
#                                     elif opModif == 2:
#                                         tipo_a = int(input("\nSeleccione el tipo de abono:\n[1] Mensual (25€)."
#                                                            "\n[2] Trimestral (70€).\n[3] Semestral (130€)."
#                                                            "\n[4] Anual (200€).\n> "))
#                                         if tipo_a == 1:
#                                             tipo_abono = "Mensual"
#                                         elif tipo_a == 2:
#                                             tipo_abono = "Trimestral"
#                                         elif tipo_a == 3:
#                                             tipo_abono = "Semestral"
#                                         elif tipo_a == 4:
#                                             tipo_abono = "Anual"
#                                         cliente.abono = Abono.renovar_abono(None, cliente.abono, tipo_abono)
#                                         lista_cobros_abonados.append(cliente.abono)
#                                         print(cliente, cliente.abono)
#                                     elif opModif == 0:
#                                         print("Saliendo...")
#                                     else:
#                                         print("Opción incorrecta.")
#                             else:
#                                 print("No se ha encontrado el cliente.")
#
#                         elif opAbono == 3:
#                             dni = input("Indique su DNI: ")
#                             cliente = ClienteAbono.buscar_cliente_dni(None, dni, lista_clientes)
#                             if isinstance(cliente, ClienteAbono):
#                                 cliente.abono.plaza.ocupada = None
#                                 lista_reservadas.remove(cliente.abono.plaza)
#                                 cliente.abono.plaza = None
#                                 cliente.__del__()
#                             else:
#                                 print("No se ha encontrado el cliente.")
#
#                         elif opAbono == 0:
#                             print("Saliendo...")
#
#                         else:
#                             print("Opción incorrecta.")
#
#                 elif opAdmin == 5:
#                     opCad = -1
#                     while opCad != 0:
#                         opCad = int(input("\nSeleccione una opción:\n[1] Caducidad en un mes.\n[2] Caducidad "
#                                           "en próximos 10 días.\n[0] Salir.\n> "))
#                         if opCad == 1:
#                             mes = 0
#                             while mes < 1 or mes > 13:
#                                 mes = int(input("Indique el mes: "))
#                             ClienteAbono.buscar_clientes_cad(None, mes, lista_clientes, opCad)
#
#                         elif opCad == 2:
#                             ClienteAbono.buscar_clientes_cad(None, 0, lista_clientes, opCad)
#
#                         elif opCad == 0:
#                             print("Saliendo...")
#
#                         else:
#                             print("Opción incorrecta.")
#
#                 elif opAdmin == 0:
#                     print("Saliendo...")
#
#                 else:
#                     print("Opción incorrecta.")
#
#         else:
#             print("\nUsuario y/o contraseña errónea.")
#
#     elif opZona == 0:
#         print("Saliendo...")
#
#     else:
#         print("Opción incorrecta.")
