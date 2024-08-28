import sys
from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor

class EvalVisitor(CalculatorVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Accede al operador usando ctx.op
        if ctx.op.type == CalculatorParser.MUL:
            return left * right
        elif ctx.op.type == CalculatorParser.DIV:
            return left / right
        else:
            raise Exception("Operador no soportado: " + ctx.op.getText())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == CalculatorParser.ADD:
            return left + right
        else:
            return left - right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitId(self, ctx):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        return 0

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

def main():
    while True:
        try:
            # Leer entrada desde la consola
            input_text = input('Ingrese una expresión (o "exit" para salir): ')
            if input_text.lower() == "exit":
                break
            
            final_input = input_text + "\n"
            input_stream = InputStream(final_input)
            lexer = CalculatorLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = CalculatorParser(token_stream)
            tree = parser.prog()

            eval_visitor = EvalVisitor()
            eval_visitor.visit(tree)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
