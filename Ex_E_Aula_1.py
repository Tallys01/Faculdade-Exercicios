def calculadora_de_salario(horas, valor_por_hora):
    total = valor_por_hora * horas
    return total


horas = float(input("Quantas horas você trabalhou? "))
valor_por_hora = float(input("Quanto você ganha por Hora? "))
print(f"Você vai receber R${calculadora_de_salario(horas, valor_por_hora)}")
