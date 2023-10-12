from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular: str, saldo_inicial: float,sobregiro:float):
        super().__init__(nombre_titular, saldo_inicial)
        self.__sobregiro = sobregiro
    
    def ver_limite_sobregiro(self):
        pass

    def modificar_limite_sobregiro(self):
        pass

    def pagar_sobregiro(self):
        pass
    def ver_sobregiro(self):
        pass
    