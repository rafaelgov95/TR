def main():

    f = Lista()
    f.inserir("sal")
    f.inserir("alho",0)
    f.inserir("cebola",0)
    f.inserir("pimenta")

    print f.dados

class Lista(object):

    def __init__(self):
        self.dados = []

    def inserirFim(self, elemento):
        self.dados.insert(len(self.dados),elemento)

    def inserir(self,elemento,index=None):
        if index is None:
            self.dados.append(elemento)
        else:
            self.dados.insert(index, elemento)

    def remove(self):
        if not self.vazia():
            return self.dados.pop(-1)


main()