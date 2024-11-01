from tkinter import Tk, Canvas
from Triangulo import Triangulo

def dibujar_triangulo(canvas, tri):
    
    x1, y1 = 100, 300  
    x2, y2 = x1 + tri.lado1 * 10, 300  
    x3, y3 = x1 + (tri.lado2 * 10) / 2, 300 - (tri.calcular_area() * 10)  # Vértice superior


    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline='black', fill='blue')

def main():
    
    triangulo = Triangulo(5, 5, 5)
    

    area = triangulo.calcular_area()
    perimetro = triangulo.calcular_perimetro()

   
    print(f"Área del triángulo: {area}")
    print(f"Perímetro del triángulo: {perimetro}")

    
    ventana = Tk()
    ventana.title("Dibujo de Triángulo")

   
    canvas = Canvas(ventana, width=400, height=400)
    canvas.pack()

    dibujar_triangulo(canvas, triangulo)

    ventana.mainloop()

if __name__ == "__main__":
    main()