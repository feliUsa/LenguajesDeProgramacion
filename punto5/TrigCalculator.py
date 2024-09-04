import sys
from antlr4 import *
from TrigLexer import TrigLexer
from TrigParser import TrigParser
from TrigVisitorImpl import TrigVisitorImpl

def main(argv):
    input_file = FileStream(argv[1])
    lexer = TrigLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = TrigParser(stream)
    tree = parser.prog()

    visitor = TrigVisitorImpl()

    # Visitar todas las expresiones y acumular resultados
    results = [visitor.visit(child) for child in tree.children]

    # Imprimir resultados
    for result in results:
        print(result)

if __name__ == '__main__':
    main(sys.argv)
