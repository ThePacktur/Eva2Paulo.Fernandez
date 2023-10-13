from Libro import Libro

def ver_menu():
    libro = Libro("Entrevista Con un vampiro", "Anne Rice", "05/Mayo/1976")
    
    while True:
        
        print("--------Menu--------")
        print(" 1 Prestastamo de libro")
        print(" 2 Devolucion del libro")
        print(" 3 ver informacion del libro")
        print(" 4 Obtener informacion actual del libro")
        print(" 5 Actualizar informacion del libro")
        print(" 6 Salir")
        print("-------------------------")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            libro.prestar()
        elif opcion == "2":
            libro.devolver()
        elif opcion == "3":
            if libro.estado_prestado():
                print("El libro se encuentra disponible")
            else: 
                print("El libro no se encuentra disponible")
            
        elif opcion == "4":
            print(libro.obtener_informacion())
        elif opcion == "5":
            libro.cambiar_informacion()
        elif opcion == "6":
            print("Muchas gracias por usar el programa ¡Hasta luego!")
            break
        else: 
            print("Opcion ingresada no es valida, por favor intente con una opcion valida.")

ver_menu()
