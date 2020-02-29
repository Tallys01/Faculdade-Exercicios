def produto(n1, n2):
    return ((2*n1)*(n2/2))

def soma(n1, n3):
    return ((3*n1)+n3)

def elevado(n3):
    return (n3**3)

def main():

    numero1 = int(input("Digite o valor do primeiro número: "))
    numero2 = int(input("Digite o valor do segundo número: "))
    numero3 = float(input("Digite o valor do terceiro número: "))

    print(produto(numero1, numero2))
    print(soma(numero1, numero3))
    print(elevado(numero3))
main()
