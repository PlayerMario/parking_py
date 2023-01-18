class ParkingViews:
    def mostrar_disponibles(self, num_turismo, num_moto, num_mov_red):
        return f"""\t\t\t\tPLAZAS DISPONIBLES:
                ==========================
                -TURISMOS: {num_turismo}
                -MOTOCICLETAS: {num_moto}
                -MOVILIDAD REDUCIDA: {num_mov_red}"""