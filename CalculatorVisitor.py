# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#prog.
    def visitProg(self, ctx:CalculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#printExpr.
    def visitPrintExpr(self, ctx:CalculatorParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#assign.
    def visitAssign(self, ctx:CalculatorParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#blank.
    def visitBlank(self, ctx:CalculatorParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#parens.
    def visitParens(self, ctx:CalculatorParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#MulDiv.
    def visitMulDiv(self, ctx:CalculatorParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#AddSub.
    def visitAddSub(self, ctx:CalculatorParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#id.
    def visitId(self, ctx:CalculatorParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#int.
    def visitInt(self, ctx:CalculatorParser.IntContext):
        return self.visitChildren(ctx)



del CalculatorParser