from CuentaBancaria import CuentaBancaria 
from CuentaCorriente import CuentaCorriente

#Test
#cta1 = CuentaBancaria("Pedro", 15000)
#cta1.depositar(600)
#cta1.retirar(400)
#cta1.ver_saldo()
#Test2
#cta2 = CuentaCorriente("Gab",40000,15740)
#cta2.depositar(600)
#cta2.retiro(400)
#cta2.ver_saldo()
#cta2.ver_limite_sobregiro()

#MENU

def menu():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta_bancaria = CuentaBancaria(titular, saldo_inicial)
    cuenta_corriente = CuentaCorriente(titular, saldo_inicial)

    while True:
        print("\nMenú Principal:")
        print("1. Cuenta Bancaria")
        print("2. Cuenta Corriente")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_cuenta_bancaria(cuenta_bancaria)
        elif opcion == "2":
            menu_cuenta_corriente(cuenta_corriente)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")



def menu_cuenta_bancaria(cuenta_bancaria):
    while True:
        print("\nMenú de Cuenta Bancaria:")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(cuenta_bancaria.ver_saldo())
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta_bancaria.depositar(cantidad)
            print("Depósito exitoso.")
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta_bancaria.retirar(cantidad)
            print("Retiro exitoso.")
        elif opcion == "4":
            print("Saliendo del menú de Cuenta Bancaria.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_cuenta_corriente(cuenta_corriente):
    while True:
        print("\nMenú de Cuenta Corriente:")
        print("1. Ver saldo y sobregiro")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver límite de sobregiro")
        print("5. Modificar límite de sobregiro")
        print("6. Pagar sobregiro")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(cuenta_corriente)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta_corriente.depositar(cantidad)
            print("Depósito exitoso.")
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta_corriente.retirar(cantidad)
            print("Retiro exitoso.")
        elif opcion == "4":
            print(cuenta_corriente.ver_limite_sobregiro())
        elif opcion == "5":
            nuevo_limite = float(input("Ingrese el nuevo límite de sobregiro: "))
            cuenta_corriente.modificar_limite_sobregiro(nuevo_limite)
            print("Límite de sobregiro modificado.")
        elif opcion == "6":
            cantidad = float(input("Ingrese la cantidad a pagar del sobregiro: "))
            cuenta_corriente.pagar_sobregiro(cantidad)
            print("Pago de sobregiro exitoso.")
        elif opcion == "7":
            print("Saliendo del menú de Cuenta Corriente.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
menu()
menu_cuenta_bancaria()
menu_cuenta_corriente()
