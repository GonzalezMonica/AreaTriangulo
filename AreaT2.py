class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

if __name__ == "__main__":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    triangulo = Triangulo(base, altura)
    print("Área:", triangulo.calcular_area())
