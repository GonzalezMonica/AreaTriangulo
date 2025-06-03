def calcular_area(base, altura):
    return (base * altura) / 2

def main():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = calcular_area(base, altura)
    print("Área:", area)

if __name__ == "__main__":
    main()
