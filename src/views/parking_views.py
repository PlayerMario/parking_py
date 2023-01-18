from models.ocupada import Ocupada


class ParkingViews:
    def mostrar_disponibles(self, num_turismo, num_moto, num_mov_red):
        return f"""\t\t\t\tPLAZAS DISPONIBLES:
                ==========================
                -TURISMOS: {num_turismo}
                -MOTOCICLETAS: {num_moto}
                -MOVILIDAD REDUCIDA: {num_mov_red}"""

    def mostrar_ticket(self, plaza):
        if isinstance(plaza.ocupada, Ocupada):
            print(f"""
                    ==================================
                    | ·PLAZA: {plaza.id_plaza}\t\t\t\t\t\t |
                    | ·MATRÍCULA: {plaza.ocupada.cliente.vehiculo.matricula}\t\t\t |
                    | ·ENTRADA: {plaza.ocupada.fecha_deposito.strftime('%d/%m/%Y, %H:%M')}\t |
                    | ·PIN: {plaza.ocupada.pin}\t\t\t\t\t |
                    ==================================
                    """)
        else:
            print(f"La operación no ha podido completarse.")