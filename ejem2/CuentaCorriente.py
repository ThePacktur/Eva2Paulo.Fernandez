from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular: str, saldo_inicial= 0, sobregiro = 0):
        super().__init__(nombre_titular, saldo_inicial)
        self.__sobregiro = sobregiro
        
    
    def set_sobregiro(self,sobregiro:float):
        self.__sobregiro = sobregiro

    def get_sobregiro(self):
        return self.__sobregiro

    def retirar(self, valor):
        if valor > 0:
            if self.get_saldo_inicial() >= valor:
                self.set_saldo_inicial(self.get_saldo_inicial() - valor)
            elif (self.get_saldo_inicial() + self.get_sobregiro()) >= valor:
                self.set_sobregiro(self.get_sobregiro() - (valor - self.get_saldo_inicial()))
                self.get_saldo_inicial(0)
        else:
            print("saldo insuficiente, se encuentra sobregirado.")

    def ver_limite_sobregiro(self):
        print(f"\nSaldo insuficiente:{self.__sobregiro}")

    def modificar_limite_sobregiro(self, new_limit: float):
        if new_limit >= 0:
            self.__sobregiro = new_limit
        

    def pagar_sobregiro(self, valor):
        if valor > 0 and self.get_saldo_inicial() >= valor:
            self.get_saldo_inicial(self.get_saldo_inicial() - valor)
            self.set_sobregiro(self.get_sobregiro() + valor)
            print(f"\nSe ha realizado el pago del sobregiro: ${valor}")
        else:
            print("Saldo insuficiente en la cuenta.")
        
    #def ver_sobregiro(self):
    #    print(f"\nsobregiro: {self.__sobregiro}")
    def __str__(self):
        txt = super().__str__()
        txt += f"\nSobreGiro: {self.__sobregiro}"
        return txt