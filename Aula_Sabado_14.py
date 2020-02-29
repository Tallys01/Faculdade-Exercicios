def main():
  soma = 0
  for i in range(10):
    valor = int(input(f"Informe o {i+1} valor: "))
    soma += valor
  print(f"Todos os valores digitados somados é igual a {soma}!")
main()
