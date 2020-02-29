def valor(qtde):
  if qtde < 12:
    return qtde * 1.30
  else:
    return qtde * 1

def main():
  qtde_maçãs = int(input("Quantidade de Maçãs: "))
  print(f"O valor total da compra é R${valor(qtde_maçãs)}!")
main()

