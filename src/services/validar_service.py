from models.cliente_abono import ClienteAbono
from models.ocupada import Ocupada


class ValidarService:
    def validar_letra(self, letra):
        try:
            if isinstance(int(letra), int):
                return False
            else:
                return True
        except ValueError:
            return True

    def validar_dni(self, dni):
        try:
            if len(dni) == 9 and self.validar_letra(dni[-1]) and isinstance(int(dni[:8]), int):
                return True
            else:
                return False
        except ValueError:
            return False

    def comprobar_letras_matricula(self, matricula):
        for letra in list(matricula[-3:]):
            try:
                if isinstance(int(letra), int):
                    return False
            except ValueError:
                pass
        return True

    def validar_matricula(self, matricula):
        try:
            if len(matricula) == 7 and isinstance(int(matricula[:4]), int) and self.comprobar_letras_matricula(
                    matricula):
                return True
            else:
                return False
        except ValueError:
            return False

    def comprobar_dni_existe(self, dni, lista_clientes):
        dni = dni.upper()
        for cliente in lista_clientes:
            if isinstance(cliente, ClienteAbono) and cliente.dni.upper() == dni:
                return False
        return self.validar_dni(dni)

    def comprobar_matricula_existe(self, matricula, lista_plazas, lista_clientes):
        matricula = matricula.upper()
        for plaza in lista_plazas:
            if isinstance(plaza.ocupada, Ocupada) and plaza.ocupada.cliente.vehiculo.matricula.upper() == matricula:
                return False
        for cliente in lista_clientes:
            if isinstance(cliente, ClienteAbono) and cliente.vehiculo.matricula == matricula:
                return False
        return self.validar_matricula(matricula)
