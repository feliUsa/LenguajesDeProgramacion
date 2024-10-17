# Generated from appFuncion.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .appFuncionParser import appFuncionParser
else:
    from appFuncionParser import appFuncionParser

# This class defines a complete listener for a parse tree produced by appFuncionParser.
class appFuncionListener(ParseTreeListener):

    # Enter a parse tree produced by appFuncionParser#program.
    def enterProgram(self, ctx:appFuncionParser.ProgramContext):
        pass

    # Exit a parse tree produced by appFuncionParser#program.
    def exitProgram(self, ctx:appFuncionParser.ProgramContext):
        pass


    # Enter a parse tree produced by appFuncionParser#statement.
    def enterStatement(self, ctx:appFuncionParser.StatementContext):
        pass

    # Exit a parse tree produced by appFuncionParser#statement.
    def exitStatement(self, ctx:appFuncionParser.StatementContext):
        pass


    # Enter a parse tree produced by appFuncionParser#mapFunction.
    def enterMapFunction(self, ctx:appFuncionParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by appFuncionParser#mapFunction.
    def exitMapFunction(self, ctx:appFuncionParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by appFuncionParser#filterFunction.
    def enterFilterFunction(self, ctx:appFuncionParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by appFuncionParser#filterFunction.
    def exitFilterFunction(self, ctx:appFuncionParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by appFuncionParser#function.
    def enterFunction(self, ctx:appFuncionParser.FunctionContext):
        pass

    # Exit a parse tree produced by appFuncionParser#function.
    def exitFunction(self, ctx:appFuncionParser.FunctionContext):
        pass


    # Enter a parse tree produced by appFuncionParser#condition.
    def enterCondition(self, ctx:appFuncionParser.ConditionContext):
        pass

    # Exit a parse tree produced by appFuncionParser#condition.
    def exitCondition(self, ctx:appFuncionParser.ConditionContext):
        pass


    # Enter a parse tree produced by appFuncionParser#iterable.
    def enterIterable(self, ctx:appFuncionParser.IterableContext):
        pass

    # Exit a parse tree produced by appFuncionParser#iterable.
    def exitIterable(self, ctx:appFuncionParser.IterableContext):
        pass



del appFuncionParser