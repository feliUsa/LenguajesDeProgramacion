import cmath
from antlr4 import *
from transformadasLexer import transformadasLexer
from transformadasParser import transformadasParser
from transformadasVisitor import transformadasVisitor

class FourierEvalVisitor(transformadasVisitor):
    def visitFourierTransform(self, ctx):
        print("Transformada de Fourier")
        array = self.visit(ctx.array())
        N = int(ctx.NUMBER().getText())
        
        # Calculamos la Transformada de Fourier Discreta
        fourier_result = self.fourier_transform(array, N)
        
        print("Transformada de Fourier (limpia):")
        self.mostrar_transformada(fourier_result)  # Mostrar en formato limpio
        return fourier_result  # Devolver el resultado final

    def visitArrayExpr(self, ctx):
        # Extraer los elementos del array como una lista de números
        elements = [float(num.getText()) for num in ctx.elements().NUMBER()]
        print(f"Entrada: {elements}")
        return elements

    def fourier_transform(self, array, N):
        result = []
        for k in range(N):
            sum_val = 0
            for n, x_n in enumerate(array):
                angle = -2 * cmath.pi * k * n / N
                sum_val += x_n * cmath.exp(1j * angle)  # Expresión de Fourier
            result.append(sum_val)
        return result

    def mostrar_transformada(self, resultado):
        # Redondear y formatear cada número complejo de la lista
        for idx, valor in enumerate(resultado):
            valor_real = round(valor.real, 5)  # Redondeamos a 5 decimales
            valor_imag = round(valor.imag, 5)  # Redondeamos a 5 decimales
            
            # Mostramos el número en formato "a + bi" o "a - bi"
            if valor_imag >= 0:
                print(f"Resultado {idx}: {valor_real} + {valor_imag}i")
            else:
                print(f"Resultado {idx}: {valor_real} - {abs(valor_imag)}i")

    def visitExpr(self, ctx):
        if ctx.fourier():
            return self.visitFourierTransform(ctx.fourier())
        return None

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())  # Asegurar que devolvemos el resultado de expr

# Función para leer desde archivo
def leer_entrada_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            return file.read().strip()  # Leemos el contenido y eliminamos espacios innecesarios
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return None

# Prueba el visitor con archivo de entrada
def main():
    archivo_entrada = "input.txt"  # El nombre del archivo de entrada
    input_text = leer_entrada_desde_archivo(archivo_entrada)

    if input_text:
        input_stream = InputStream(input_text)
        lexer = transformadasLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = transformadasParser(stream)
        tree = parser.program()

        visitor = FourierEvalVisitor()
        result = visitor.visit(tree)
        
        if result is None:
            print("Error: El resultado es None.")
            
        
if __name__ == "__main__":
    main()
