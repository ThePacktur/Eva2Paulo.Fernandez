class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.disponible and libro.titulo == titulo:
                return f'El libro "{libro.titulo}" está disponible para préstamo.'
        return f'El libro "{titulo}" no está disponible para préstamo.'

    def prestar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.disponible and libro.titulo == titulo:
                libro.disponible = False
                return f'Se ha prestado el libro "{libro.titulo}".'
        return f'No se puede prestar el libro "{titulo}".'

    def devolver_libro(self, titulo):
        for libro in self.lista_libros:
            if not libro.disponible and libro.titulo == titulo:
                libro.disponible = True
                return f'Se ha devuelto el libro "{libro.titulo}".'
        return f'No se puede devolver el libro "{titulo}".'

    def listar_libros(self):
        for libro in self.lista_libros:
            print(libro)
