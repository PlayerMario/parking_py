from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada


class PruebasView:
    def mostrar_info(self, opcion, lista_clientes, lista_plazas, lista_id_plaza, lista_cobros, lista_cobros_abono):
        if opcion == 1:
            for c in lista_clientes:
                if isinstance(c, ClienteAbono):
                    print(f"·{c.nombre} {c.apellidos} -> DNI: {c.dni} -> {c.vehiculo.matricula} - {c.vehiculo.tipo}"
                          f" -> {c.abono.tipo} -> PIN: {c.abono.pin} -> Plaza: {c.abono.plaza.id_plaza}")
                else:
                    print(f"·{c.vehiculo.matricula} - {c.vehiculo.tipo}")

        elif opcion == 2:
            for p in lista_plazas:
                if isinstance(p.ocupada, Ocupada):
                    if isinstance(p.ocupada.cliente, ClienteAbono):
                        print(f"·Plaza {p.id_plaza} -> {p.tipo_vehiculo} -> {p.ocupada.cliente.nombre} "
                              f"{p.ocupada.cliente.apellidos} -> PIN: {p.ocupada.cliente.abono.pin} -> "
                              f"{p.ocupada.cliente.vehiculo.matricula} - {p.ocupada.cliente.vehiculo.tipo}")
                    else:
                        print(f"·Plaza {p.id_plaza} -> {p.tipo_vehiculo} -> {p.ocupada.cliente.vehiculo.matricula} -> "
                              f"{p.ocupada.cliente.vehiculo.tipo} -> PIN: {p.ocupada.pin}")
                else:
                    print(f"·Plaza {p.id_plaza} -> {p.tipo_vehiculo}")
        elif opcion == 3:
            for i in lista_id_plaza:
                print(f"·Plaza {i}")
        elif opcion == 4:
            total = 0
            for c in lista_cobros:
                print(f"·{c.matricula} -> {c.fecha_entrada.strftime('%d/%m/%Y, %H:%M')} -> "
                      f"{c.fecha_salida.strftime('%d/%m/%Y, %H:%M')} -> {c.cobro}€")
                total += c.cobro
            print(f"·TOTAL: {round(total, 2)}€")
        elif opcion == 5:
            total = 0
            for c in lista_cobros_abono:
                print(f"·{c.matricula} -> {c.fecha_entrada.strftime('%d/%m/%Y, %H:%M')} -> "
                      f"{c.fecha_salida.strftime('%d/%m/%Y, %H:%M')} -> {c.cobro}€")
                total += c.cobro
            print(f"·TOTAL: {round(total, 2)}€")
        elif opcion == 0:
            print("Saliendo...")
