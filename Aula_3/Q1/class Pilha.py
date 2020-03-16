class Pilha:
#construtor
    def __init__(self):
            self.__dados = []

#pegando novo valor
    def push(self,novo_valor):
        self.__dados.append(novo_valor)

#mostrando o tamanho
    def tamanho(self):
        return len(self.__dados)

#retirando dados
    def pop(self):
        self.__dados.pop()

#print da pilha
    def getpilha(self):
        return self.__dados