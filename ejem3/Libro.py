class Libro:
    def __init__(self, titulo:str, autor:str, anio_publicacion:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__disponible = True

    def set_titulo(self, titulo:str):
         self.__titulo = titulo
    
    def set_autor(self, autor:str):
         self.__autor = autor

    def set_anio_publicacion(self, anio_publicacion:int):
         self.__anio_publicacion = anio_publicacion

    def set_disponible(self, disponible: bool):
         self.__disponible = disponible

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor

    def get_anio_publicacion(self):
        return self.__anio_publicacion

    def get_disponible(self):
        return self.__disponible

    def disponible(self, valor):
        self.__disponible = valor
    
    def __str__(self) -> str:
        txt = f"\nTitulo: {self.__titulo}"
        txt += f"\nAutor: {self.__autor}"
        txt += f"\nAnio publicacion: {self.__anio_publicacion}"
        txt += f'\n Disponible: {"Si" if self.disponible else "NO"}'
        return txt