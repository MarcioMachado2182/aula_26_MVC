import tkinter as tk

from model.usuario_m import UsuarioModel
from view.usuario_v import UsuarioView
from controller.usuario_c import UsuarioController

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Gerenciamento de Usuarios')
    root.geometry('400x300')

    model = UsuarioModel()
    view = UsuarioView(root)
    model.atualizar_dados_usuarios(28, 'Caveira', 101)
    controller = UsuarioController(view, model)
    root.mainloop()





