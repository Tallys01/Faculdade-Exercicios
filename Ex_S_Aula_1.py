def detector_de_triangulo(h, a, b):
  if (h**2) == ((a**2)+(b**2)):
    return "Esses dados formam um triangulo retangulo"
  else:
    return "Esses dados não formam um triangulo retangulo"

def main():
  hipotenusa = float(input("Informe a medida da Hipotenusa: "))
  cateto_A = float(input("Informe a medida do Cateto 'A': "))
  cateto_B = float(input("Informe a medida do Cateto 'B': "))

  print(detector_de_triangulo(hipotenusa, cateto_A, cateto_B))
main()
