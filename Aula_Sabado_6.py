def media_ponderada(nota_1, nota_2, nota_3):
  if nota_1 > nota_2 and nota_1 > nota_3:
    return ((nota_1*4) + (nota_2*3) + (nota_3*3)) / 10
  elif nota_2 > nota_1 and nota_2 > nota_3:
    return ((nota_2*4) + (nota_1*3) + (nota_3*3)) / 10
  else:
    return ((nota_3*4) + (nota_1*3) + (nota_2*3)) / 10

def aprovado_reprovado(media):
  if media < 5:
    return "REPROVADO!"
  else:
    return "APROVADO!"

def main():
  matricula = int(input("Informe a Matricula do Aluno: "))
  print("Informe suas Notas!")
  nota_1 = float(input("Primeira Nota: "))
  nota_2 = float(input("Segunda Nota: "))
  nota_3 = float(input("Terceira Nota: "))

  media = media_ponderada(nota_1, nota_2, nota_3)

  print(f"Situação do Aluno de matricula: {matricula} é {aprovado_reprovado(media)}, Media final = {media_ponderada(nota_1, nota_2, nota_3)}")

main()
