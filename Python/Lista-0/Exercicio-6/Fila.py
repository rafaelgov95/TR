def main():
    # testes da classe Fila
    f = Fila(10)
    f.insere("sal")
    f.insere("alho")
    f.insere("cebola")
    f.insere("pimenta")
    print(f.remove())
    print(f.remove())
    print(f.remove())
    print(f.remove())

class Fila:
    def __init__(self, max):
        self.elemento = [0]*max # cria uma fila com max elementos, todos zero
        self.ini = 0
        self.fim  = 0
    def insere(self, ele):
        self.elemento[self.fim] = ele
        self.fim += 1
    def remove(self):
        obj = self.elemento[self.ini]
        self.ini += 1
        return obj

main()