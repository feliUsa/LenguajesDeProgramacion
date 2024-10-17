# Generated from transformadas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .transformadasParser import transformadasParser
else:
    from transformadasParser import transformadasParser

# This class defines a complete listener for a parse tree produced by transformadasParser.
class transformadasListener(ParseTreeListener):

    # Enter a parse tree produced by transformadasParser#program.
    def enterProgram(self, ctx:transformadasParser.ProgramContext):
        pass

    # Exit a parse tree produced by transformadasParser#program.
    def exitProgram(self, ctx:transformadasParser.ProgramContext):
        pass


    # Enter a parse tree produced by transformadasParser#FourierTransform.
    def enterFourierTransform(self, ctx:transformadasParser.FourierTransformContext):
        pass

    # Exit a parse tree produced by transformadasParser#FourierTransform.
    def exitFourierTransform(self, ctx:transformadasParser.FourierTransformContext):
        pass


    # Enter a parse tree produced by transformadasParser#InverseFourierTransform.
    def enterInverseFourierTransform(self, ctx:transformadasParser.InverseFourierTransformContext):
        pass

    # Exit a parse tree produced by transformadasParser#InverseFourierTransform.
    def exitInverseFourierTransform(self, ctx:transformadasParser.InverseFourierTransformContext):
        pass


    # Enter a parse tree produced by transformadasParser#ArrayExpr.
    def enterArrayExpr(self, ctx:transformadasParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by transformadasParser#ArrayExpr.
    def exitArrayExpr(self, ctx:transformadasParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by transformadasParser#elements.
    def enterElements(self, ctx:transformadasParser.ElementsContext):
        pass

    # Exit a parse tree produced by transformadasParser#elements.
    def exitElements(self, ctx:transformadasParser.ElementsContext):
        pass


    # Enter a parse tree produced by transformadasParser#complexNumber.
    def enterComplexNumber(self, ctx:transformadasParser.ComplexNumberContext):
        pass

    # Exit a parse tree produced by transformadasParser#complexNumber.
    def exitComplexNumber(self, ctx:transformadasParser.ComplexNumberContext):
        pass



del transformadasParser