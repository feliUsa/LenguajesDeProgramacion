import sys
from antlr4 import *
from appFuncionLexer import appFuncionLexer
from appFuncionParser import appFuncionParser

# Función auxiliar para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class funcionMapFilterEvalListener(ParseTreeListener):
    def __init__(self, numList):
        self.numList = numList

    def exitMapFunction(self, ctx):
        function_name = ctx.function().getText()
        print(f"{function_name}({self.numList})")

        # Aplicar MAP usando la función definida
        if function_name == "square":
            resultado = list(map(lambda x: x ** 2, self.numList))
        elif function_name == "cube":
            resultado = list(map(lambda x: x ** 3, self.numList))
        elif function_name == "double":
            resultado = list(map(lambda x: x * 2, self.numList))
        elif function_name == "neg":
            resultado = list(map(lambda x: -x, self.numList))
        elif function_name == "even_to_zero":
            resultado = list(map(lambda x: 0 if x % 2 == 0 else x, self.numList))
        elif function_name == "is_prime":
            resultado = list(map(is_prime, self.numnumListeros))
        else:
            print(f"Function {function_name} not supported.")
            return
        print(f"Result of MAP: {resultado}")

    def exitFilterFunction(self, ctx):
        condition_name = ctx.condition().getText()
        print(f"{condition_name}({self.numList})")

        # Aplicar FILTER usando la condición definida
        if condition_name == "par":
            resultado = list(filter(lambda x: x % 2 == 0, self.numList))
        elif condition_name == "impar":
            resultado = list(filter(lambda x: x % 2 != 0, self.numList))
        elif condition_name == "sort":
            resultado = sorted(self.numList)
        elif condition_name == "reverseSort":
            resultado = sorted(self.numList, reverse=True)
        else:
            print(f"Condition {condition_name} not supported.")
            return
        print(f"Result of FILTER: {resultado}")

def main(argv):
    # Recibir los números desde la consola o como argumentos
    if len(argv) > 2:
        numList = list(map(int, argv[2:]))  # Los números ingresados como argumentos
    else:
        numList = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))

    input_stream = FileStream(argv[1])
    lexer = appFuncionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = appFuncionParser(stream)
    tree = parser.program()

    listener = funcionMapFilterEvalListener(numList)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
