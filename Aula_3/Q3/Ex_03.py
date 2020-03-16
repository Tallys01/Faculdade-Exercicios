from pilha_3 import Pilha
from time import sleep

def main():
    pilha = Pilha()
    pilha_2 = Pilha()

    print("""Deseja preencher a Pilha 'S'? 
    [1] Preencher manualmente 
    [2] Preencher automaticamente""")
    resposta = int(input("Resposta: "))

    if resposta == 1:

        qtde = int(input("Quantos elementos quer na Pilha? "))

        for i in range(qtde):
            pilha.push(input(f"{i+1} Valor: "))
        print(f"Pilha 'S': {pilha.getPilha()}")

    else:
        print("Gerando a pilha...")
        sleep(5)

        pilha.push(100)
        pilha.push(80)
        pilha.push(90)
        pilha.push(70)
        pilha.push(60)
        pilha.push(40)
        pilha.push(30)
        pilha.push(20)
        pilha.push(10)
        pilha.push(50)

        print(pilha.getPilha())

    print("Ordenando sua Pilha...")
    sleep(7)

    print(f"Pilha 'S'(Ordenada):{pilha.ordenacao(pilha, pilha_2)}")

main()