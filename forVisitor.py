# Generated from for.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete generic visitor for a parse tree produced by forParser.

class forVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by forParser#prog.
    def visitProg(self, ctx:forParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#AssignStat.
    def visitAssignStat(self, ctx:forParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#PrintStat.
    def visitPrintStat(self, ctx:forParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#WhileStat.
    def visitWhileStat(self, ctx:forParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#ForStat.
    def visitForStat(self, ctx:forParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#assign.
    def visitAssign(self, ctx:forParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#MulDiv.
    def visitMulDiv(self, ctx:forParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#AddSub.
    def visitAddSub(self, ctx:forParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Var.
    def visitVar(self, ctx:forParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Parens.
    def visitParens(self, ctx:forParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Int.
    def visitInt(self, ctx:forParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Comp.
    def visitComp(self, ctx:forParser.CompContext):
        return self.visitChildren(ctx)



del forParser