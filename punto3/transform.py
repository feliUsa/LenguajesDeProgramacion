import cmath
from antlr4 import *
from transformadasLexer import transformadasLexer
from transformadasParser import transformadasParser
from transformadasVisitor import transformadasVisitor

# Función pura: transformada de Fourier
def fourier_transform(array, N):
    return [
        sum(
            x_n * cmath.exp(-2j * cmath.pi * k * n / N)
            for n, x_n in enumerate(array)
        )
        for k in range(N)
    ]

# Función pura: transformada inversa de Fourier
def inverse_fourier_transform(array, N):
    return [
        sum(
            X_k * cmath.exp(2j * cmath.pi * k * n / N)
            for k, X_k in enumerate(array)
        ) / N
        for n in range(N)
    ]

class FourierEvalVisitor(transformadasVisitor):
    def visitFourierTransform(self, ctx):
        print("Transformada de Fourier")
        array = self.visit(ctx.array())
        
        N = int(ctx.NUMBER().getText()) if ctx.NUMBER() else None
        if N is None:
            raise ValueError("Error: No se pudo obtener el número de puntos para la transformada.")
        
        # Usamos la función pura para calcular la Transformada de Fourier
        fourier_result = fourier_transform(array, N)
        
        print("Transformada de Fourier (limpia):")
        self.mostrar_transformada(fourier_result)
        return fourier_result

    def visitInverseFourierTransform(self, ctx):
        print("Transformada Inversa de Fourier")
        array = self.visit(ctx.array())
        
        N = int(ctx.NUMBER().getText()) if ctx.NUMBER() else None
        if N is None:
            raise ValueError("Error: No se pudo obtener el número de puntos para la transformada inversa.")
        
        # Usamos la función pura para calcular la Transformada Inversa de Fourier
        inverse_fourier_result = inverse_fourier_transform(array, N)
        
        print("Transformada Inversa de Fourier (limpia):")
        self.mostrar_transformada(inverse_fourier_result)
        return inverse_fourier_result

    def visitArrayExpr(self, ctx):
        # Extraer los elementos del array como una lista de números complejos
        elements = [self.convertir_a_complejo(num.getText()) for num in ctx.elements().complexNumber()]
        print(f"Entrada: {elements}")
        return elements

    def convertir_a_complejo(self, texto):
        try:
            # Función pura: convertir texto en número complejo
            return complex(texto.replace('i', 'j'))
        except ValueError:
            raise ValueError(f"Error al convertir {texto} a número complejo")

    def mostrar_transformada(self, resultado):
        # Mostrar el resultado de manera pura e inmutable
        for idx, valor in enumerate(resultado):
            valor_real = round(valor.real, 5)
            valor_imag = round(valor.imag, 5)
            
            # Mostrar el número en formato "a + bi" o "a - bi"
            signo = '+' if valor_imag >= 0 else '-'
            print(f"Resultado {idx}: {valor_real} {signo} {abs(valor_imag)}i")

    def visitExpr(self, ctx):
        if ctx.fourier():
            return self.visitFourierTransform(ctx.fourier())
        elif ctx.inversa():
            return self.visitInverseFourierTransform(ctx.inversa())
        return None

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

# Función para leer desde archivo
def leer_entrada_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return None

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
