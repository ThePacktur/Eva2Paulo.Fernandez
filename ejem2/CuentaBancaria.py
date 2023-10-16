class CuentaBancaria:
    def __init__(self,nombre_titular:str,saldo_inicial=0):
        self.__nombre_titular = nombre_titular
        self.__saldo_inicial = saldo_inicial
   
    def set_saldo_inicial(self,saldo_inicial: float):
        self.__saldo_inicial = saldo_inicial

    def get_nombre_titular(self):
        return self.__nombre_titular

    def get_saldo_inicial(self):
        return self.__saldo_inicial
    
    def depositar(self,valor:float):
        if valor > 0:
            self.__saldo_inicial += valor

    def retirar(self,valor:float):
        if valor > 0 and self.__saldo_inicial >= valor:
            self.__saldo_inicial -= valor
        
        else:    
            print("no ahi suficiente saldo en la cuenta.")

    def ver_saldo(self):
        print("Bienvenido al Programa de calculo de saldo e interes del Banco virtual.")
        print(f"\nTitular de la cuenta: {self.__nombre_titular}")
        print(f"\nSaldo inicial: {self.__saldo_inicial}")
       

  
    def __str__(self):
        txt =  (f"Titular Cuenta: {self.__nombre_titular}")
        txt += (f"\nSaldo inicial  Cta Bancaria: {self.__saldo_inicial}")
        txt += (f"\nDepositar: {self.depositar}")
        txt += (f"\nGiro: {self.retirar}")
        return txt
    
    
        