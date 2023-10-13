class CuentaBancaria:
    def __init__(self,nombre_titular:str,saldo_inicial:float):
        self.__nombre_titular = nombre_titular
        self.__saldo_inicial = saldo_inicial

    def depositar(self,valor:float):
        tot = self.__saldo_inicial + valor
        self.__saldo_inicial(tot)
        print(f"se realizo el deposito de : ${valor}")
        print(f"ahora dispones de : ${self.__saldo_inicial()}")
    
    def retirar(self,valor:float):
        if valor <= self.__saldo_inicial:
            self.__saldo_inicial - valor
        else:    
            print("no ahi suficiente saldo en la cuenta.")

    def ver_saldo(self):
        print(f"\nTitular de la cuenta: {self.__nombre_titular}")
        print(f"\nSaldo inicial: {self.__saldo_inicial}")
        print(f"\nDeposito: {self.depositar()}")
        print(f"\nGiro: {self.retirar()}")
        

    
        