def detector_de_palindromo(numero):
  numero_inverso = numero[::-1]
  print(f"O inverso de {numero} e {numero_inverso}")

  if (numero) == (numero_inverso):
    return "O numero digitado é um palindromo"
  else: 
    return "O numero digitado nao é um palindromo"

def main():
  numero = input('Digite um numero: ')
  print(detector_de_palindromo(numero))
main()
