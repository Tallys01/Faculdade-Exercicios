def verificar_sinal(num):
    if num >= 0:
       return "Número positivo!"
    else:
       return "Número negativo!"
       
def main():
    numero = int(input("Digite um número: "))
    print (verificar_sinal(numero))
main()
