import ply.yacc as yacc

from json_parser.json_lexer import tokens

def p_json(p):
    'json : value'
    p[0] = p[1]

def p_value(p):
    'value : object'
    p[0] = p[1]

def p_object(p):
    'object : '


def p_characters(p):
    'characters : CHAR characters'
    p[0] = p[1] + p[2]


parser = yacc.yacc()

while True:
    try:
        s = input('json > ')
    except EOFError:
        break

    if not s: continue
    result = parser.parse(s)
    print(result)