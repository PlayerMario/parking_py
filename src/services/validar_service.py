from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada


class ValidarService:
    def validar_letra(self, letra):
        try:
            # Si la letra del DNI puede convertirse en int, quiere decir que es un número, no se valida
            if isinstance(int(letra), int):
                return False
            else:
                return True
        except ValueError:
            return True

    def validar_dni(self, dni):
        try:
            # Comprueba si la longitud es 9, que el último caracter sea una letra, y que los 8 primeros sean números
            if len(dni) == 9 and self.validar_letra(dni[-1]) and isinstance(int(dni[:8]), int):
                return True
            else:
                return False
        except ValueError:
            return False

    def comprobar_letras_matricula(self, matricula):
        for letra in list(matricula[-3:]):
            try:
                # Si cada una de los 3 últimos caracteres pueden convertirse en int, quiere decir que son números y
                # no letras, por lo que no se valida
                if isinstance(int(letra), int):
                    return False
            except ValueError:
                pass
        return True

    def validar_matricula(self, matricula):
        try:
            # Comprueba si la longitud es 7, que 3 los último caracteres sean letras, y que los 4 primeros sean números
            if len(matricula) == 7 and isinstance(int(matricula[:4]), int) and self.comprobar_letras_matricula(
                    matricula):
                return True
            else:
                return False
        except ValueError:
            return False

    def comprobar_dni_existe(self, dni, lista_clientes):
        dni = dni.upper()
        # Iterar la lista de clientes para ver si entre los abonados ya existe su DNI
        for cliente in lista_clientes:
            if isinstance(cliente, ClienteAbono) and cliente.dni.upper() == dni:
                return False
        # Si no coincide, comprobará que el formato del DNI está bien
        return self.validar_dni(dni)

    def comprobar_matricula_existe(self, matricula, lista_plazas, lista_clientes):
        matricula = matricula.upper()
        # Itera la lista de plazas para comprobar que está ocupada, y que la matrícula del vehículo que lo ocupa no sea
        # la misma que se está indicando, ya que ese vehículo ya está
        for plaza in lista_plazas:
            if isinstance(plaza.ocupada, Ocupada) and plaza.ocupada.cliente.vehiculo.matricula.upper() == matricula:
                return False
        # Itera la lista de clientes para comprobar que, de los abonados, su matrícula no coincida con la que se está
        # indicando
        for cliente in lista_clientes:
            if isinstance(cliente, ClienteAbono) and cliente.vehiculo.matricula == matricula:
                return False
        # Si no coincide, comprobará que el formato de la matrícula está bien
        return self.validar_matricula(matricula)
