from livro import Livro


class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
    
    def emprestar_livro(self, livro: Livro):
        return livro.emprestar()
    
    def devolver_livro(self, livro: Livro):
        livro.devolver()
