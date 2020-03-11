class Estacionamento: #Team: Mateus Tallys, Diego Figuereido e Guilherme   

# construtor
    def __init__(self):
        self.dados = []

    def retornar_estacionamento(self):
        return self.dados

    def adcionar_carro(self, novoValor):
        self.dados.append(novoValor)

    def remover_carro(self, placa):
        pos = self.dados.index(placa)
        for i in range(0, pos):
            self.dados.append(self.dados[i])
        for i in range(0, pos + 1):
            self.dados.pop(0)

    def tamanho_estacionamento(self):
        return len(self.dados)

    def localizar(self, placa):
        for i in range(len(self.dados)):
            if self.dados[i] == placa:
                return True
        return False
