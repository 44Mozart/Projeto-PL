import ply.yacc as yacc
from lex import tokens
import sys

# Programa : Main Funcoes 
#
# Main : MAIN CA Declaracoes Instrucoes CF 
#
# Funcoes : Funcao Funcoes
#         | vazio
#
# Funcao : FUNCAO NOME CA Declaracoes Instrucoes RETURN Exp PV CF
#
# Declaracoes : DECLARACOES CA Decls CF
#
# Decls : Decl Decls
#       | vazio
#
# Decl : VAR ID PV
#      | VAR ID IGUAL Exp PV
# 
# Instrucoes : INSTRUCOES CA Insts CF
#
# Insts : Inst Insts
#       | vazio
#
# Inst : ID IGUAL Exp PV
#      | ID IGUAL Exp 
#      | LER ID PV
#      | ESCREVER Frase PV
#      | CALL Funcao PV
#      | RETURN Exp PV
#      | FOR PA Inst Logica PV IFor PF DO CA Insts CF
#      | IF PA Logica PF CA Insts CF
#      | IF PA Logica PF CA Insts CF ELSE CA Insts CF
#
# Frase : STRING
#       | Exp
#
# Logica : Logica AND Cond
#        | Logica OR Cond
#        | NOT Cond
#        | Cond
#
# Cond : Cond MAIOR Exp
#      | Cond MENOR Exp
#      | Cond MAIORI Exp
#      | Cond MENORI Exp
#      | Cond II Exp
#      | Cond DIF Exp
#      | Exp
#   
# Exp : Exp SOMA Termo
#     | Exp SUB Termo
#     | Termo
#
# Termo : Termo MUL Fator
#       | Termo DIV Fator
#       | Termo MOD Fator
#       | Fator
#
# Factor : PA Exp PF
#        | NUM

# --------------------------------------------------------------------------------
# |                                 Programa                                     |
# --------------------------------------------------------------------------------

def p_Programa(p):
    "Programa : Main Funcoes"
    p.parser.fileOut.write(f'{p[1]}\n{p[2]}') 

# --------------------------------------------------------------------------------
# |                                 Main                                         |
# --------------------------------------------------------------------------------

def p_Main(p):
    "Main : MAIN CA Declaracoes Instrucoes CF"
    p[0] = p[3] + 'start\n' + p[4] + 'stop'

# --------------------------------------------------------------------------------
# |                                 Funcoes                                      |
# --------------------------------------------------------------------------------

def p_Funcoes_Funcao(p):
    "Funcoes : Funcao Funcoes"
    p[0] = p[1] + p[2]

def p_Funcoes_vazio(p):
    "Funcoes : "
    p[0] = ""

# --------------------------------------------------------------------------------
# |                                 Funcao                                       |
# --------------------------------------------------------------------------------

def p_Funcao(p):
    "Funcao : FUNCAO NOME CA Declaracoes Instrucoes RETURN Exp PV CF"
    p[0] = f"{set_functions(p,p[2])}{p[4]}{p[5]}return {p[7]}"

# --------------------------------------------------------------------------------
# |                                 Declaracoes                                  |
# --------------------------------------------------------------------------------

def p_Declaracoes(p):
    "Declaracoes : DECLARACOES CA Decls CF"
    p[0] = p[3]

# --------------------------------------------------------------------------------
# |                                 Decls                                        |
# --------------------------------------------------------------------------------

def p_Decls_Decl(p):
    "Decls : Decl Decls"
    p[0] = p[1] + p[2]

def p_Decls_Vazio(p):
    "Decls : "
    p[0] = ""

# --------------------------------------------------------------------------------
# |                                 Decl                                         |
# --------------------------------------------------------------------------------

def p_Decl_Var(p):
    "Decl : VAR ID PV"
    set_registers(p, p[2])
    p[0] = "pushi 0\n" 

def p_Decl_Var_Igual(p):
    "Decl : VAR ID IGUAL Exp PV"
    set_registers(p, p[2])
    p[0] = p[4]

# --------------------------------------------------------------------------------
# |                                 Instrucoes                                   |
# --------------------------------------------------------------------------------

def p_Instrucoes(p):
    "Instrucoes : INSTRUCOES CA Insts CF"
    p[0] = p[3]

# --------------------------------------------------------------------------------
# |                                 Insts                                        |
# --------------------------------------------------------------------------------

def p_Insts_Inst(p):
    "Insts : Inst Insts"
    p[0] = p[1] + p[2]

def p_Insts_Vazio(p) : 
    "Insts : "
    p[0] = ""

# --------------------------------------------------------------------------------
# |                                 Inst                                         |
# --------------------------------------------------------------------------------

def p_Inst_IGUAL(p):
    "Inst : ID IGUAL Exp PV"
    p[0] = f"{p[3]}storeg {p.parser.registers[p[1]]}\n"

def p_IFor_ISP(p):
    "IFor : ID IGUAL Exp"
    p[0] = f"{p[3]}storeg {p.parser.registers[p[1]]}\n"
    
def p_Inst_LER(p):
    "Inst : LER ID PV"
    p[0] = f"read\natoi\nstoreg {p.parser.registers[p[2]]}\n" 

def p_Inst_ESCREVER(p):
    "Inst : ESCREVER Frase PV"
    p[0] = p[2]

#
#
#
#
def p_Inst_CALL(p):
    "Inst : CALL Funcao PV"
    p[0] = f"call {get_functions(p,p[2])}"

def p_Inst_RETURN(p):
    "Inst : RETURN Exp PV"
    p[0] = f"return {p[2]}"

