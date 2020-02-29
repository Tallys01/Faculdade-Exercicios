def verificador(valor, array):
  if valor in array:
    return True
  else:
    return False

def main():
  array_1 = []

  for i in range(20):
    array_1.append(i+1)
  array_1.sort()

  novo_valor = int(input("Informe outro valor: "))

  if verificador(novo_valor, array_1) == True:
    array_1.remove(novo_valor)

  print(array_1)
main()
