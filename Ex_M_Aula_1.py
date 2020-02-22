def main():
  numeros = []
  for i in range(3):
    numeros.append(input(f"Informe o {i+1} numero: "))
  numeros.sort()
  print(numeros)
main()
