def calcular_tmb_tme(pm, grupo, flag):
#Convertendo o flag
    if flag == 1:
        flag = 'B'
    else:
        flag = 'E'

#Atribuindo valor ao 'K'
    if grupo == 1:
        k = 129
    elif grupo == 2:
        k = 78
    elif grupo == 3:
        k = 70
    elif grupo == 4:
        k = 49
    else:
        k = 10
#Calculando TMB ou TME
    if flag == 'B':
        tmb = (pm**0.75) * k
        return tmb
    elif flag == 'E':
        tme = (pm ** 0.25) * k
        return tme

def main():
    print('''A qual grupo o animal pertence? 
    [1] Passeriformes
    [2] Não Passeriformes
    [3] Mamíferos Placentários
    [4] Marsupiais e Edentadas
    [5] Répteis''')
    grupo = int(input("Grupo: "))
    print('''O que você dejesa calcular? 
    [1] Taxa metabólica basal (TMB)
    [2] Taxa metabólica Específica(TME)''')
    flag = int(input(("Escolha '1' para TMB ou '2' para TME: ")))
    pm = float(input("Informe o Peso do Animal em quilogramas:  "))

    if flag == 1:
        print(f"O resultado do TMB do seu animal é: {calcular_tmb_tme(pm, grupo, flag):.2f}")
    else:
        print(f"O resultado do TME do seu animal é: {calcular_tmb_tme(pm, grupo, flag):.2f}")
main()
