# Generated from transformadas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .transformadasParser import transformadasParser
else:
    from transformadasParser import transformadasParser

# This class defines a complete generic visitor for a parse tree produced by transformadasParser.

class transformadasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by transformadasParser#program.
    def visitProgram(self, ctx:transformadasParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by transformadasParser#FourierTransform.
    def visitFourierTransform(self, ctx:transformadasParser.FourierTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by transformadasParser#InverseFourierTransform.
    def visitInverseFourierTransform(self, ctx:transformadasParser.InverseFourierTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by transformadasParser#ArrayExpr.
    def visitArrayExpr(self, ctx:transformadasParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by transformadasParser#elements.
    def visitElements(self, ctx:transformadasParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by transformadasParser#complexNumber.
    def visitComplexNumber(self, ctx:transformadasParser.ComplexNumberContext):
        return self.visitChildren(ctx)



del transformadasParser