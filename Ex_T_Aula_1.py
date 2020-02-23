def verificador_nome(nome):
  return len(nome) > 3

def verificador_idade(idade):
  return idade > 0 and idade <= 150

def verificador_salario(salario):
  return salario > 0

def verificador_sexo(sexo):
  return sexo == "M" or sexo == "F"

def verificador_estado_civil(estado_civil):
  return estado_civil == "S" or estado_civil == "C" or estado_civil == "V" or estado_civil == "D"

def main():
  cadastra_mais_um = 'SIM'
  while cadastra_mais_um == 'SIM':
    nome = ""
    while verificador_nome(nome) == False:
      nome = input("Digite seu Nome: ")
      if len(nome) <= 3:
        print("Nome invalido! Informe um com mais de 3 caracteres!")
      if verificador_nome(nome) == True:
        print("Nome Cadastrado!")
    
    idade = 0
    while verificador_idade(idade) == False:
      idade = int(input("Digite sua Idade: "))
      if verificador_idade(idade) == False:
        print("Idade Invalida!")
      else:
        print("Idade Cadastrada!")

    salario = 0
    while verificador_salario(salario) == False:
      salario = float(input("Informe seu salario: "))
      if verificador_salario(salario) == False:
        print("Salario Invalido!")
      else:
        print("Salario Cadastrado!")
    
    sexo = ""
    while verificador_sexo(sexo) == False:
      sexo = str(input("Informe seu Sexo, 'M' para Masculino e 'F' para Feminino: ")).strip('').upper()
      if verificador_sexo(sexo) == False:
        print("Sexo Invalido! Informe 'M' para Masculino e 'F' para Feminino!")
      else:
        print("Sexo Cadastrado!")
    
    estado_civil = ""
    while verificador_estado_civil(estado_civil) == False:
      estado_civil = str(input("Informe seu Estado civil! 'S' Para Solteiro, 'C' para Casado, 'V' para Viúvo ou 'D' para Divorciado: ")).strip('').upper()
      if verificador_estado_civil(estado_civil) == False:
        print("Estado Civil Invalido!")
        estado_civil = str(input("Informe seu Estado civil! 'S' Para Solteiro, 'C' para Casado, 'V' para Viúvo ou 'D' para Divorciado: ")).strip('').upper()
      else:
        print("Estado Civil cadastrado!")
    cadastra_mais_um = str(input("Dejesa cadastrar outra pessoa? (sim ou nao): ")).strip('').upper()      
main()

