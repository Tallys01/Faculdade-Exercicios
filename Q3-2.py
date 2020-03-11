from pessoa import Pessoa #Team: Mateus Tallys e Diego Figuereido
from cadastrofisico import Fichas
from random import randint

def main ():
    condicao = True
    coracao = 0
    fichascriada = Fichas()
    while condicao:
        print('[1] Cadastrar paciente: \n[2] Exibir fila de espera: \n[3] Finalizar atendimento: ')
        opcao = input()
        if opcao == '1':
            coracao = randint(0, 1)
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            prioridade = int(input('Grau de Urgência: '))
            usuario = Pessoa(nome, telefone, prioridade)
            fichascriada.adcionar_ficha(usuario)
        elif opcao == '2':
            print(f'No momento a fila de espera tem {fichascriada.tamanho()} paciente(s)')
        elif opcao == '3':
            print('Obrigado')
            condicao = False
        else:
            print('Opção inválida por favor tente novamente:')
        if fichascriada.tamanho() > 0 and coracao > 0:
            paciente = fichascriada.maiorprioridade()
            print(f'O próximo paciente a ser operado: Nome: {paciente.nome}. Telefone: {paciente.telefone} .')


main()

