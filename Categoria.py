class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_info(Self):
        print("nombre: ", self.__nombre)