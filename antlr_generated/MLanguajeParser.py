# Generated from MLanguaje.g4 by ANTLR 4.13.1
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
        4,1,50,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,73,8,4,10,4,12,4,76,9,4,1,4,1,4,1,4,1,4,5,4,82,8,4,10,4,12,4,85,
        9,4,1,4,3,4,88,8,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,96,8,5,11,5,12,5,
        97,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,108,8,6,10,6,12,6,111,9,6,
        1,6,1,6,1,7,1,7,1,7,1,7,5,7,119,8,7,10,7,12,7,122,9,7,1,7,1,7,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,159,8,9,1,9,1,9,1,9,5,9,164,8,9,10,9,12,9,167,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,193,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,216,8,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        246,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,257,8,
        14,1,14,1,14,1,14,0,1,18,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,0,3,1,1,48,48,1,0,16,20,1,0,37,42,284,0,34,1,0,0,0,2,49,1,0,0,
        0,4,51,1,0,0,0,6,57,1,0,0,0,8,66,1,0,0,0,10,89,1,0,0,0,12,101,1,
        0,0,0,14,114,1,0,0,0,16,125,1,0,0,0,18,158,1,0,0,0,20,192,1,0,0,
        0,22,215,1,0,0,0,24,245,1,0,0,0,26,247,1,0,0,0,28,251,1,0,0,0,30,
        33,3,2,1,0,31,33,5,48,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,
        0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,
        5,0,0,1,38,1,1,0,0,0,39,50,3,4,2,0,40,50,3,6,3,0,41,50,3,8,4,0,42,
        50,3,10,5,0,43,50,3,12,6,0,44,50,3,16,8,0,45,50,3,20,10,0,46,50,
        3,22,11,0,47,50,3,24,12,0,48,50,5,48,0,0,49,39,1,0,0,0,49,40,1,0,
        0,0,49,41,1,0,0,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,
        1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,
        52,5,1,0,0,52,53,5,44,0,0,53,54,5,2,0,0,54,55,3,18,9,0,55,56,7,0,
        0,0,56,5,1,0,0,0,57,58,5,3,0,0,58,61,5,4,0,0,59,62,5,45,0,0,60,62,
        3,18,9,0,61,59,1,0,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,64,5,5,0,0,
        64,65,7,0,0,0,65,7,1,0,0,0,66,67,5,6,0,0,67,68,5,4,0,0,68,69,3,26,
        13,0,69,70,5,5,0,0,70,74,5,7,0,0,71,73,3,2,1,0,72,71,1,0,0,0,73,
        76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,
        0,77,87,5,8,0,0,78,79,5,9,0,0,79,83,5,7,0,0,80,82,3,2,1,0,81,80,
        1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,
        85,83,1,0,0,0,86,88,5,8,0,0,87,78,1,0,0,0,87,88,1,0,0,0,88,9,1,0,
        0,0,89,90,5,10,0,0,90,91,5,4,0,0,91,92,3,26,13,0,92,93,5,5,0,0,93,
        95,5,7,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,
        0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,8,0,0,100,11,1,0,0,0,101,
        102,5,11,0,0,102,103,5,44,0,0,103,104,5,12,0,0,104,105,3,18,9,0,
        105,109,5,7,0,0,106,108,3,2,1,0,107,106,1,0,0,0,108,111,1,0,0,0,
        109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,
        112,113,5,8,0,0,113,13,1,0,0,0,114,115,5,13,0,0,115,120,3,18,9,0,
        116,117,5,14,0,0,117,119,3,18,9,0,118,116,1,0,0,0,119,122,1,0,0,
        0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,
        0,123,124,5,15,0,0,124,15,1,0,0,0,125,126,3,18,9,0,126,127,7,0,0,
        0,127,17,1,0,0,0,128,129,6,9,-1,0,129,130,5,21,0,0,130,131,5,4,0,
        0,131,132,3,18,9,0,132,133,5,5,0,0,133,159,1,0,0,0,134,135,5,22,
        0,0,135,136,5,4,0,0,136,137,3,18,9,0,137,138,5,5,0,0,138,159,1,0,
        0,0,139,140,5,23,0,0,140,141,5,4,0,0,141,142,3,18,9,0,142,143,5,
        14,0,0,143,144,3,18,9,0,144,145,5,5,0,0,145,159,1,0,0,0,146,147,
        5,24,0,0,147,148,5,4,0,0,148,149,3,18,9,0,149,150,5,5,0,0,150,159,
        1,0,0,0,151,159,3,14,7,0,152,159,3,28,14,0,153,159,3,20,10,0,154,
        159,5,46,0,0,155,159,5,47,0,0,156,159,5,44,0,0,157,159,5,45,0,0,
        158,128,1,0,0,0,158,134,1,0,0,0,158,139,1,0,0,0,158,146,1,0,0,0,
        158,151,1,0,0,0,158,152,1,0,0,0,158,153,1,0,0,0,158,154,1,0,0,0,
        158,155,1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,0,159,165,1,0,0,0,
        160,161,10,12,0,0,161,162,7,1,0,0,162,164,3,18,9,13,163,160,1,0,
        0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,19,1,0,0,
        0,167,165,1,0,0,0,168,169,5,25,0,0,169,170,5,4,0,0,170,171,3,18,
        9,0,171,172,5,14,0,0,172,173,3,18,9,0,173,174,5,5,0,0,174,193,1,
        0,0,0,175,176,5,26,0,0,176,177,5,4,0,0,177,178,3,18,9,0,178,179,
        5,14,0,0,179,180,3,18,9,0,180,181,5,5,0,0,181,193,1,0,0,0,182,183,
        5,27,0,0,183,184,5,4,0,0,184,185,3,18,9,0,185,186,5,5,0,0,186,193,
        1,0,0,0,187,188,5,28,0,0,188,189,5,4,0,0,189,190,3,18,9,0,190,191,
        5,5,0,0,191,193,1,0,0,0,192,168,1,0,0,0,192,175,1,0,0,0,192,182,
        1,0,0,0,192,187,1,0,0,0,193,21,1,0,0,0,194,195,5,29,0,0,195,196,
        5,4,0,0,196,197,5,45,0,0,197,198,5,14,0,0,198,199,5,45,0,0,199,216,
        5,5,0,0,200,201,5,30,0,0,201,202,5,4,0,0,202,203,5,45,0,0,203,216,
        5,5,0,0,204,205,5,31,0,0,205,206,5,4,0,0,206,207,5,45,0,0,207,208,
        5,14,0,0,208,209,3,18,9,0,209,210,5,5,0,0,210,216,1,0,0,0,211,212,
        5,32,0,0,212,213,5,4,0,0,213,214,5,45,0,0,214,216,5,5,0,0,215,194,
        1,0,0,0,215,200,1,0,0,0,215,204,1,0,0,0,215,211,1,0,0,0,216,23,1,
        0,0,0,217,218,5,33,0,0,218,219,5,4,0,0,219,220,3,18,9,0,220,221,
        5,14,0,0,221,222,3,18,9,0,222,223,5,5,0,0,223,246,1,0,0,0,224,225,
        5,34,0,0,225,226,5,4,0,0,226,227,3,18,9,0,227,228,5,14,0,0,228,229,
        3,18,9,0,229,230,5,5,0,0,230,246,1,0,0,0,231,232,5,35,0,0,232,233,
        5,4,0,0,233,234,3,18,9,0,234,235,5,5,0,0,235,246,1,0,0,0,236,237,
        5,36,0,0,237,238,5,4,0,0,238,239,3,18,9,0,239,240,5,14,0,0,240,241,
        3,18,9,0,241,242,5,14,0,0,242,243,3,18,9,0,243,244,5,5,0,0,244,246,
        1,0,0,0,245,217,1,0,0,0,245,224,1,0,0,0,245,231,1,0,0,0,245,236,
        1,0,0,0,246,25,1,0,0,0,247,248,3,18,9,0,248,249,7,2,0,0,249,250,
        3,18,9,0,250,27,1,0,0,0,251,252,5,43,0,0,252,253,5,4,0,0,253,256,
        5,46,0,0,254,255,5,14,0,0,255,257,5,46,0,0,256,254,1,0,0,0,256,257,
        1,0,0,0,257,258,1,0,0,0,258,259,5,5,0,0,259,29,1,0,0,0,16,32,34,
        49,61,74,83,87,97,109,120,158,165,192,215,245,256
    ]

