import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.usuario_v import UsuarioView
from view.atualizar_view import AtualizarView

class AtualizarController:
    def __init__(self, view:AtualizarView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.atualizar_usuario)
        self.carregar_usuarios()

    def atualizar_usuario(self):
        id  = self.view.get_id()
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        if id and nome and idade.isdigit():
            self.model.atualizar_dados_usuarios(id, nome, idade)
            self.view.adicionar_usuario_lista((id, nome, idade))
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_usuarios()
        else: 
            self.viwe.show_info()
           

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)