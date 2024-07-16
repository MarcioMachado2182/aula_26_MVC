import tkinter as tk

from model.usuario_m import UsuarioModel
from view.usuario_v import UsuarioView
from controller.usuario_c import UsuarioController
from view.delete_view import DeleteView
from view.usuario_v import UsuarioView
from controller.delete_controller import DeleteController
from view.atualizar_view import AtualizarView
from controller.atualizar_controller import AtualizarController


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Gerenciamento de Usuarios')
    root.geometry('400x300')

    model = UsuarioModel()
    view = AtualizarView(root)
    controller = AtualizarController(view, model)
    #view = DeleteView(root)
    #view = UsuarioView(root)
    #model.atualizar_dados_usuarios(28, 'Caveira', 101)
    #controller = DeleteController(view, model)
    root.mainloop()





