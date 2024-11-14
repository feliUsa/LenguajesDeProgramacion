# Generated from MLanguaje.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by MLanguajeParser#DeclareVarStmt.
    def visitDeclareVarStmt(self, ctx:MLanguajeParser.DeclareVarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ExprStmt.
    def visitExprStmt(self, ctx:MLanguajeParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#IfStmt.
    def visitIfStmt(self, ctx:MLanguajeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#WhileStmt.
    def visitWhileStmt(self, ctx:MLanguajeParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ForStmt.
    def visitForStmt(self, ctx:MLanguajeParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#FileOpStmt.
    def visitFileOpStmt(self, ctx:MLanguajeParser.FileOpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#PlotOpStmt.
    def visitPlotOpStmt(self, ctx:MLanguajeParser.PlotOpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MLanguajeParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#functionDecl.
    def visitFunctionDecl(self, ctx:MLanguajeParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#parameterList.
    def visitParameterList(self, ctx:MLanguajeParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#list.
    def visitList(self, ctx:MLanguajeParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#comparison.
    def visitComparison(self, ctx:MLanguajeParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ifStatement.
    def visitIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#whileStatement.
    def visitWhileStatement(self, ctx:MLanguajeParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#forStatement.
    def visitForStatement(self, ctx:MLanguajeParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#PrimaryExpr.
    def visitPrimaryExpr(self, ctx:MLanguajeParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#StringExpr.
    def visitStringExpr(self, ctx:MLanguajeParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#PowerExpr.
    def visitPowerExpr(self, ctx:MLanguajeParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#TrigFunc.
    def visitTrigFunc(self, ctx:MLanguajeParser.TrigFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#TrueExpr.
    def visitTrueExpr(self, ctx:MLanguajeParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#NumberExpr.
    def visitNumberExpr(self, ctx:MLanguajeParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#MultExpr.
    def visitMultExpr(self, ctx:MLanguajeParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#CallFunc.
    def visitCallFunc(self, ctx:MLanguajeParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#VarExpr.
    def visitVarExpr(self, ctx:MLanguajeParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#AddExpr.
    def visitAddExpr(self, ctx:MLanguajeParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ListExpr.
    def visitListExpr(self, ctx:MLanguajeParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#ParenExpr.
    def visitParenExpr(self, ctx:MLanguajeParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#FalseExpr.
    def visitFalseExpr(self, ctx:MLanguajeParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#matrixOperation.
    def visitMatrixOperation(self, ctx:MLanguajeParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#fileOperation.
    def visitFileOperation(self, ctx:MLanguajeParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#plotOperation.
    def visitPlotOperation(self, ctx:MLanguajeParser.PlotOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#functionCall.
    def visitFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#argumentList.
    def visitArgumentList(self, ctx:MLanguajeParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLanguajeParser#trigFunction.
    def visitTrigFunction(self, ctx:MLanguajeParser.TrigFunctionContext):
        return self.visitChildren(ctx)



del MLanguajeParser