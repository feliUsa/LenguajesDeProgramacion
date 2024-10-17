# Generated from appFuncion.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .appFuncionParser import appFuncionParser
else:
    from appFuncionParser import appFuncionParser

# This class defines a complete generic visitor for a parse tree produced by appFuncionParser.

class appFuncionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by appFuncionParser#program.
    def visitProgram(self, ctx:appFuncionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#statement.
    def visitStatement(self, ctx:appFuncionParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#mapFunction.
    def visitMapFunction(self, ctx:appFuncionParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#filterFunction.
    def visitFilterFunction(self, ctx:appFuncionParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#function.
    def visitFunction(self, ctx:appFuncionParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#condition.
    def visitCondition(self, ctx:appFuncionParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by appFuncionParser#iterable.
    def visitIterable(self, ctx:appFuncionParser.IterableContext):
        return self.visitChildren(ctx)



del appFuncionParser