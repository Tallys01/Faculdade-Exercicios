def situacao(nota1, nota2):
  media = (nota1 + nota2) / 2
  if media == 10:
    return "Aprovado com Distinção"
  elif media >= 7:
    return "Aprovado"
  else:
    return "Reprovado"

def main():
  nota1 = float(input("Informe a primeira Nota: "))
  nota2 = float(input("Informe a segunda Nota: "))
  print(situacao(nota1, nota2))

main()
