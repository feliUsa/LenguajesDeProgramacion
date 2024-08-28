# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#prog.
    def enterProg(self, ctx:CalculatorParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculatorParser#prog.
    def exitProg(self, ctx:CalculatorParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculatorParser#printExpr.
    def enterPrintExpr(self, ctx:CalculatorParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#printExpr.
    def exitPrintExpr(self, ctx:CalculatorParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#assign.
    def enterAssign(self, ctx:CalculatorParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculatorParser#assign.
    def exitAssign(self, ctx:CalculatorParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculatorParser#blank.
    def enterBlank(self, ctx:CalculatorParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculatorParser#blank.
    def exitBlank(self, ctx:CalculatorParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculatorParser#parens.
    def enterParens(self, ctx:CalculatorParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculatorParser#parens.
    def exitParens(self, ctx:CalculatorParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculatorParser#MulDiv.
    def enterMulDiv(self, ctx:CalculatorParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculatorParser#MulDiv.
    def exitMulDiv(self, ctx:CalculatorParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculatorParser#AddSub.
    def enterAddSub(self, ctx:CalculatorParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculatorParser#AddSub.
    def exitAddSub(self, ctx:CalculatorParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculatorParser#id.
    def enterId(self, ctx:CalculatorParser.IdContext):
        pass

    # Exit a parse tree produced by CalculatorParser#id.
    def exitId(self, ctx:CalculatorParser.IdContext):
        pass


    # Enter a parse tree produced by CalculatorParser#int.
    def enterInt(self, ctx:CalculatorParser.IntContext):
        pass

    # Exit a parse tree produced by CalculatorParser#int.
    def exitInt(self, ctx:CalculatorParser.IntContext):
        pass



del CalculatorParser