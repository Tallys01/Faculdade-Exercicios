def calculo_tinta(area_total):
	litros_de_tinta = area_total / 3
	return litros_de_tinta

def calcular_latas(litros):
    qtde_latas = int(litros/18)
    if (litros%18 != 0):
        qtde_latas = qtde_latas+1
    return qtde_latas

def valor(qtde_latas):
	valor_por_lata = 80
	valor_total = qtde_latas * valor_por_lata
	return valor_total

def main():
	area_total = float(input("Informe a area a ser pintada em m²: "))
	qtde_litros = calculo_tinta(area_total)
	qtde_latas = calcular_latas(qtde_litros)
	valor_total = valor(qtde_latas)
	print(f"Para pintar totalmente essa area sera nescessario {qtde_latas} latas de tinta e vai custar R${valor_total}.")
main()
