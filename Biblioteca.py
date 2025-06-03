class livro:
    #definir aqui dentro o molde, que vai ser as caracteristicas e o comportamento

    def __init__(self, titulo, autor, numero_pagina):
        #metodo magico construtor
        self.titulo = titulo
        self.autor = autor
        self.numero_pagina = numero_pagina
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f'O livro {self.titulo} foi emprestado'
        return f'O livro {self.titulo} já está emprestado.'

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f'O livro {self.titulo} foi devolvido'
        return f'O livro {self.titulo} já está disponivel'
    
class leitor:
    def __init__(self, nome):
        self.nome = nome
        #o colchete vazio cria uma lista, porque um leitor pode pegar mais de um livro
        self.livros_emprestados = []
    def realizar_emprestimos(self,livro):
        if not livro.emprestado:
            self.livros_emprestados.append(livro)
            return livro.emprestar()
        
        return f'O livro {livro.titulo} não está diponivel'
    
    def devolver_livro(self,livro, dias_atrasado):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            multa = max(0, (dias_atrasado - 15) *2)
            #2 é o valor da multa por dia

            return livro.devolver() + f'multa R${multa:.2}'
        
        return f'O leitor {self.nome} não possui o livro {livro.titulo}'
    
class biblioteca:
    def __init__(self):
        self.livro = []
        self.leitor = []
        
    def adicionar_livro(self, livro):
        self.livro.append(livro)
        return f'O livro {livro.titulo} foi adicionado a biblioteca'
    
    def remover_livro(self, livro):
        if livro in self.livro:
            self.livro.remove(livro)
            return f'O livro {livro} foi removido da biblioteca'
        return f'O livro {livro} não está na biblioteca'
    
    def emprestar_livro(self, leitor, livro):
        if livro in self.livro and not livro.emprestado:
            return leitor.realizar_emprestimos(livro)
        return f'O {livro.titulo} não está disponivel para emprestimo'
    
livro1= livro("fundamentos de POO", "Ricardo", 500)
leitor1= leitor("larissa")
biblioteca = biblioteca()

print(biblioteca.adicionar_livro(livro1))
print(biblioteca.emprestar_livro(leitor1, livro1))
print(leitor1.devolver_livro(livro1, dias_atrasado=20))