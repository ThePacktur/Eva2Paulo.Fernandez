from CuentaBancaria import CuentaBancaria 
from CuentaCorriente import CuentaCorriente

#Test
cta1 = CuentaBancaria("Pedro", 15000)
cta1.depositar(600)
cta1.retirar(400)
cta1.ver_saldo()

cta2 = CuentaCorriente("Gab",40000,15740)
cta2.depositar(600)
cta2.retiro(400)
cta2.ver_saldo()
cta2.ver_limite_sobregiro()

