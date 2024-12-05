# Generated from MLanguaje.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MLanguajeParser import MLanguajeParser
else:
    from MLanguajeParser import MLanguajeParser

# This class defines a complete listener for a parse tree produced by MLanguajeParser.
class MLanguajeListener(ParseTreeListener):

    # Enter a parse tree produced by MLanguajeParser#program.
    def enterProgram(self, ctx:MLanguajeParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#program.
    def exitProgram(self, ctx:MLanguajeParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#statement.
    def enterStatement(self, ctx:MLanguajeParser.StatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#statement.
    def exitStatement(self, ctx:MLanguajeParser.StatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MLanguajeParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MLanguajeParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#printStatement.
    def enterPrintStatement(self, ctx:MLanguajeParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#printStatement.
    def exitPrintStatement(self, ctx:MLanguajeParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ifStatement.
    def enterIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ifStatement.
    def exitIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#whileLoop.
    def enterWhileLoop(self, ctx:MLanguajeParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#whileLoop.
    def exitWhileLoop(self, ctx:MLanguajeParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#forLoop.
    def enterForLoop(self, ctx:MLanguajeParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#forLoop.
    def exitForLoop(self, ctx:MLanguajeParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#list_.
    def enterList_(self, ctx:MLanguajeParser.List_Context):
        pass

    # Exit a parse tree produced by MLanguajeParser#list_.
    def exitList_(self, ctx:MLanguajeParser.List_Context):
        pass


    # Enter a parse tree produced by MLanguajeParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MLanguajeParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MLanguajeParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#expression.
    def enterExpression(self, ctx:MLanguajeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#expression.
    def exitExpression(self, ctx:MLanguajeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#matrixOperation.
    def enterMatrixOperation(self, ctx:MLanguajeParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#matrixOperation.
    def exitMatrixOperation(self, ctx:MLanguajeParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#fileOperation.
    def enterFileOperation(self, ctx:MLanguajeParser.FileOperationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#fileOperation.
    def exitFileOperation(self, ctx:MLanguajeParser.FileOperationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#visualization.
    def enterVisualization(self, ctx:MLanguajeParser.VisualizationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#visualization.
    def exitVisualization(self, ctx:MLanguajeParser.VisualizationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#plotLine.
    def enterPlotLine(self, ctx:MLanguajeParser.PlotLineContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#plotLine.
    def exitPlotLine(self, ctx:MLanguajeParser.PlotLineContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#plotBar.
    def enterPlotBar(self, ctx:MLanguajeParser.PlotBarContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#plotBar.
    def exitPlotBar(self, ctx:MLanguajeParser.PlotBarContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#plotHistogram.
    def enterPlotHistogram(self, ctx:MLanguajeParser.PlotHistogramContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#plotHistogram.
    def exitPlotHistogram(self, ctx:MLanguajeParser.PlotHistogramContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#plotScatter3D.
    def enterPlotScatter3D(self, ctx:MLanguajeParser.PlotScatter3DContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#plotScatter3D.
    def exitPlotScatter3D(self, ctx:MLanguajeParser.PlotScatter3DContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#condition.
    def enterCondition(self, ctx:MLanguajeParser.ConditionContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#condition.
    def exitCondition(self, ctx:MLanguajeParser.ConditionContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#functionCall.
    def enterFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#functionCall.
    def exitFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#rangeExpr.
    def enterRangeExpr(self, ctx:MLanguajeParser.RangeExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#rangeExpr.
    def exitRangeExpr(self, ctx:MLanguajeParser.RangeExprContext):
        pass



del MLanguajeParser