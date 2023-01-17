from models.cliente import Cliente


class ClienteAbono(Cliente):

    # CONSTRUCTOR
    def __init__(self, vehiculo, nombre, apellidos, dni, num_tarjeta, email, abono):
        super().__init__(vehiculo)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__num_tarjeta = num_tarjeta
        self.__email = email
        self.__abono = abono

    # GETTERS & SETTERS
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono

    # TOSTRING
    def __str__(self):
        return f"-{self.__nombre} {self.__apellidos}\n-DNI: {self.__dni}\n{self.vehiculo}"

    # MÉTODOS DE CLASE
    def buscar_cliente(self, matricula, dni, lista_clientes):
        salir = False
        cont = 0
        while not salir and cont != len(lista_clientes):
            cliente = lista_clientes[cont]
            if isinstance(cliente, ClienteAbono):
                if cliente.vehiculo.matricula == matricula and cliente.__dni == dni:
                    salir = True
                    return cliente
            cont += 1

    def buscar_abonados(self, lista_clientes):
        total = 0
        for cliente in lista_clientes:
            if isinstance(cliente, ClienteAbono):
                cliente.mostrar_abonados()
                total += cliente.__abono.precio
        print(f"===================================\n\n\tImporte total: {total}€")

    def mostrar_abonados(self):
        print(f"\n===================================\n"
              f"Abonado: {self.__nombre} {self.__apellidos}\nPlaza: {self.__abono.plaza.id_plaza}"
              f"\nTipo abono: {self.__abono.tipo}\nValidez hasta: "
              f"{self.__abono.fecha_cancelacion.strftime('%d/%m/%Y, %H:%M')}\nImporte: {self.__abono.precio}€")
