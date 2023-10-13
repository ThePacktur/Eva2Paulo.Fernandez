class Libro:
    def __init__(self,titulo:str,autor:str,anio:str):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__prestamo = False
    
    def get_prestamo(self):
        return self.__prestamo

    def prestar(self):
        if self.__prestamo:
            print("El libro no es encuentra disponible, vuelva mas tarde.")
        
        else:
            self.__prestamo = True
    def set_titulo(self,titulo):
        self.__titulo = titulo

    def set_autor(self,autor):
        self.__autor = autor

    def set_anio(self,anio):
        self.__anio = anio

    def devolver(self):
        devo = self.__prestamo = False
        return devo
    
    def estado_prestado(self):
        prestamo = self.__prestamo
        return prestamo

    def obtener_informacion(self):
        estado_libro = f"\nSe encuentra Prestado: " if self.__prestamo else "Se encuetra Disponible"
        info_libro = f"\nTitulo: {self.__titulo}\nAutor : {self.__autor}\nAnio de publicacion: {self.__anio}\nEstado del Libro: {estado_libro}"
        return info_libro

    def cambiar_informacion(self):
        cambio_titulo = input("Ingrese el nuevo Titulo: ")
        cambio_autor = input("Ingrese El nuevo Autor: ")
        cambio_anio = input("ingrese el nuevo anio de publicacion: ")
        self.set_titulo = cambio_titulo
        self.set_autor = cambio_autor
        self.set_anio = cambio_anio