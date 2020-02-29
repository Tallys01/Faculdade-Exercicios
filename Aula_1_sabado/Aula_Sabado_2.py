def calcular_area(altura, largura):
  area = altura * largura
  return area
  
def main():
  altura = float(input("Informe a altura do Retangulo: "))
  largura = float(input("Informe a largura do Retangulo: "))
  print(f"A area desse Retangulo é {calcular_area(altura, largura):.2f} centimetros quadrados!")
main()
