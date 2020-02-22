def main():
    entrada = int(input("Fatorial de qual valor? "))
    fatorial = 1
    for i in range(1,entrada+1):
        fatorial *= i #fatorial = fatorial * i
        if i < entrada:
            print(f"{i}", end=" x ")
        else:
            print(i, end=" = ")
    print(fatorial)
main()
