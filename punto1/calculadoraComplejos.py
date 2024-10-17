from antlr4 import *
from complejosLexer import complejosLexer
from complejosParser import complejosParser
from complejosVisitor import complejosVisitor

class visitorClass(complejosVisitor):
    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        result = left + right
        return result

    def visitSubtract(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        result = left - right
        return result

    def visitComplexExpr(self, ctx):
        numReal = 0.0
        numComp = 0.0

        components = ctx.getText().split('i')[0]

        if '+' in components or '-' in components:
            parts = components.split('+') if '+' in components else components.split('-')
            numReal = float(parts[0].strip())
            numComp = float(parts[1].strip()) if '+' in components else -float(parts[1].strip())
        else:
            if 'i' in ctx.getText():
                numComp = float(components.strip())
            else:
                numReal = float(components.strip())
        return complex(numReal, numComp)

    def visitRealNumber(self, ctx):
        number = float(ctx.getText())
        return number

    def visitParentheses(self, ctx):
        return self.visit(ctx.expr())

    def visitFactor(self, ctx):
        # Parentesis
        if ctx.expr():
            return self.visit(ctx.expr())
        
        # Imaginario
        if ctx.complexNumber():
            return self.visitComplexExpr(ctx.complexNumber())
        
        # Real
        if ctx.NUMBER():
            return self.visitRealNumber(ctx)
        
        raise ValueError("Factor no reconocido en el contexto")

    def visitTerm(self, ctx):
        return self.visit(ctx.factor())

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

def main():
    expression = input("Introduce una expresion con numeros complejos: ")

    input_stream = InputStream(expression)
    lexer = complejosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = complejosParser(stream)
    tree = parser.program()

    visitor = visitorClass()
    result = visitor.visit(tree)
    print(f"Resultado\n{expression} = {result}")

if __name__ == "__main__":
    main()
