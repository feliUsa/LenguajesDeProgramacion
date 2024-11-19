import sys
from antlr4 import *
from antlrEjecucion.MLanguajeLexer import MLanguajeLexer
from antlrEjecucion.MLanguajeParser import MLanguajeParser
from MLanguajeInterpreter import MLanguajeInterpreter

def main(argv):
    if len(argv) < 2:
        print("Uso: python Main.py <archivo_entrada>")
        return

    archivo_entrada = argv[1]

    try:
        with open(archivo_entrada, 'r') as file:
            codigo_fuente = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no existe.")
        return

    print("Iniciando el procesamiento del código...")
    try:
        input_stream = InputStream(codigo_fuente)
        lexer = MLanguajeLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MLanguajeParser(stream)
        tree = parser.program()

        interpreter = MLanguajeInterpreter()
        interpreter.visit(tree)

        print("\n=== Resumen de la Ejecución ===")
        print(interpreter.get_summary())
        
    except Exception as e:
        print(f"Error durante el procesamiento o la interpretación: {e}")

if __name__ == "__main__":
    main(sys.argv)
