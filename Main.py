from antlr4 import InputStream, CommonTokenStream
from forLexer import forLexer
from forParser import forParser
from EvalVisitor import EvalVisitor

def ejecutar(codigo):
    lexer = forLexer(InputStream(codigo))
    tokens = CommonTokenStream(lexer)
    parser = forParser(tokens)
    tree = parser.prog()
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    print("Prueba Numeros del 1 al 10")
    codigo_for = """
    for i = 1 to 10 {
        print i
    }
    """
    ejecutar(codigo_for)