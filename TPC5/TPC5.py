import re
import ply.lex as lex
import ply.yacc as yacc


tokens = ('LEVANTAR', 'POUSAR', 'MOEDAS', 'TELEFONE', 'ABORTAR')

t_ignore = ' \t'

t_LEVANTAR = r'LEVANTAR'
t_POUSAR = r'POUSAR'
t_ABORTAR = r'ABORTAR'

def t_MOEDAS(t):
    r'MOEDA ((\d{1,2}[ce], )*\d{1,2}[ce]).'
    res = re.search('MOEDA ((\d{1,2}[ce], )*\d{1,2}[ce]).',t).group(1)    
    l = re.split(', ',res)
    
    return t

def t_TELEFONE(t):
    r'T=(00\d+|\d{9})'
    result = re.search('T=(00\d+|\d{9})',t).group(1)
    t.value = int(result)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

lexer = lex.lex()

parser = yacc.yacc()