class Pessoa: #Team: Mateus Tallys e Diego Figuereido
    def __init__(self, nome, telefone, prioridade):
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade

####
class Fichas:
    def __init__(self):
        self.dados = []

    def retornar_cadastro(self):
        return self.dados
    #adicionando
    def adcionar_ficha(self, novoValor):
        self.dados.append(novoValor)
    # Tamanho
    def tamanho(self):
        return len(self.dados)
    # Removendo e pegando a pessoa com maior prioridade
    def maiorprioridade(self):
        usuario = 0
        for i in range(0, len(self.dados)):
            if self.dados[i].prioridade > self.dados[usuario].prioridade:
                usuario = i
        usuariomaiorprioridade = self.dados.pop(usuario)
        return usuariomaiorprioridade
