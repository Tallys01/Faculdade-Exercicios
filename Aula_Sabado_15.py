def main():
  soma = 0
  qtde = int(input("Informe o Quantidade de mercadorias em estoque: "))

  for i in range(qtde):
    valor = float(input(f"Informe o valor da {i+1} Mercadoria: "))
    soma += valor

  print(f"Valor total em estoque R${soma:.2f}")
  print(f"Media do itens no Estoque R${soma / qtde:.2f}")

main()
