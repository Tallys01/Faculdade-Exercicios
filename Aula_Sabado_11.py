def media(nota_1, nota_2):
  return (nota_1 + nota_2) / 2

def main():
  loop = True
  while loop == True:
    nota_1 = float(input("Primeira Nota: "))
    nota_2 = float(input("Segunda Nota: "))
    if nota_1 and nota_2 >= 0 and nota_1 and nota_2 <= 10:
      loop = False
    else:
      print("Voce inseriu algum dado invalido! olhe com atenção.")
  print(f"Media = {media(nota_1, nota_2)}")
main()
