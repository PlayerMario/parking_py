from data.data import Data
from models.cliente import Cliente
from models.vehiculo import Vehiculo
from services.clientes_service import ClienteService
from views.menu_views import MenuViews
from views.parking_views import ParkingViews

# VARIABLES APLICACIÓN:
opZona = -1
opCliente = -1
opAdmin = -1
opAbono = -1
opCad = -1
opModif = -1
opDato = -1
usuario = "admin"
pswd = "1234"
data = Data()

parking = data.cargar_datos()[0]
clientes = data.cargar_datos()[1]
cobros_abono = data.cargar_datos()[2]
cobros = data.cargar_datos()[3]
reservadas = data.cargar_datos()[4]
vehiculos = data.cargar_datos()[5]
abonos = data.cargar_datos()[6]
ocupadas = data.cargar_datos()[7]
plazas = data.cargar_datos()[8]

menu_views = MenuViews()
parking_views = ParkingViews()
cliente_service = ClienteService()

plaza_no_dispo = []
for r in reservadas:
    plaza_no_dispo.append(r.id_plaza)

print("Bienvenido al Parking Triana.\n")

# MENÚ ZONA:
while opZona != 0:
    opZona = int(input(menu_views.menu_ppal()))
    if opZona == 1:
        opCliente = -1
        while opCliente != 0:
            opCliente = int(input(menu_views.menu_cliente()))
            if opCliente == 1:
                print(cliente_service.mostrar_libres(plazas, plaza_no_dispo)[3])
                opTipo = int(input(menu_views.menu_tipo_vehiculo()))
                tipo_vehiculo = cliente_service.devolver_tipo(opTipo, plazas, plaza_no_dispo)
                if tipo_vehiculo != "":
                    matricula = input("Indique su matrícula: ")
                    v = Vehiculo(matricula, tipo_vehiculo)
                    vehiculos = v.actualizar_listado(vehiculos)
                    c = Cliente(v)
                    clientes = c.actualizar_listado(clientes)
                    parking_views.mostrar_ticket(
                        cliente_service.depositar_ocasional(plazas, c, plaza_no_dispo))
                else:
                    print("Opción incorrecta / No hay plazas de ese tipo disponibles")

            elif opCliente == 2:
                matricula = input("Indique su matrícula: ")
                id_plaza = input("Indique la plaza: ")
                pin = input("Indique su pin: ")

                plaza = cliente_service.buscar_plaza(matricula, plazas, id_plaza, pin)
                # METER ESTO EN UN MÉTODO EN CLIENTE_CLIENTE
#                 if isinstance(plaza, Plaza):
#                     cobro = plaza.ocupada.salida_vehiculo()
#                     if isinstance(cobro, Cobro):
#                         Data.listaCobros.append(plaza.ocupada.salida_vehiculo())
#                     print(plaza.ocupada.salida_vehiculo())
#                     plaza.ocupada = None
#                 else:
#                     print("Error en la operación.")
#
#             elif opCliente == 3:
#                 matricula = input("Indique su matrícula: ")
#                 dni = input("Indique su DNI: ")
#
#                 cliente = ClienteAbono.buscar_cliente(None, matricula, dni, lista_clientes)
#                 if isinstance(cliente, ClienteAbono):
#                     parking.mostrar_ticket(parking.depositar_abonado(cliente))
#                 else:
#                     print("\nNo se ha encontrado cliente.")
#
#             elif opCliente == 4:
#                 matricula = input("Indique su matrícula: ")
#                 id_plaza = input("Indique la plaza: ")
#                 pin = input("Indique su pin: ")
#
#                 plaza = parking.buscar_plaza(matricula, id_plaza, pin)
#                 if isinstance(plaza, Plaza):
#                     print(plaza.ocupada.salida_vehiculo())
#                     plaza.ocupada = None
#
#             elif opCliente == 0:
#                 print("Saliendo...")
#
#             else:
#                 print("Opción incorrecta.")
#
#     elif opZona == 2:
#         # USUARIO Y CONTRASEÑA (admin - 1234)
#         user = input("\nIndique su usuario: ")
#         psw = input("Indique su contraseña: ")
#
#         # MENÚ ADMINISTRADOR
#         if user == usuario and psw == pswd:
#             opAdmin = -1
#             while opAdmin != 0:
#                 opAdmin = int(input("\nSeleccione una opción:\n[1] Estado del parking.\n[2] Facturación."
#                                     "\n[3] Consulta de abonados.\n[4] Abonos.\n[5] Caducidad de abonos."
#                                     "\n[0] Salir.\n> "))
#
#                 if opAdmin == 1:
#                     parking.estado_parking(lista_reservadas)
#
#                 elif opAdmin == 2:
#                     print("Indique la primera fecha: ")
#                     fecha1 = datetime(int(input("Indique el año: ")), int(input("Indique el mes: ")),
#                                       int(input("Indique el día: ")), int(input("Indique la hora: ")))
#
#                     print("Indique la segunda fecha: ")
#                     fecha2 = datetime(int(input("Indique el año: ")), int(input("Indique el mes: ")),
#                                       int(input("Indique el día: ")), int(input("Indique la hora: ")))
#
#                     print(f"{fecha1.strftime('%d/%m/%Y, %H:%M')} - {fecha2.strftime('%d/%m/%Y, %H:%M')}\n")
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
