import sys
from antlr4 import *
from antlr_generated.MLanguajeLexer import MLanguajeLexer
from antlr_generated.MLanguajeParser import MLanguajeParser
from MLanguajeInterpreter import MLanguajeVisitorImplementation

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MLanguajeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MLanguajeParser(stream)
    tree = parser.program()
    visitor = MLanguajeVisitorImplementation()
    visitor.visit(tree)
    #print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main(sys.argv)
