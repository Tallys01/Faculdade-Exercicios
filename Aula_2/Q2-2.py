from estacionamento import Estacionamento
#Team: Mateus Tallys, Diego Figuereido e Guilherme
def main():
    condição = True
    estacionamento = Estacionamento()
    while condição:
        print('Digite ce quer fazer \n1. Adiconar carro. \n2. Remover carro.\nS. Mostrar Estacionamento. \nX. Fechar programa.')
        entrada = input('')
        if entrada == '1':
            estacionamento.adcionar_carro(input('Digite a placa do carro: '))
        elif entrada == '2':
            if estacionamento.tamanho_estacionamento() == 0:
                print('Não existe carros estacionados.')
            else:
                remover = input('Digite a placa que quer remover: ')
                if estacionamento.localizar(remover) == True:
                    estacionamento.remover_carro(remover)
                else:
                    print('Carro não localizado.')
        elif entrada == 's' or entrada == 'S':
            print(estacionamento.retornar_estacionamento())

        elif entrada == 'x' or entrada == 'X':
            condição = False
        else:
            print('Digite um caractere valido: ')


main()
