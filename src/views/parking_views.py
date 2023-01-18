from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada


class ParkingViews:
    def mostrar_disponibles(self, num_turismo, num_moto, num_mov_red):
        return f"==========================\n\tPLAZAS DISPONIBLES:\n==========================\n-TURISMOS: " \
               f"{num_turismo}\n-MOTOCICLETAS: {num_moto}\n-MOVILIDAD REDUCIDA: {num_mov_red}" \
               f"\n=========================="

    def mostrar_ticket(self, plaza):
        if isinstance(plaza.ocupada, Ocupada):
            print(f"""
                    ==================================
                    | ·PLAZA: {plaza.id_plaza}\t\t\t\t\t |
                    | ·MATRÍCULA: {plaza.ocupada.cliente.vehiculo.matricula}\t\t\t |
                    | ·ENTRADA: {plaza.ocupada.fecha_deposito.strftime('%d/%m/%Y, %H:%M')}\t |
                    | ·PIN: {plaza.ocupada.pin}\t\t\t\t\t |
                    ==================================
                    """)
        else:
            print("La operación no ha podido completarse.")

    def estado_parking(self, lista_plazas, lista_reservadas):
        abonado = 0
        no_abonado = 0
        reservado = 0
        libre = 0
        for plaza in lista_plazas:
            if isinstance(plaza.ocupada, Ocupada):
                if isinstance(plaza.ocupada.cliente, ClienteAbono):
                    print("\n=============================\n\t\tCLIENTE ABONADO\n=============================")
                    print(plaza)
                    abonado += 1
                else:
                    print("\n=============================\n\tCLIENTE NO ABONADO\n=============================")
                    print(plaza)
                    no_abonado += 1
            elif plaza.id_plaza in lista_reservadas:
                print("\n=============================\n\t\tPLAZA RESERVADA\n=============================")
                print(plaza)
                reservado += 1
            else:
                print("\n=============================\n\t\tPLAZA LIBRE\n=============================")
                print(plaza)
                libre += 1

        print(f"==========================\n\t\tRESUMEN:\n==========================\n-Ocupadas Abonados: {abonado}"
              f"\n-Ocupadas Ocasionales: {no_abonado}\n-Reservadas: {reservado}\n-Libres: {libre}"
              f"\n==========================\n")

    def mostrar_facturacion(self, cobros):
        total = 0
        for fecha, cobro in cobros.items():
            print(f"\t· {fecha.strftime('%d/%m/%Y, %H:%M')} -> {cobro}€.")
            total += cobro
        print(f"\t===============================\n\t\tRecaudado: {round(total, 2)}€\n")
