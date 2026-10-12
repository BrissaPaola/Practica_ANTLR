from forVisitor import forVisitor
class EvalVisitor(forVisitor):
    def __init__(self):
        self.tabla = {} 
    def visitProg(self, ctx):
        for s in ctx.stat():
            self.visit(s)
    def visitAssignStat(self, ctx):
        self.visit(ctx.assign())
    def visitAssign(self, ctx):
        nombre = ctx.VAR().getText()
        valor = self.visit(ctx.expr())
        self.tabla[nombre] = valor
    def visitPrintStat(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)
    def visitWhileStat(self, ctx):
        while self.visit(ctx.expr()) != 0:
            for s in ctx.stat():
                self.visit(s)
    def visitForStat(self, ctx):
        var_nombre = ctx.VAR().getText()
        inicio = self.visit(ctx.expr(0))
        fin = self.visit(ctx.expr(1))
        self.tabla[var_nombre] = inicio
        while self.tabla[var_nombre] <= fin:
            for s in ctx.stat():
                self.visit(s)
            self.tabla[var_nombre] += 1
    def visitInt(self, ctx):
        return int(ctx.INT().getText())
    def visitVar(self, ctx):
        nombre = ctx.VAR().getText()
        if nombre not in self.tabla:
            raise NameError(f"Error: Variable '{nombre}' no definida.")
        return self.tabla[nombre]
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    def visitMulDiv(self, ctx):
        izq, der = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        return izq * der if ctx.op.text == '*' else int(izq / der)
    def visitAddSub(self, ctx):
        izq, der = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        return izq + der if ctx.op.text == '+' else izq - der
    def visitComp(self, ctx):
        izq, der = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '<':
            return 1 if izq < der else 0
        elif op == '>':
            return 1 if izq > der else 0
        elif op == '==':
            return 1 if izq == der else 0
        elif op == '!=':
            return 1 if izq != der else 0
        return 0