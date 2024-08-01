from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro


def cadastrar_usuario(biblioteca: Biblioteca):
    nome = input("digite o nome do usuario: ")
    id = str(len(biblioteca.usuarios) + 1)

    user = Usuario(nome=nome, id=id)
    biblioteca.usuarios.append(user)

    print(f'usuario: {nome} cadastrado com id: {id}')


def cadastrar_livro(biblioteca: Biblioteca):
    titulo = input("digite o titulo do livro: ")
    autor = input("digite o autor do livro: ")
    isbn = input("digite o isbn do livro: ")

    liv = Livro(titulo=titulo, autor=autor, isbn=isbn)
    biblioteca.adicionar_livro(liv)
    print(f'livro: {titulo} cadastrado com sucesso')


def emprestar_livro(biblioteca: Biblioteca):
    user_id = input('digite o id do usuario: ')
    user = biblioteca.buscar_usuario(user_id)
    if user is None:
        print(f"usuario {user_id} nao encontrado")
        return
    
    isbn = input('digite o isbn do livro: ')
    livro = biblioteca.buscar_livro(isbn)
    if livro is None:
        print('livro nao encontrado')

    biblioteca.registrar_emprestimo(user, livro)


def devolver_livro(biblioteca: Biblioteca):
    user_id = input('digite o id do usuario: ')
    user = biblioteca.buscar_usuario(user_id)
    if user is None:
        print(f"usuario {user_id} nao encontrado")
        return
    
    isbn = input('digite o isbn do livro: ')
    livro = biblioteca.buscar_livro(isbn)
    if livro is None:
        print('livro nao encontrado')

    biblioteca.registrar_devolucao(user, livro)


def main():
    biblioteca = Biblioteca()

    choices = {
        '1': cadastrar_usuario,
        '2': cadastrar_livro,
        '3': emprestar_livro,
        '4': devolver_livro
    }
    
    while True:
        print("*" * 50)
        print("selecione a função: ")
        print("1 - cadastrar usuario")
        print("2 - cadastrar livro")
        print("3 - emprestar livro")
        print('4 - devolver livro')

        choice = input("opcao: ")
        func = choices.get(choice, None)
        if func:
            func(biblioteca)

        else:
            print('opcao invalida')


if __name__ == '__main__':
    main()
