# Generated from MLanguaje.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MLanguajeParser import MLanguajeParser
else:
    from MLanguajeParser import MLanguajeParser

# This class defines a complete generic visitor for a parse tree produced by MLanguajeParser.

class MLanguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLanguajeParser#program.
    def visitProgram(self, ctx:MLanguajeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#statement.
    def visitStatement(self, ctx:MLanguajeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MLanguajeParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#printStatement.
    def visitPrintStatement(self, ctx:MLanguajeParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ifStatement.
    def visitIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#whileLoop.
    def visitWhileLoop(self, ctx:MLanguajeParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#forLoop.
    def visitForLoop(self, ctx:MLanguajeParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#listWithValues.
    def visitListWithValues(self, ctx:MLanguajeParser.ListWithValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MLanguajeParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#expression.
    def visitExpression(self, ctx:MLanguajeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#matrixOperation.
    def visitMatrixOperation(self, ctx:MLanguajeParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#fileOperation.
    def visitFileOperation(self, ctx:MLanguajeParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#visualization.
    def visitVisualization(self, ctx:MLanguajeParser.VisualizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#plotLine.
    def visitPlotLine(self, ctx:MLanguajeParser.PlotLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#plotBar.
    def visitPlotBar(self, ctx:MLanguajeParser.PlotBarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#plotHistogram.
    def visitPlotHistogram(self, ctx:MLanguajeParser.PlotHistogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#plotScatter3D.
    def visitPlotScatter3D(self, ctx:MLanguajeParser.PlotScatter3DContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#condition.
    def visitCondition(self, ctx:MLanguajeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#functionCall.
    def visitFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#rangeExpr.
    def visitRangeExpr(self, ctx:MLanguajeParser.RangeExprContext):
        return self.visitChildren(ctx)



del MLanguajeParser