def p_Inst_FOR(p):
    "Inst : FOR PA Inst Logica PV IFor PF DO CA Insts CF"
    p.parser.for_counter += 1
    p[0] = f"{p[3]}for{p.parser.for_counter}:\n{p[4]}jz fimfor{p.parser.for_counter}\n{p[10]}{p[6]}jump for{p.parser.for_counter}\nfimfor{p.parser.for_counter}:\n"

def p_Inst_IF(p):
    "Inst : IF PA Logica PF CA Insts CF"
    p.parser.if_counter += 1
    p[0] = f"{p[3]}jz fimif{p.parser.if_counter}\n{p[6]}fimif{p.parser.if_counter}:\n"

def p_Inst_ELSE(p):
    "Inst : IF PA Logica PF CA Insts CF ELSE CA Insts CF"
    p.parser.if_counter += 1
    p[0] = f"{p[3]}jz else{p.parser.if_counter}\n{p[6]}jump fimif{p.parser.if_counter}\nelse{p.parser.if_counter}:\n{p[10]}fimif{p.parser.if_counter}:\n"

# --------------------------------------------------------------------------------
# |                                 Frase                                        |
# --------------------------------------------------------------------------------

def p_Frase_ESCREVER_STRING(p):
    "Frase : STRING"
    p[0] = f"pushs {p[1]}\nwrites\npushs \"\\n\"\nwrites\n"

def p_Frase_ESCREVER_NUM(p):
    "Frase : Exp"
    p[0] = f"{p[1]}writei\npushs \"\\n\"\nwrites\n"


# --------------------------------------------------------------------------------
# |                                 Logica                                       |
# --------------------------------------------------------------------------------

def p_Logica_AND(p):
    "Logica : Logica AND Cond"
    p[0] = f"{p[1]}{p[3]}mul\n" 

def p_Logica_OR(p):
    "Logica : Logica OR Cond"
    p[0] = f"{p[1]}{p[3]}add\n{p[1]}{p[3]}mul\nsub\n"

def p_Logica_NOT(p):
    "Logica : NOT Cond"
    p[0] = f"{p[2]}not\n"

def p_Logica_Cond(p):
    "Logica : Cond"
    p[0] = p[1]

# --------------------------------------------------------------------------------
# |                                 Cond                                         |
# --------------------------------------------------------------------------------

def p_Cond_MAIOR(p):
    "Cond : Cond MAIOR Exp"
    p[0] = f"{p[1]}{p[3]}sup\n" 

def p_Cond_MENOR(p):
    "Cond : Cond MENOR Exp"
    p[0] = f"{p[1]}{p[3]}inf\n" 

def p_Cond_MAIORI(p):
    "Cond : Cond MAIORI Exp"
    p[0] = f"{p[1]}{p[3]}supeq\n" 

def p_Cond_MENORI(p):
    "Cond : Cond MENORI Exp"
    p[0] = f"{p[1]}{p[3]}infeq\n" 

def p_Cond_II(p):
    "Cond : Cond II Exp"
    p[0] = f"{p[1]}{p[3]}equal\n" 

def p_Cond_DIF(p):
    "Cond : Cond DIF Exp"
    p[0] = f"{p[1]}{p[3]}equal\nnot\n"

def p_Cond_NUM(p):
    "Cond : Exp"
    p[0] = p[1]

# --------------------------------------------------------------------------------
# |                                 Exp                                          |
# --------------------------------------------------------------------------------

def p_Exp_SOMA(p):
    "Exp : Exp SOMA Termo"
    p[0] = f"{p[1]}{p[3]}add\n"
    
def p_Exp_SUB(p):
    "Exp : Exp SUB Termo"
    p[0] = f"{p[1]}{p[3]}sub\n"

def p_Exp(p):
    "Exp : Termo"
    p[0] = p[1] 

def p_Termo_MUL(p):
    "Termo : Termo MUL Fator"
    p[0] = f"{p[1]}{p[3]}mul\n"

def p_Termo_DIV(p):
    "Termo : Termo DIV Fator"
    if p[3] != 0:
        p[0] = f"{p[1]}{p[3]}div\n"
    else:
        p[0] = p[1]

def p_Termo_MOD(p):
    "Termo : Termo MOD Fator"
    if p[3] != 0:
        p[0] = f"{p[1]}{p[3]}mod\n"
    else:
        p[0] = p[1]

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Fator_par(p):
    "Fator : '(' Logica ')'"
    p[0] = p[2]

def p_Fator_num(p):
    "Fator : NUM"
    p[0] = f"pushi {p[1]}\n"

def p_Fator_id(p):
    "Fator : ID"
    p[0] = f"pushg {str(get_registers(p,p[1]))}\n"

def p_error(p):
    print("Erro sintático: ", p)
    parser.success = False

# --------------------------------------------------------------------------------
# |                                 Auxiliares                                   |
# --------------------------------------------------------------------------------

def set_registers(p, id):
    if id not in p.parser.registers:
        parser.registers[id] = p.parser.offset
        p.parser.offset += 1

def get_registers(p, id):
    if id in p.parser.registers:
        return p.parser.registers[id]
    else:
        return None

def set_functions(p, id):
    if id not in p.parser.functions:
        parser.functions[id] = p.parser.offset_functions
        p.parser.offset_functions += 1

def get_functions(p, id):
    if id in p.parser.functions:
        return p.parser.functions[id]
    else:
        return None

parser = yacc.yacc()

parser.registers = dict() # (id : offset)
parser.offset = 0
parser.functions = dict()
parser.offset_functions = 0
parser.if_counter = 0
parser.for_counter = 0
parser.fileOut = open('teste_vm.vm','w+')

# Read input and parse it by line
textoFonte = ""

file = open(input("Introduce path to file to be compiled: "),'r')

for linha in file:
    textoFonte += linha

parser.parse(textoFonte)

