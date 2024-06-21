class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    def get_libros(self):
        return self.__libros

    def set_libros(self, libros):
        self.__libros = libros

    def get_usuarios(self):
        return self.__usuarios

    def set_usuarios(self, usuarios):
        self.__usuarios = usuarios

    def get_prestamos(self):
        return self.__prestamos

    def set_prestamos(self, prestamos):
        self.__prestamos = prestamos

    def registrar_libro(self, libro):
        self.__libros.append(libro)

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def realizar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)

    def devolver_libro(self, prestamo):
        self.__prestamos.remove(prestamo)

    def mostrar_libros(self):
        for libro in self.__libros:
            print(libro.mostrar_info())