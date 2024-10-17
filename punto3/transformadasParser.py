# Generated from transformadas.g4 by ANTLR 4.13.2
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
        4,1,11,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,35,8,3,10,3,12,3,38,9,3,1,4,1,4,1,4,1,4,
        3,4,44,8,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,7,8,43,0,10,1,0,0,0,2,25,
        1,0,0,0,4,27,1,0,0,0,6,31,1,0,0,0,8,39,1,0,0,0,10,11,3,2,1,0,11,
        12,5,0,0,1,12,1,1,0,0,0,13,14,5,1,0,0,14,15,3,4,2,0,15,16,5,2,0,
        0,16,17,5,10,0,0,17,18,5,3,0,0,18,26,1,0,0,0,19,20,5,4,0,0,20,21,
        3,4,2,0,21,22,5,2,0,0,22,23,5,10,0,0,23,24,5,3,0,0,24,26,1,0,0,0,
        25,13,1,0,0,0,25,19,1,0,0,0,26,3,1,0,0,0,27,28,5,5,0,0,28,29,3,6,
        3,0,29,30,5,6,0,0,30,5,1,0,0,0,31,36,3,8,4,0,32,33,5,2,0,0,33,35,
        3,8,4,0,34,32,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,
        37,7,1,0,0,0,38,36,1,0,0,0,39,40,5,10,0,0,40,41,7,0,0,0,41,43,5,
        10,0,0,42,44,5,9,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,9,1,0,0,0,3,
        25,36,43
    ]

class transformadasParser ( Parser ):

    grammarFileName = "transformadas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fourier('", "','", "')'", "'inversa('", 
                     "'['", "']'", "'+'", "'-'", "'i'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_array = 2
    RULE_elements = 3
    RULE_complexNumber = 4

    ruleNames =  [ "program", "expr", "array", "elements", "complexNumber" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(transformadasParser.ExprContext,0)


        def EOF(self):
            return self.getToken(transformadasParser.EOF, 0)

        def getRuleIndex(self):
            return transformadasParser.RULE_program

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

        localctx = transformadasParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr()
            self.state = 11
            self.match(transformadasParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return transformadasParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FourierTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a transformadasParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(transformadasParser.ArrayContext,0)

        def NUMBER(self):
            return self.getToken(transformadasParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFourierTransform" ):
                listener.enterFourierTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFourierTransform" ):
                listener.exitFourierTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFourierTransform" ):
                return visitor.visitFourierTransform(self)
            else:
                return visitor.visitChildren(self)


    class InverseFourierTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a transformadasParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(transformadasParser.ArrayContext,0)

        def NUMBER(self):
            return self.getToken(transformadasParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInverseFourierTransform" ):
                listener.enterInverseFourierTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInverseFourierTransform" ):
                listener.exitInverseFourierTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInverseFourierTransform" ):
                return visitor.visitInverseFourierTransform(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = transformadasParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = transformadasParser.FourierTransformContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(transformadasParser.T__0)
                self.state = 14
                self.array()
                self.state = 15
                self.match(transformadasParser.T__1)
                self.state = 16
                self.match(transformadasParser.NUMBER)
                self.state = 17
                self.match(transformadasParser.T__2)
                pass
            elif token in [4]:
                localctx = transformadasParser.InverseFourierTransformContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(transformadasParser.T__3)
                self.state = 20
                self.array()
                self.state = 21
                self.match(transformadasParser.T__1)
                self.state = 22
                self.match(transformadasParser.NUMBER)
                self.state = 23
                self.match(transformadasParser.T__2)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return transformadasParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayExprContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a transformadasParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elements(self):
            return self.getTypedRuleContext(transformadasParser.ElementsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = transformadasParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        try:
            localctx = transformadasParser.ArrayExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(transformadasParser.T__4)
            self.state = 28
            self.elements()
            self.state = 29
            self.match(transformadasParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complexNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(transformadasParser.ComplexNumberContext)
            else:
                return self.getTypedRuleContext(transformadasParser.ComplexNumberContext,i)


        def getRuleIndex(self):
            return transformadasParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = transformadasParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.complexNumber()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 32
                self.match(transformadasParser.T__1)
                self.state = 33
                self.complexNumber()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(transformadasParser.NUMBER)
            else:
                return self.getToken(transformadasParser.NUMBER, i)

        def getRuleIndex(self):
            return transformadasParser.RULE_complexNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexNumber" ):
                listener.enterComplexNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexNumber" ):
                listener.exitComplexNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexNumber" ):
                return visitor.visitComplexNumber(self)
            else:
                return visitor.visitChildren(self)




    def complexNumber(self):

        localctx = transformadasParser.ComplexNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_complexNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(transformadasParser.NUMBER)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 41
            self.match(transformadasParser.NUMBER)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 42
                self.match(transformadasParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





