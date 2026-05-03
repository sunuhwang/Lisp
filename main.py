import sys
import lexer
import parser
import builtin
import LispObj
code = sys.argv[1]
code = open(code).read()
code = lexer.lex(code)
code = parser.parse(code)
for stmt in code:
    stmt.eval(builtin.env)