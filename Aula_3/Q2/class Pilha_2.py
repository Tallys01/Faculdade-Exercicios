class Pilha:
#construtor
    def __init__(self):
        self.__dados = []
#Mostra os valores da pilha
    def getPilha(self):
        return self.__dados
#inserção de elementos
    def push(self, novo_elemento):
        self.__dados.append(novo_elemento)
#remoção de elementos
    def pop(self):
        self.__dados.pop()
#Descorberta do elementos do Topo
    def topo(self):
        return self.__dados[len(self.__dados)-1]
#esvaziamento da pilha
    def esvaziar(self):
        while(len(self.__dados) != 0):
            self.__dados.pop()
#tamanho da pilha
    def tamanho(self):
        return len(self.__dados)
