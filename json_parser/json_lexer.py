import ply.lex as lex

literals = ["{", "}", "\"", ":", ]

tokens = [
    "DIGITS",
    "CHAR",
    "NEWLINE",
    "QUOTE",
    "LBRACKET",
    "RBRACKET"
]

def t_DIGITS(t): 
    r'\d+'
    t.value = int(t.value)
    return t

def t_LBRACKET(t):
    r'{'
    return t

def t_RBRACKET(t):
    r'}'
    return t

def t_CHAR(t):
    r'[^"\\\s]'
    return t

def t_NEWLINE(t):
    r'\n+|(\r\n)+'
    t.lexer.lineno = len(t.value)

def t_QUOTE(t):
    r'"'
    return t



t_ignore = ' \t\f\v\r'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = '''
{
    "a":"bxx",
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    print(tok.lexer.lineno)

