# Generated from appFuncion.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,40,0,15,1,0,0,0,2,23,1,0,0,0,
        4,25,1,0,0,0,6,32,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,0,12,43,1,0,0,
        0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,
        1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,24,3,4,2,0,22,
        24,3,6,3,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,0,
        0,26,27,5,2,0,0,27,28,3,8,4,0,28,29,5,3,0,0,29,30,3,12,6,0,30,31,
        5,4,0,0,31,5,1,0,0,0,32,33,5,5,0,0,33,34,5,2,0,0,34,35,3,10,5,0,
        35,36,5,3,0,0,36,37,3,12,6,0,37,38,5,4,0,0,38,7,1,0,0,0,39,40,5,
        6,0,0,40,9,1,0,0,0,41,42,5,6,0,0,42,11,1,0,0,0,43,44,5,6,0,0,44,
        13,1,0,0,0,2,17,23
    ]

class appFuncionParser ( Parser ):

    grammarFileName = "appFuncion.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mapFunction = 2
    RULE_filterFunction = 3
    RULE_function = 4
    RULE_condition = 5
    RULE_iterable = 6

    ruleNames =  [ "program", "statement", "mapFunction", "filterFunction", 
                   "function", "condition", "iterable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IDENTIFIER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(appFuncionParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(appFuncionParser.StatementContext)
            else:
                return self.getTypedRuleContext(appFuncionParser.StatementContext,i)


        def getRuleIndex(self):
            return appFuncionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = appFuncionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

            self.state = 19
            self.match(appFuncionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapFunction(self):
            return self.getTypedRuleContext(appFuncionParser.MapFunctionContext,0)


        def filterFunction(self):
            return self.getTypedRuleContext(appFuncionParser.FilterFunctionContext,0)


        def getRuleIndex(self):
            return appFuncionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = appFuncionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.mapFunction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.filterFunction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(appFuncionParser.FunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(appFuncionParser.IterableContext,0)


        def getRuleIndex(self):
            return appFuncionParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = appFuncionParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(appFuncionParser.T__0)
            self.state = 26
            self.match(appFuncionParser.T__1)
            self.state = 27
            self.function()
            self.state = 28
            self.match(appFuncionParser.T__2)
            self.state = 29
            self.iterable()
            self.state = 30
            self.match(appFuncionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(appFuncionParser.ConditionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(appFuncionParser.IterableContext,0)


        def getRuleIndex(self):
            return appFuncionParser.RULE_filterFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunction" ):
                listener.enterFilterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunction" ):
                listener.exitFilterFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterFunction" ):
                return visitor.visitFilterFunction(self)
            else:
                return visitor.visitChildren(self)




    def filterFunction(self):

        localctx = appFuncionParser.FilterFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(appFuncionParser.T__4)
            self.state = 33
            self.match(appFuncionParser.T__1)
            self.state = 34
            self.condition()
            self.state = 35
            self.match(appFuncionParser.T__2)
            self.state = 36
            self.iterable()
            self.state = 37
            self.match(appFuncionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(appFuncionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return appFuncionParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = appFuncionParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(appFuncionParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(appFuncionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return appFuncionParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = appFuncionParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(appFuncionParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(appFuncionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return appFuncionParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = appFuncionParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_iterable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(appFuncionParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





