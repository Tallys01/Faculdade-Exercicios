def verificador_par(array):
  qtde = 0
  for i in range(len(array)):
    if array[i] % 2 == 0:
      qtde += 1
  return qtde

def verificador_inpar(array):
  qtde = 0
  for i in range(len(array)):
    if array[i] % 2 != 0:
      qtde += 1
  return qtde

def main():
  array = []

  for i in range(20):
    array.append(i+1)

  print(f"Existem {verificador_par(array)} numeros Pares!")
  print(f"Existem {verificador_inpar(array)} numeros Inpares!")
main()
