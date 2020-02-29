def maior_que_10(valor):
  if valor > 10:
    return "É maior que 10!"
  else:
    return "É menor que 10!"

def main():
  valor = int(input("Informe um valor: "))
  print(maior_que_10(valor))
main()
