def contador(contagem):
  for i in range(contagem+1):
    print(i, end = ' ')
  return ''

def main():
  contagem = int(input("Ate onde deseja contar: "))
  print(contador(contagem))  
main()
