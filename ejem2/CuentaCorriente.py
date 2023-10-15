from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular: str, saldo_inicial: float,sobregiro:float):
        super().__init__(nombre_titular, saldo_inicial)
        self.__sobregiro = sobregiro
    
    def retiro(self,valor: float):
        if valor <= self.get_saldo_inicial + self.__sobregiro:
            if valor <= self.get_saldo_inicial:
                super().get_saldo_inicial -= valor
            else:
                self.__sobregiro -= valor -self.get_saldo_inicial
                self.get_saldo_inicial = 0
        else:
            print("saldo insuficiente, se encuentra sobregirado.")

    def ver_limite_sobregiro(self):
        print(f"\nSaldo insuficiente:{self.__sobregiro}")

    def modificar_limite_sobregiro(self, new_limit: float):
        self.__sobregiro = new_limit
        

    def pagar_sobregiro(self, valor:float):
        if valor <= self.get_saldo_inicial:
            self.get_saldo_inicial -= valor
            self.__sobregiro += valor
            print(f"\nSe ha realizado el pago del sobregiro: ${self.pagar_sobregiro()}")
        else:
            print("Saldo insuficiente en la cuenta.")
        
    #def ver_sobregiro(self):
    #    print(f"\nsobregiro: {self.__sobregiro}")
