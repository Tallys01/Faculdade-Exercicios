def main():
  produto1 = input("Nome Produto 1: ")
  preco1 = float(input("Preço produto 1: "))
  produto2 = input("Nome Produto 2: ")
  preco2 = float(input("Preço produto 2: "))
  produto3 = input("Nome Produto 3: ")
  preco3 = float(input("Preço produto 3: "))

  if preco1 < preco2 and preco1 < preco3:
    print(f"O produto mais barato é {produto1}!")
  elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto mais barato é {produto2}!")
  else:
    print(f"O produto mais barato é {produto3}!")

main()
