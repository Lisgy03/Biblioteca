class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__autor = autor
        self.__categoria = categoria

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def mostrar_info(self):
        print("titulo: ", self.__titulo)
        print("isbn: ", self.__isbn)
        print("autor: ", self.__autor)
        print("categoria: ", self.__categoria)
