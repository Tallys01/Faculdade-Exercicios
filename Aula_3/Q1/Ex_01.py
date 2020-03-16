from pilha import Pilha

def main():
    pilha = Pilha()
    condicao = True
    while condicao:
        print("""
[1] Adicionar
[#] Apagar
[@] Esvaziar
[0] Fechar
        """)
        opcao = input("Resposta: ")

        while opcao != "1" and opcao != "#" and opcao != "@" and opcao != "0":
            opcao = input("Resposta: ")

        if opcao == "1":
            pilha.push(input("Dados: "))

        elif opcao == "#":
            if pilha.tamanho() > 0:
                    pilha.pop()
            else:
                print("OPERAÇÃO INVALIDA!")

        elif opcao == "@":
            if pilha.tamanho() > 0:

                while pilha.tamanho() != 0:
                    pilha.pop()
                else:
                    print("OPERAÇÃO INVALIDA!")

        elif opcao == "0":
            condicao = False

        print(pilha.getpilha())
main()