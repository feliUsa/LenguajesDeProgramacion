import sys
from antlr4 import *
from antlrEjecucion.MLanguajeLexer import MLanguajeLexer
from antlrEjecucion.MLanguajeParser import MLanguajeParser
from MLanguajeInterpreter import MLanguajeInterpreter


def main(argv):
    if len(argv) < 2:
        print("Uso: python main.py <archivo_entrada>")
        return

    # Abrir archivo de entrada y cargar el código fuente
    archivo_entrada = argv[1]
    with open(archivo_entrada, 'r') as file:
        codigo_fuente = file.read()

    # Crear lexer y parser para el lenguaje
    input_stream = InputStream(codigo_fuente)
    lexer = MLanguajeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MLanguajeParser(stream)

    # Realizar el análisis sintáctico
    tree = parser.program()

    # Crear y ejecutar el intérprete de MLanguaje
    interpreter = MLanguajeInterpreter()
    try:
        interpreter.visit(tree)
        print("Programa ejecutado exitosamente.")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == '__main__':
    main(sys.argv)