class MLanguajeParser ( Parser ):

    grammarFileName = "MLanguaje.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "'print'", "'('", "')'", 
                     "'if'", "'{'", "'}'", "'else'", "'while'", "'for'", 
                     "'in'", "'['", "','", "']'", "'+'", "'-'", "'*'", "'/'", 
                     "'**'", "'sin'", "'cos'", "'power'", "'sqrt'", "'addMatrix'", 
                     "'multiplyMatrix'", "'transposeMatrix'", "'inverseMatrix'", 
                     "'writeFile'", "'readFile'", "'writeCSV'", "'readCSV'", 
                     "'plotLine'", "'plotBar'", "'plotHistogram'", "'plotScatter3D'", 
                     "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", "'range'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "STRING", "INT", "FLOAT", "NEWLINE", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_printStatement = 3
    RULE_ifStatement = 4
    RULE_whileLoop = 5
    RULE_forLoop = 6
    RULE_list_ = 7
    RULE_expressionStatement = 8
    RULE_expression = 9
    RULE_matrixOperation = 10
    RULE_fileOperation = 11
    RULE_visualization = 12
    RULE_condition = 13
    RULE_rangeExpr = 14

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "ifStatement", "whileLoop", "forLoop", "list_", "expressionStatement", 
                   "expression", "matrixOperation", "fileOperation", "visualization", 
                   "condition", "rangeExpr" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    ID=44
    STRING=45
    INT=46
    FLOAT=47
    NEWLINE=48
    WS=49
    LINE_COMMENT=50

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
            return self.getToken(MLanguajeParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MLanguajeParser.NEWLINE)
            else:
                return self.getToken(MLanguajeParser.NEWLINE, i)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_program

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

        localctx = MLanguajeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554291297266762) != 0):
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.match(MLanguajeParser.NEWLINE)
                    pass


                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(MLanguajeParser.EOF)
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(MLanguajeParser.VariableDeclarationContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MLanguajeParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MLanguajeParser.IfStatementContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(MLanguajeParser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MLanguajeParser.ForLoopContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionStatementContext,0)


        def matrixOperation(self):
            return self.getTypedRuleContext(MLanguajeParser.MatrixOperationContext,0)


        def fileOperation(self):
            return self.getTypedRuleContext(MLanguajeParser.FileOperationContext,0)


        def visualization(self):
            return self.getTypedRuleContext(MLanguajeParser.VisualizationContext,0)


        def NEWLINE(self):
            return self.getToken(MLanguajeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_statement

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

        localctx = MLanguajeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.whileLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.expressionStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.matrixOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.fileOperation()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 47
                self.visualization()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 48
                self.match(MLanguajeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLanguajeParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(MLanguajeParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(MLanguajeParser.EOF, 0)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MLanguajeParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MLanguajeParser.T__0)
            self.state = 52
            self.match(MLanguajeParser.ID)
            self.state = 53
            self.match(MLanguajeParser.T__1)
            self.state = 54
            self.expression(0)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==-1 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MLanguajeParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(MLanguajeParser.EOF, 0)

        def STRING(self):
            return self.getToken(MLanguajeParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = MLanguajeParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MLanguajeParser.T__2)
            self.state = 58
            self.match(MLanguajeParser.T__3)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 59
                self.match(MLanguajeParser.STRING)
                pass

            elif la_ == 2:
                self.state = 60
                self.expression(0)
                pass


            self.state = 63
            self.match(MLanguajeParser.T__4)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==-1 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MLanguajeParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.StatementContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MLanguajeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MLanguajeParser.T__5)
            self.state = 67
            self.match(MLanguajeParser.T__3)
            self.state = 68
            self.condition()
            self.state = 69
            self.match(MLanguajeParser.T__4)
            self.state = 70
            self.match(MLanguajeParser.T__6)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554291297266762) != 0):
                self.state = 71
                self.statement()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(MLanguajeParser.T__7)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 78
                self.match(MLanguajeParser.T__8)
                self.state = 79
                self.match(MLanguajeParser.T__6)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554291297266762) != 0):
                    self.state = 80
                    self.statement()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(MLanguajeParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MLanguajeParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.StatementContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = MLanguajeParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MLanguajeParser.T__9)
            self.state = 90
            self.match(MLanguajeParser.T__3)
            self.state = 91
            self.condition()
            self.state = 92
            self.match(MLanguajeParser.T__4)
            self.state = 93
            self.match(MLanguajeParser.T__6)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.statement()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 554291297266762) != 0)):
                    break

            self.state = 99
            self.match(MLanguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLanguajeParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.StatementContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MLanguajeParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MLanguajeParser.T__10)
            self.state = 102
            self.match(MLanguajeParser.ID)
            self.state = 103
            self.match(MLanguajeParser.T__11)

            self.state = 104
            self.expression(0)
            self.state = 105
            self.match(MLanguajeParser.T__6)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554291297266762) != 0):
                self.state = 106
                self.statement()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(MLanguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_list_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_" ):
                listener.enterList_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_" ):
                listener.exitList_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_" ):
                return visitor.visitList_(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MLanguajeParser.List_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MLanguajeParser.T__12)
            self.state = 115
            self.expression(0)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 116
                self.match(MLanguajeParser.T__13)
                self.state = 117
                self.expression(0)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(MLanguajeParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(MLanguajeParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(MLanguajeParser.EOF, 0)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MLanguajeParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression(0)
            self.state = 126
            _la = self._input.LA(1)
            if not(_la==-1 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,i)


        def list_(self):
            return self.getTypedRuleContext(MLanguajeParser.List_Context,0)


        def rangeExpr(self):
            return self.getTypedRuleContext(MLanguajeParser.RangeExprContext,0)


        def matrixOperation(self):
            return self.getTypedRuleContext(MLanguajeParser.MatrixOperationContext,0)


        def INT(self):
            return self.getToken(MLanguajeParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MLanguajeParser.FLOAT, 0)

        def ID(self):
            return self.getToken(MLanguajeParser.ID, 0)

        def STRING(self):
            return self.getToken(MLanguajeParser.STRING, 0)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MLanguajeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 129
                self.match(MLanguajeParser.T__20)
                self.state = 130
                self.match(MLanguajeParser.T__3)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [22]:
                self.state = 134
                self.match(MLanguajeParser.T__21)
                self.state = 135
                self.match(MLanguajeParser.T__3)
                self.state = 136
                self.expression(0)
                self.state = 137
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [23]:
                self.state = 139
                self.match(MLanguajeParser.T__22)
                self.state = 140
                self.match(MLanguajeParser.T__3)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(MLanguajeParser.T__13)
                self.state = 143
                self.expression(0)
                self.state = 144
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [24]:
                self.state = 146
                self.match(MLanguajeParser.T__23)
                self.state = 147
                self.match(MLanguajeParser.T__3)
                self.state = 148
                self.expression(0)
                self.state = 149
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [13]:
                self.state = 151
                self.list_()
                pass
            elif token in [43]:
                self.state = 152
                self.rangeExpr()
                pass
            elif token in [25, 26, 27, 28]:
                self.state = 153
                self.matrixOperation()
                pass
            elif token in [46]:
                self.state = 154
                self.match(MLanguajeParser.INT)
                pass
            elif token in [47]:
                self.state = 155
                self.match(MLanguajeParser.FLOAT)
                pass
            elif token in [44]:
                self.state = 156
                self.match(MLanguajeParser.ID)
                pass
            elif token in [45]:
                self.state = 157
                self.match(MLanguajeParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MLanguajeParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 160
                    if not self.precpred(self._ctx, 12):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                    self.state = 161
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2031616) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 162
                    self.expression(13) 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrixOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_matrixOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixOperation" ):
                listener.enterMatrixOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixOperation" ):
                listener.exitMatrixOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixOperation" ):
                return visitor.visitMatrixOperation(self)
            else:
                return visitor.visitChildren(self)




    def matrixOperation(self):

        localctx = MLanguajeParser.MatrixOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_matrixOperation)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(MLanguajeParser.T__24)
                self.state = 169
                self.match(MLanguajeParser.T__3)
                self.state = 170
                self.expression(0)
                self.state = 171
                self.match(MLanguajeParser.T__13)
                self.state = 172
                self.expression(0)
                self.state = 173
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MLanguajeParser.T__25)
                self.state = 176
                self.match(MLanguajeParser.T__3)
                self.state = 177
                self.expression(0)
                self.state = 178
                self.match(MLanguajeParser.T__13)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(MLanguajeParser.T__26)
                self.state = 183
                self.match(MLanguajeParser.T__3)
                self.state = 184
                self.expression(0)
                self.state = 185
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(MLanguajeParser.T__27)
                self.state = 188
                self.match(MLanguajeParser.T__3)
                self.state = 189
                self.expression(0)
                self.state = 190
                self.match(MLanguajeParser.T__4)
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


    class FileOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MLanguajeParser.STRING)
            else:
                return self.getToken(MLanguajeParser.STRING, i)

        def expression(self):
            return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_fileOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileOperation" ):
                listener.enterFileOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileOperation" ):
                listener.exitFileOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileOperation" ):
                return visitor.visitFileOperation(self)
            else:
                return visitor.visitChildren(self)




    def fileOperation(self):

        localctx = MLanguajeParser.FileOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fileOperation)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MLanguajeParser.T__28)
                self.state = 195
                self.match(MLanguajeParser.T__3)
                self.state = 196
                self.match(MLanguajeParser.STRING)
                self.state = 197
                self.match(MLanguajeParser.T__13)
                self.state = 198
                self.match(MLanguajeParser.STRING)
                self.state = 199
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(MLanguajeParser.T__29)
                self.state = 201
                self.match(MLanguajeParser.T__3)
                self.state = 202
                self.match(MLanguajeParser.STRING)
                self.state = 203
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(MLanguajeParser.T__30)
                self.state = 205
                self.match(MLanguajeParser.T__3)
                self.state = 206
                self.match(MLanguajeParser.STRING)
                self.state = 207
                self.match(MLanguajeParser.T__13)
                self.state = 208
                self.expression(0)
                self.state = 209
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.match(MLanguajeParser.T__31)
                self.state = 212
                self.match(MLanguajeParser.T__3)
                self.state = 213
                self.match(MLanguajeParser.STRING)
                self.state = 214
                self.match(MLanguajeParser.T__4)
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


    class VisualizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_visualization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualization" ):
                listener.enterVisualization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualization" ):
                listener.exitVisualization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualization" ):
                return visitor.visitVisualization(self)
            else:
                return visitor.visitChildren(self)




    def visualization(self):

        localctx = MLanguajeParser.VisualizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_visualization)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(MLanguajeParser.T__32)
                self.state = 218
                self.match(MLanguajeParser.T__3)
                self.state = 219
                self.expression(0)
                self.state = 220
                self.match(MLanguajeParser.T__13)
                self.state = 221
                self.expression(0)
                self.state = 222
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(MLanguajeParser.T__33)
                self.state = 225
                self.match(MLanguajeParser.T__3)
                self.state = 226
                self.expression(0)
                self.state = 227
                self.match(MLanguajeParser.T__13)
                self.state = 228
                self.expression(0)
                self.state = 229
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(MLanguajeParser.T__34)
                self.state = 232
                self.match(MLanguajeParser.T__3)
                self.state = 233
                self.expression(0)
                self.state = 234
                self.match(MLanguajeParser.T__4)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(MLanguajeParser.T__35)
                self.state = 237
                self.match(MLanguajeParser.T__3)
                self.state = 238
                self.expression(0)
                self.state = 239
                self.match(MLanguajeParser.T__13)
                self.state = 240
                self.expression(0)
                self.state = 241
                self.match(MLanguajeParser.T__13)
                self.state = 242
                self.expression(0)
                self.state = 243
                self.match(MLanguajeParser.T__4)
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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLanguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MLanguajeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MLanguajeParser.RULE_condition

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

        localctx = MLanguajeParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.expression(0)
            self.state = 248
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8658654068736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 249
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MLanguajeParser.INT)
            else:
                return self.getToken(MLanguajeParser.INT, i)

        def getRuleIndex(self):
            return MLanguajeParser.RULE_rangeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpr" ):
                listener.enterRangeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpr" ):
                listener.exitRangeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeExpr" ):
                return visitor.visitRangeExpr(self)
            else:
                return visitor.visitChildren(self)




    def rangeExpr(self):

        localctx = MLanguajeParser.RangeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rangeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MLanguajeParser.T__42)
            self.state = 252
            self.match(MLanguajeParser.T__3)
            self.state = 253
            self.match(MLanguajeParser.INT)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 254
                self.match(MLanguajeParser.T__13)
                self.state = 255
                self.match(MLanguajeParser.INT)


            self.state = 258
            self.match(MLanguajeParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         




