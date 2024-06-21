class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    def get_libro(self):
        return self.__libro

    def set_libro(self, libro):
        self.__libro = libro

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def set_fecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        print("Libro:", self.__libro.get_titulo())
        print("Usuario:", self.__usuario.get_nombre())
        print("Fecha de préstamo:", self.__fecha_prestamo)
        print("Fecha de devolución:", self.__fecha_devolucion)
