import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

# Función auxiliar para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class MapFilterEvalListener(ParseTreeListener):
    def __init__(self, numeros):
        self.numeros = numeros

    def exitMapFunction(self, ctx):
        function_name = ctx.function().getText()
        print(f"Applying {function_name} to {self.numeros}")

        # Aplicar MAP usando la función definida
        if function_name == "square":
            resultado = list(map(lambda x: x ** 2, self.numeros))
        elif function_name == "cube":
            resultado = list(map(lambda x: x ** 3, self.numeros))
        elif function_name == "double":
            resultado = list(map(lambda x: x * 2, self.numeros))
        elif function_name == "negate":
            resultado = list(map(lambda x: -x, self.numeros))
        elif function_name == "even_to_zero":
            resultado = list(map(lambda x: 0 if x % 2 == 0 else x, self.numeros))
        elif function_name == "is_prime":
            resultado = list(map(is_prime, self.numeros))
        else:
            print(f"Function {function_name} not supported.")
            return
        print(f"Result of MAP: {resultado}")

    def exitFilterFunction(self, ctx):
        condition_name = ctx.condition().getText()
        print(f"Applying {condition_name} filter to {self.numeros}")

        # Aplicar FILTER usando la condición definida
        if condition_name == "even":
            resultado = list(filter(lambda x: x % 2 == 0, self.numeros))
        elif condition_name == "odd":
            resultado = list(filter(lambda x: x % 2 != 0, self.numeros))
        elif condition_name == "asc":
            resultado = sorted(self.numeros)
        elif condition_name == "desc":
            resultado = sorted(self.numeros, reverse=True)
        else:
            print(f"Condition {condition_name} not supported.")
            return
        print(f"Result of FILTER: {resultado}")

def main(argv):
    # Recibir los números desde la consola o como argumentos
    if len(argv) > 2:
        numeros = list(map(int, argv[2:]))  # Los números ingresados como argumentos
    else:
        numeros = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))

    input_stream = FileStream(argv[1])
    lexer = MapFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.program()

    listener = MapFilterEvalListener(numeros)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
