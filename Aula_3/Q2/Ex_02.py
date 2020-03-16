from pilha_2 import Pilha
from fila_2 import Fila

def main():
    pilha = Pilha()
    pilha_2 = Pilha()
    fila = Fila()
    
    qtde = int(input("Quantos valores você quer inserir na Pilha: "))

    for i in range(qtde): #alimentando a pilha
        pilha.push(input(f"Valor {i+1}: "))

    print("""Escolha o metodo de inversão: 
    [1] Usando Pilhas adicionais
    [2] Usando Filas adicionais""")

    escolha = int(input("Resposta: "))

    while escolha != 1 and escolha != 2:
        print("INVALIDO!!!")
        escolha = int(input("Resposta: "))

    if escolha == 1: #inverção com Pilha
        for i in range(qtde):
            pilha_2.push(pilha.topo())
            pilha.pop()
        print(pilha_2.getPilha())

    else: #inverção com lista
        for i in range(qtde):
            fila.inserirDados((pilha.topo()))
            pilha.pop()
        print(fila.getFila())

main()


