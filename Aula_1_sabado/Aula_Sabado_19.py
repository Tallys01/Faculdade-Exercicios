def verificador(array_1, array_2):
  qtde = 0
  for i in range(15):
    if array_1[i] == array_2[i]:
      qtde+=1
  return qtde

def main():
  array_1 = []
  array_2 = []

  for i in range(15):
    array_1.append(i+1)
    array_2.append(i+1)
  array_1.sort()
  array_2.sort()

  print(f"A quantidades de itens repetidos no primeiro e no segundo vetor é igual a {verificador(array_1, array_2)}! ")
main()
