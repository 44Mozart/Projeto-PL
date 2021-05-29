import ply.lex as lex

reserved = {'var' : 'VAR',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'do' : 'DO',
    'declaracoes' : 'DECLARACOES',
    'instrucoes' : 'INSTRUCOES',
    'ler' : 'LER',
    'escrever' : 'ESCREVER',
    'funcao' : 'FUNCAO',
    'main' : 'MAIN',
}


tokens = ['SOMA','SUB','MUL','DIV','MOD','II','MAIOR','MENOR','MENORI','MAIORI',
          'AND','OR','NOT','IGUAL','DIF','PV','CA','CF','PA','PF','ID','NUM','NOME','RETURN','CALL','STRING'] + list(reserved.values())

def t_AND(t):
    r'&&'
    t.type = reserved.get(t.value,'AND')
    return t

def t_OR(t):
    r'\|\|'
    t.type = reserved.get(t.value,'OR')
    return t

def t_DIF(t):
    r'\!\='
    t.type = reserved.get(t.value,'DIF')
    return t

def t_NOT(t):
    r'!'
    t.type = reserved.get(t.value,'NOT')
    return t

def t_II(t):
    r'=='
    t.type = reserved.get(t.value,'II')
    return t

def t_MAIORI(t):
    r'\>='
    t.type = reserved.get(t.value,'MAIORI')
    return t

def t_MENORI(t):
    r'\<='
    t.type = reserved.get(t.value,'MENORI')
    return t

def t_MAIOR(t):
    r'\>'
    t.type = reserved.get(t.value,'MAIOR')
    return t

def t_MENOR(t):
    r'\<'
    t.type = reserved.get(t.value,'MENOR')
    return t

def t_IGUAL(t):
    r'\='
    t.type = reserved.get(t.value,'IGUAL')
    return t

def t_SOMA(t):
    r'\+'
    t.type = reserved.get(t.value,'SOMA')
    return t

def t_SUB(t):
    r'\-'
    t.type = reserved.get(t.value,'SUB')
    return t

def t_MUL(t):
    r'\*'
    t.type = reserved.get(t.value,'MUL')
    return t

def t_DIV(t):
    r'\/'
    t.type = reserved.get(t.value,'DIV')
    return t

def t_MOD(t):
    r'%'
    t.type = reserved.get(t.value,'MOD')
    return t

def t_PV(t):
    r';'
    t.type = reserved.get(t.value,'PV')
    return t

def t_CA(t):
    r'\{'
    t.type = reserved.get(t.value,'CA')
    return t

def t_CF(t):
    r'\}'
    t.type = reserved.get(t.value,'CF')
    return t

def t_PA(t):
    r'\('
    t.type = reserved.get(t.value,'PA')
    return t

def t_PF(t):
    r'\)'
    t.type = reserved.get(t.value,'PF')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_RETURN(t):
    r'return'
    t.type = reserved.get(t.value,'RETURN')
    return t

def t_CALL(t):
    r'call'
    t.type = reserved.get(t.value,'CALL')
    return t

def t_NUM(t):
    r'\d+'
    t.type = reserved.get(t.value,'NUM')
    return t

def t_NOME(t):
    r'[a-zA-Z_][a-zA-Z0-9]*\(\)'
    t.type = reserved.get(t.value,'NOME')
    return t

def t_STRING(t):
    r'\"[^"]+\"'
    t.type = reserved.get(t.value,'STRING')
    return t


t_ignore = " \t\n"


def t_error(t):
    print('Carater ilegal: ', t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()