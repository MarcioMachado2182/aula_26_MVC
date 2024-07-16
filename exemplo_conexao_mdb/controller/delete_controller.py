import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.delete_view import DeleteView

class DeleteController:
    def __init__(self, view:DeleteView, model:UsuarioModel):
            self.view = view
            self.model = model
            self.view.deletar_button.config(command=self.deletar_usuario)
            self.carregar_usuarios()

    def deletar_usuario(self):
        id = self.view.get_id()
        if id:
            self.model.apagar_usuario(id)
            self.view.usuarios_listbox(0, tk.END)
            self.carregar_usuarios()

    def adicionar_usuario_lista(self, usuario):
            self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos")

    def carregar_usuarios(self):
          usuarios = self.model.selecionar_usuarios()
          for usuario in usuarios:
                self.view.adicionar_usuario_lista(usuario)

 
    
    