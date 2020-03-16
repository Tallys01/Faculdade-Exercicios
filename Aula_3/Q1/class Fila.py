class Fila:
#construtor
    def __init__(self):
        self.__dados = []
#Mostrar valores da Fila
    def getFila(self):
        return self.__dados
#inserir valores na fila
    def inserirDados(self, novo_Valor):
        self.__dados.append(novo_Valor)
#remover valores da fila
    def removerDados(self):
        self.__dados.pop()