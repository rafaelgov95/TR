def main():
    # testes da classe Fila
    f = Pilha()
    f.empilha("Angular")
    f.empilha("C++")
    f.empilha("Java")
    f.empilha("JavaScript")
    f.empilha("Python")
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())


class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

main()