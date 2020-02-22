def descontoINSS(salario):
    return (0.08 * salario)

def descontoIPRF(salario):
    return (0.11*salario)

def descontoSindicato(salario):
    return (0.05*salario)

def calcularSalarioBruto(hora, valor):
    return hora*valor

def valorDescontado(salario):
    return (descontoINSS(salario)+descontoIPRF(salario)+descontoSindicato(salario))


def calcularSalarioLiquido(salario):
    return (salario- valorDescontado(salario))

def main():
    valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
    qnt_horas = float (input("Digite a quantidade de horas"))

    salarioTotal = calcularSalarioBruto(qnt_horas, valor_hora)
    print (salarioTotal)

    print(descontoIPRF(salarioTotal))
    print(descontoINSS(salarioTotal))
    print(descontoSindicato(salarioTotal))
    print(calcularSalarioLiquido(salarioTotal))
    print(valorDescontado(salarioTotal))


main()
