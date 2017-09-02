def main():

    f = Lista()
    f.inserir("Angular",0)
    f.inserir("C++",1)
    f.inserir("Java",1)
    f.inserir("JavaScript",5)
    f.inserir("Python",0)
    f.inserirFim("NodeJs")

    print f.elementos
    f.remove("JavaScript")
    print f.elementos

class Lista(object):

    def __init__(self):
        self.elementos = []

    def inserirFim(self, elemento):
        self.elementos.insert(len(self.elementos),elemento)

    def inserir(self,elemento,index=None):
        if index is None:
            self.elementos.append(elemento)
        else:
            self.elementos.insert(index, elemento)

    vazia = lambda self: self.dados == 0

    def remove(self,elemento):
        if not self.vazia:
            return self.elementos.remove(elemento)


main()