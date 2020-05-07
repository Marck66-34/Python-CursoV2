from .figura import Figura

class Triangulo(Figura):
    def __init__(self, color_fondo, color_borde, base, altura):
        super().__init__(color_fondo, color_borde)

        self.base = base
        self.altura = altura
    
    def dibujar(self):
        print(f'Se está dibujando un triángulo con base {self.base} y altura {self.altura}.')
    
    def area(self):
        resultado = self.base * self.altura / 2
