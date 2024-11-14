# Generated from MLanguaje.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by MLanguajeParser#DeclareVarStmt.
    def enterDeclareVarStmt(self, ctx:MLanguajeParser.DeclareVarStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#DeclareVarStmt.
    def exitDeclareVarStmt(self, ctx:MLanguajeParser.DeclareVarStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ExprStmt.
    def enterExprStmt(self, ctx:MLanguajeParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ExprStmt.
    def exitExprStmt(self, ctx:MLanguajeParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#IfStmt.
    def enterIfStmt(self, ctx:MLanguajeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#IfStmt.
    def exitIfStmt(self, ctx:MLanguajeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#WhileStmt.
    def enterWhileStmt(self, ctx:MLanguajeParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#WhileStmt.
    def exitWhileStmt(self, ctx:MLanguajeParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ForStmt.
    def enterForStmt(self, ctx:MLanguajeParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ForStmt.
    def exitForStmt(self, ctx:MLanguajeParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#FileOpStmt.
    def enterFileOpStmt(self, ctx:MLanguajeParser.FileOpStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#FileOpStmt.
    def exitFileOpStmt(self, ctx:MLanguajeParser.FileOpStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#PlotOpStmt.
    def enterPlotOpStmt(self, ctx:MLanguajeParser.PlotOpStmtContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#PlotOpStmt.
    def exitPlotOpStmt(self, ctx:MLanguajeParser.PlotOpStmtContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MLanguajeParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MLanguajeParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#functionDecl.
    def enterFunctionDecl(self, ctx:MLanguajeParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#functionDecl.
    def exitFunctionDecl(self, ctx:MLanguajeParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#parameterList.
    def enterParameterList(self, ctx:MLanguajeParser.ParameterListContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#parameterList.
    def exitParameterList(self, ctx:MLanguajeParser.ParameterListContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#list.
    def enterList(self, ctx:MLanguajeParser.ListContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#list.
    def exitList(self, ctx:MLanguajeParser.ListContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#comparison.
    def enterComparison(self, ctx:MLanguajeParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#comparison.
    def exitComparison(self, ctx:MLanguajeParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ifStatement.
    def enterIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ifStatement.
    def exitIfStatement(self, ctx:MLanguajeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#whileStatement.
    def enterWhileStatement(self, ctx:MLanguajeParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#whileStatement.
    def exitWhileStatement(self, ctx:MLanguajeParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#forStatement.
    def enterForStatement(self, ctx:MLanguajeParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#forStatement.
    def exitForStatement(self, ctx:MLanguajeParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:MLanguajeParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:MLanguajeParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#StringExpr.
    def enterStringExpr(self, ctx:MLanguajeParser.StringExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#StringExpr.
    def exitStringExpr(self, ctx:MLanguajeParser.StringExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#PowerExpr.
    def enterPowerExpr(self, ctx:MLanguajeParser.PowerExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#PowerExpr.
    def exitPowerExpr(self, ctx:MLanguajeParser.PowerExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#TrigFunc.
    def enterTrigFunc(self, ctx:MLanguajeParser.TrigFuncContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#TrigFunc.
    def exitTrigFunc(self, ctx:MLanguajeParser.TrigFuncContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#TrueExpr.
    def enterTrueExpr(self, ctx:MLanguajeParser.TrueExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#TrueExpr.
    def exitTrueExpr(self, ctx:MLanguajeParser.TrueExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#NumberExpr.
    def enterNumberExpr(self, ctx:MLanguajeParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#NumberExpr.
    def exitNumberExpr(self, ctx:MLanguajeParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#MultExpr.
    def enterMultExpr(self, ctx:MLanguajeParser.MultExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#MultExpr.
    def exitMultExpr(self, ctx:MLanguajeParser.MultExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#CallFunc.
    def enterCallFunc(self, ctx:MLanguajeParser.CallFuncContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#CallFunc.
    def exitCallFunc(self, ctx:MLanguajeParser.CallFuncContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#VarExpr.
    def enterVarExpr(self, ctx:MLanguajeParser.VarExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#VarExpr.
    def exitVarExpr(self, ctx:MLanguajeParser.VarExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#AddExpr.
    def enterAddExpr(self, ctx:MLanguajeParser.AddExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#AddExpr.
    def exitAddExpr(self, ctx:MLanguajeParser.AddExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ListExpr.
    def enterListExpr(self, ctx:MLanguajeParser.ListExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ListExpr.
    def exitListExpr(self, ctx:MLanguajeParser.ListExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#ParenExpr.
    def enterParenExpr(self, ctx:MLanguajeParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#ParenExpr.
    def exitParenExpr(self, ctx:MLanguajeParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#FalseExpr.
    def enterFalseExpr(self, ctx:MLanguajeParser.FalseExprContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#FalseExpr.
    def exitFalseExpr(self, ctx:MLanguajeParser.FalseExprContext):
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


    # Enter a parse tree produced by MLanguajeParser#plotOperation.
    def enterPlotOperation(self, ctx:MLanguajeParser.PlotOperationContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#plotOperation.
    def exitPlotOperation(self, ctx:MLanguajeParser.PlotOperationContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#functionCall.
    def enterFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#functionCall.
    def exitFunctionCall(self, ctx:MLanguajeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#argumentList.
    def enterArgumentList(self, ctx:MLanguajeParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#argumentList.
    def exitArgumentList(self, ctx:MLanguajeParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MLanguajeParser#trigFunction.
    def enterTrigFunction(self, ctx:MLanguajeParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by MLanguajeParser#trigFunction.
    def exitTrigFunction(self, ctx:MLanguajeParser.TrigFunctionContext):
        pass



del MLanguajeParser