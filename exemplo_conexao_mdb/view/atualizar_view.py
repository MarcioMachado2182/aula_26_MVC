import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AtualizarView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.id__label = ttk.Label(self, text="Id:")
        self.id__label.grid(row=0, column=2, padx=10, pady=5)
       
        self.id_entry = ttk.Entry(self)
        self.id_entry.grid(row=0, column=3, padx=10, pady=5)

        self.nome_label = ttk.Label(self, text="Novo Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=5)
       
        self.nome_entry = ttk.Entry(self)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
       
        self.idade_label = ttk.Label(self, text="Nova Idade:")
        self.idade_label.grid(row=1, column=0, padx=10, pady=5)
       
        self.idade_entry = ttk.Entry(self)
        self.idade_entry.grid(row=1, column=1, padx=10, pady=5)
       
        self.adicionar_button = ttk.Button(self, text="Atualizar")
        self.adicionar_button.grid(row=2, column=0, columnspan=2, pady=10)
       
        self.usuarios_listbox = tk.Listbox(self)
        self.usuarios_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
       
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def get_nome(self):
        return self.id_entry.get()

    def get_nome(self):
        return self.nome_entry.get()

    def get_idade(self):
        return self.idade_entry.get()
    
    def get_id(self):
        id = self.id_entry.get()
        return id 

    def adicionar_usuario_lista(self, usuario):
        self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")

    def mostrar_aviso():
        messagebox.showinfo("Aviso", "Esta é uma mensagem de aviso!")

             

    