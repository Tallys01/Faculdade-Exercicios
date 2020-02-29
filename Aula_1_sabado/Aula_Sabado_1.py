def anos_dias(idade):
  return idade * 365

def main():
  idade = int(input("Informe sua idade: "))
  print(f"{idade} anos é igual a {anos_dias(idade)} dias!")
main()
