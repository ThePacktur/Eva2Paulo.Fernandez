from Libro import Libro

def menu():
    libro = Libro("Entrevista Con un vampiro", "Anne Rice", "05/Mayo/1976")
    while True:
        print("--------Menu--------")
        print("1 Prestastamo de libro")
        print("2 Devolucion del libro")
        print(" 3 Actualizar informacion del libro")
        print(" 4 Obtener informacion actual del libro")
        print()

