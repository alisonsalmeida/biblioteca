from datetime import datetime
from livro import Livro
from usuario import Usuario


class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
    
    def registrar_emprestimo(self):
        if self.livro.emprestar():
            print(f"Livro '{self.livro.titulo}' emprestado para {self.usuario.nome}.")
        else:
            print(f"Livro '{self.livro.titulo}' não está disponível.")
    
    def registrar_devolucao(self):
        self.livro.devolver()
        self.data_devolucao = datetime.now()
        print(f"Livro '{self.livro.titulo}' devolvido por {self.usuario.nome}.")
