# -----------------------------------------------------------------------------
#                           Copyright: Javier Monterroso
#                           Jvmonteros98@gmail.com
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#                                   Imports
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
# -----------------------------------------------------------------------------
#                                 Configuration
# -----------------------------------------------------------------------------

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# -----------------------------------------------------------------------------
#                                     Tokens
# -----------------------------------------------------------------------------

tokens = (
    'int',
    'float',
    'string',
    'id',
    'bool',
    'power',
    'times',
    'division',
    'plus',
    'minus',
    'mod',
    'less_equal',
    'greater_equal',
    'less',
    'greater',
    'double_equal',
    'not_equal',
    'or',
    'and',
    'not',
    'equal',
    'l_par',
    'r_par' ,
    'l_cbra',
    'r_cbra',
    'l_bra',
    'r_bra'
)

def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_float(t):
    r'd+("."d+)?'
    t.value = float(t.value)
    return t
t_string = r'([\"][^"]*[\"])'
t_id = r'([a-zA-Z_])[a-zA-Z0-9_ñÑ]*'
t_bool = r'true|false'
t_power = r'\^'
t_times = r'\*'
t_division = r'/'
t_plus = r'\+'
t_minus = r'-'
t_mod = r'%'
t_less_equal = r'<='
t_greater_equal = r'>='
t_less = r'<'
t_greater = r'>'
t_double_equal = r'=='
t_not_equal = r'!='
t_or = r'\|\|'
t_and = r'&&'
t_not = r'!'
t_equal = r'='
t_l_par = r'\('
t_r_par = r'\)'
t_l_cbra = r'\{'
t_r_cbra = r'\}'
t_l_bra = r'\['
t_r_bra = r'\]'

# -----------------------------------------------------------------------------
#                                   Parser
# -----------------------------------------------------------------------------

import ply.lex as lex
lex.lex()

# -----------------------------------------------------------------------------
#                                   Configuration
# -----------------------------------------------------------------------------

precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'times', 'division')
)

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

names = {}

# -----------------------------------------------------------------------------
#                                   Productions
# -----------------------------------------------------------------------------
def p_init(t):
    'init  :  instruction_list'
    t[0]=t[1]

def p_instruction_list(t):
    'instruction_list : int plus int'
    t[0]=t[1]

# -----------------------------------------------------------------------------
#                                   Parsing
# -----------------------------------------------------------------------------
import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
