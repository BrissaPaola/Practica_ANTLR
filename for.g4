grammar for;

prog: stat+ EOF ;

stat: assign                          # AssignStat
    | 'print' expr                    # PrintStat
    | 'while' expr '{' stat* '}'      # WhileStat
    | 'for' VAR '=' expr 'to' expr '{' stat* '}' # ForStat
    ;

assign: VAR '<-' expr ;

expr: expr op=('*'|'/') expr          # MulDiv
    | expr op=('+'|'-') expr          # AddSub
    | expr op=('<'|'>'|'=='|'!=') expr # Comp
    | INT                             # Int
    | VAR                             # Var
    | '(' expr ')'                    # Parens
    ;

INT : [0-9]+ ;
VAR : [a-zA-Z][a-zA-Z0-9]* ;
WS  : [ \t\r\n]+ -> skip ;