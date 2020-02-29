def divisao(valor_1, valor_2):
  return valor_1 / valor_2

def main():  
  valor_1 = float(input("Primeiro valor: "))
  loop = True
  while loop == True:
    valor_2 = float(input("Segundo valor: "))
    if valor_2 != 0:
      loop = False
  print(f"{valor_1} / {valor_2} = {divisao(valor_1, valor_2)}")
main()
