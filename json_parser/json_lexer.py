import ply.lex as lex

literals = ["{", "}", "\"", ":", ]

tokens = [
    "CHAR"
    "WS"
]

def t_NEWLINE():


def t_CHAR(t):
    r'[^"\\]'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = '''
{
    "a":"b"
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

