class MenuViews:
    def menu_ppal(self):
        return "\nSeleccione una opción:\n[1] Acceso clientes.\n[2] Adminstración.\n[0] Salir.\n> "

    def menu_cliente(self):
        return "\nSeleccione una opción:\n[1] Depositar vehículo.\n[2] Retirar vehículo.\n[3] Depositar abonados." \
               "\n[4] Retirar abonados.\n[0] Salir.\n> "

    def menu_tipo_vehiculo(self):
        return "\nSeleccione el tipo:\n[1] Turismo.\n[2] Motocicleta.\n[3] Movilidad Reducida.\n> "

    def menu_admin(self):
        return "\nSeleccione una opción:\n[1] Estado del parking.\n[2] Facturación.\n[3] Consulta de abonados." \
               "\n[4] Gestión de abonos.\n[5] Caducidad de abonos.\n[0] Salir.\n> "

    def menu_abono(self):
        return "\nSeleccione una opción:\n[1] Nuevo abonado.\n[2] Modificación abonado.\n[3] Baja de abonado." \
               "\n[0] Salir.\n> "

    def menu_tipo_abono(self):
        return "\nSeleccione el tipo de abono:\n[1] Mensual (25€).\n[2] Trimestral (70€).\n[3] Semestral (130€)." \
               "\n[4] Anual (200€).\n> "

    def menu_modificar_abono(self):
        return "\nSeleccione una opción:\n[1] Datos del abonado.\n[2] Renovar abono.\n[0] Salir.\n> "

    def menu_opcion_dato(self):
        return "\nSeleccione una opción:\n[1] Nombre.\n[2] Apellidos.\n[3] Número de cuenta.\n[4] Email.\n[0] Salir\n> "

    def menu_caducidad(self):
        return "\nSeleccione una opción:\n[1] Caducidad en un mes.\n[2] Caducidad en próximos 10 días.\n[0] Salir.\n> "
