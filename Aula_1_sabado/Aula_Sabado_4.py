def positivo_negativo(numero):
  if numero == 0:
    return "VALOR NEUTRO!"
  elif numero > 0:
    return "VALOR POSITIVO!"
  else:
    return "VALOR NEGATIVO!"

def main():
  valor = int(input("Informe um valor: "))
  print(positivo_negativo(valor))
main()
