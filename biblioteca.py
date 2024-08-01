from typing import List
from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo


class Biblioteca:
    def __init__(self):
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []
        self.emprestimos: List[Emprestimo] = []

    def buscar_usuario(self, user_id: str):
        for user in self.usuarios:
            if user_id == user.id:
                return user
    
    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
    
    def remover_livro(self, livro: Livro):
        self.livros.remove(livro)
    
    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None
    
    def registrar_emprestimo(self, usuario, livro):
        livro = self.buscar_livro(livro.isbn)
        user = self.buscar_usuario(usuario.id)

        if livro and user:
            emprestimo = Emprestimo(livro, usuario)
            emprestimo.registrar_emprestimo()
            self.emprestimos.append(emprestimo)
            return True
        
        return False
    
    def registrar_devolucao(self, usuario, livro):
        for emprestimo in self.emprestimos:
            if emprestimo.livro == livro and emprestimo.usuario == usuario and emprestimo.data_devolucao is None:
                emprestimo.registrar_devolucao()
                self.emprestimos.remove(emprestimo)
                return
            
        print("Empréstimo não encontrado ou livro já devolvido.")
