from tkinter import Tk, Label, Entry, Button, Frame, PhotoImage, font
from tkinter import messagebox
import os

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Socratica")

        self.bg_color = "#FDF5E6"
        self.label_color = "#8B4513"
        self.button_color = "#E3C565"
        self.button_hover_color = "#D1B46F"
        self.button_text_color = "#8B4513"
        self.entry_bg_color = "#FFF8DC"

        self.root.configure(background=self.bg_color)

        self.frame = Frame(root, bg=self.bg_color)
        self.frame.pack(padx=20, pady=20)

        image_path = os.path.join("C:/Users/Lisbeth cordero/IdeaProjects/Python/Gestion de Biblioteca", 'Biblioteca.png')
        self.image = PhotoImage(file=image_path)
        self.image_label = Label(self.frame, image=self.image, bg=self.bg_color)
        self.image_label.grid(row=0, columnspan=2, pady=(0, 20))

        font_style = font.Font(family="Helvetica", size=12, weight="bold")

        Label(self.frame, text="Nombre completo de Usuario:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=1, column=0, pady=5, sticky="w")
        self.usuario_entry = Entry(self.frame, bg=self.entry_bg_color)
        self.usuario_entry.grid(row=1, column=1, pady=5, padx=10)

        Label(self.frame, text="Número de Identificación:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=2, column=0, pady=5, sticky="w")
        self.id_entry = Entry(self.frame, bg=self.entry_bg_color)
        self.id_entry.grid(row=2, column=1, pady=5, padx=10)

        Label(self.frame, text="Nombre del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=3, column=0, pady=5, sticky="w")
        self.libro_entry = Entry(self.frame, bg=self.entry_bg_color)
        self.libro_entry.grid(row=3, column=1, pady=5, padx=10)

        Label(self.frame, text="Autor del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=4, column=0, pady=5, sticky="w")
        self.autor_entry = Entry(self.frame, bg=self.entry_bg_color)
        self.autor_entry.grid(row=4, column=1, pady=5, padx=10)

        Label(self.frame, text="Categoría del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=5, column=0, pady=5, sticky="w")
        self.categoria_entry = Entry(self.frame, bg=self.entry_bg_color)
        self.categoria_entry.grid(row=5, column=1, pady=5, padx=10)

        self.boton_prestamo = Button(self.frame, text="Realizar Préstamo", bg=self.button_color, fg=self.button_text_color, font=font_style, command=self.realizar_prestamo_ejemplo)
        self.boton_prestamo.grid(row=6, columnspan=2, pady=10)
        self.boton_prestamo.bind("<Enter>", self.on_enter)
        self.boton_prestamo.bind("<Leave>", self.on_leave)

        self.boton_mostrar_registros = Button(self.frame, text="Mostrar Registros", bg=self.button_color, fg=self.button_text_color, font=font_style, command=self.mostrar_registros)
        self.boton_mostrar_registros.grid(row=7, columnspan=2, pady=10)
        self.boton_mostrar_registros.bind("<Enter>", self.on_enter)
        self.boton_mostrar_registros.bind("<Leave>", self.on_leave)

        self.registros = []

    def on_enter(self, e):
        e.widget['background'] = self.button_hover_color

    def on_leave(self, e):
        e.widget['background'] = self.button_color

    def realizar_prestamo_ejemplo(self):
        nombre_usuario = self.usuario_entry.get()
        id_usuario = self.id_entry.get()
        nombre_libro = self.libro_entry.get()
        autor_libro = self.autor_entry.get()
        categoria_libro = self.categoria_entry.get()

        registro = {
            "Nombre de Usuario": nombre_usuario,
            "Número de Identificación": id_usuario,
            "Nombre del Libro": nombre_libro,
            "Autor del Libro": autor_libro,
            "Categoría del Libro": categoria_libro
        }

        self.registros.append(registro)

        messagebox.showinfo("Préstamo realizado", "El préstamo se realizó con éxito.")

        self.usuario_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.libro_entry.delete(0, 'end')
        self.autor_entry.delete(0, 'end')
        self.categoria_entry.delete(0, 'end')

    def mostrar_registros(self):
        registros_texto = ""
        for registro in self.registros:
            registros_texto += f"Nombre de Usuario: {registro['Nombre de Usuario']}\n"
            registros_texto += f"Número de Identificación: {registro['Número de Identificación']}\n"
            registros_texto += f"Nombre del Libro: {registro['Nombre del Libro']}\n"
            registros_texto += f"Autor del Libro: {registro['Autor del Libro']}\n"
            registros_texto += f"Categoría del Libro: {registro['Categoría del Libro']}\n"
            registros_texto += "-"*40 + "\n"

        messagebox.showinfo("Registros de Préstamos", registros_texto)

if __name__ == "__main__":
    root = Tk()
    menu = Menu(root)
    root.mainloop()
