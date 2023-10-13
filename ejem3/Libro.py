class Libro:
    def __init__(self,titulo:str,autor:str,anio_publicacion:int,disponible:bool):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__disponible = disponible

        