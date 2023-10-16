from Biblioteca import Biblioteca
from Libro import Libro

biblioteca = Biblioteca()

libro1 = Libro("Entrevista Con un vampiro", "Anne Rice", 1976)
libro2 = Libro("Lestat el Vampiro", "Anne Rice", 1985)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro3)

def menu(biblioteca):
    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Listar libros")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            anio = int(input("Ingrese el año de publicación del libro: "))
            libro = Libro(titulo, autor, anio)
            biblioteca.agregar_libro(libro)
            print(f'Se ha agregado el libro "{titulo}" a la biblioteca.')
        elif opcion == '2':
            titulo = input("Ingrese el título del libro que desea buscar: ")
            print(biblioteca.buscar_libro(titulo))
        elif opcion == '3':
            titulo = input("Ingrese el título del libro que desea prestar: ")
            print(biblioteca.prestar_libro(titulo))
        elif opcion == '4':
            titulo = input("Ingrese el título del libro que desea devolver: ")
            print(biblioteca.devolver_libro(titulo))
        elif opcion == '5':
            print("Lista de libros en la biblioteca:")
            biblioteca.listar_libros()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

menu(biblioteca)