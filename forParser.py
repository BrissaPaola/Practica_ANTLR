# Generated from for.g4 by ANTLR 4.13.2
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
        4,1,21,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,
        41,9,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,58,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,69,8,3,
        10,3,12,3,72,9,3,1,3,0,1,6,4,0,2,4,6,0,3,1,0,9,10,1,0,11,12,1,0,
        13,16,80,0,9,1,0,0,0,2,44,1,0,0,0,4,46,1,0,0,0,6,57,1,0,0,0,8,10,
        3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,
        13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,45,3,4,2,0,16,17,5,1,0,
        0,17,45,3,6,3,0,18,19,5,2,0,0,19,20,3,6,3,0,20,24,5,3,0,0,21,23,
        3,2,1,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,
        25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,4,0,0,28,45,1,0,0,0,29,30,5,
        5,0,0,30,31,5,20,0,0,31,32,5,6,0,0,32,33,3,6,3,0,33,34,5,7,0,0,34,
        35,3,6,3,0,35,39,5,3,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,
        0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,
        5,4,0,0,43,45,1,0,0,0,44,15,1,0,0,0,44,16,1,0,0,0,44,18,1,0,0,0,
        44,29,1,0,0,0,45,3,1,0,0,0,46,47,5,20,0,0,47,48,5,8,0,0,48,49,3,
        6,3,0,49,5,1,0,0,0,50,51,6,3,-1,0,51,58,5,19,0,0,52,58,5,20,0,0,
        53,54,5,17,0,0,54,55,3,6,3,0,55,56,5,18,0,0,56,58,1,0,0,0,57,50,
        1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,58,70,1,0,0,0,59,60,10,6,0,0,
        60,61,7,0,0,0,61,69,3,6,3,7,62,63,10,5,0,0,63,64,7,1,0,0,64,69,3,
        6,3,6,65,66,10,4,0,0,66,67,7,2,0,0,67,69,3,6,3,5,68,59,1,0,0,0,68,
        62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,
        0,71,7,1,0,0,0,72,70,1,0,0,0,7,11,24,39,44,57,68,70
    ]

class forParser ( Parser ):

    grammarFileName = "for.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'while'", "'{'", "'}'", "'for'", 
                     "'='", "'to'", "'<-'", "'*'", "'/'", "'+'", "'-'", 
                     "'<'", "'>'", "'=='", "'!='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "VAR", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assign = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "stat", "assign", "expr" ]

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
    INT=19
    VAR=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(forParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.StatContext)
            else:
                return self.getTypedRuleContext(forParser.StatContext,i)


        def getRuleIndex(self):
            return forParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = forParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048614) != 0)):
                    break

            self.state = 13
            self.match(forParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(forParser.VAR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.StatContext)
            else:
                return self.getTypedRuleContext(forParser.StatContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStat" ):
                return visitor.visitForStat(self)
            else:
                return visitor.visitChildren(self)


    class AssignStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assign(self):
            return self.getTypedRuleContext(forParser.AssignContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.StatContext)
            else:
                return self.getTypedRuleContext(forParser.StatContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = forParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = forParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.assign()
                pass
            elif token in [1]:
                localctx = forParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(forParser.T__0)
                self.state = 17
                self.expr(0)
                pass
            elif token in [2]:
                localctx = forParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(forParser.T__1)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(forParser.T__2)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048614) != 0):
                    self.state = 21
                    self.stat()
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27
                self.match(forParser.T__3)
                pass
            elif token in [5]:
                localctx = forParser.ForStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(forParser.T__4)
                self.state = 30
                self.match(forParser.VAR)
                self.state = 31
                self.match(forParser.T__5)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(forParser.T__6)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(forParser.T__2)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048614) != 0):
                    self.state = 36
                    self.stat()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(forParser.T__3)
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(forParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def getRuleIndex(self):
            return forParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = forParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(forParser.VAR)
            self.state = 47
            self.match(forParser.T__7)
            self.state = 48
            self.expr(0)
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
            return forParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(forParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(forParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class CompContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = forParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = forParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                self.match(forParser.INT)
                pass
            elif token in [20]:
                localctx = forParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(forParser.VAR)
                pass
            elif token in [17]:
                localctx = forParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(forParser.T__16)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(forParser.T__17)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = forParser.MulDivContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 60
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = forParser.AddSubContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = forParser.CompContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(5)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




