class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id_usuario = id_usuario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apeliido):
        self.__apellido = apellido

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def mostrar_info(self):
        print("nombre: ", self.__nombre)
        print("apellido: ", self.__apellido)
        print("id_usuario: ",self.__id_usuario)