
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CA CALL CF DECLARACOES DIF DIV DO ELSE ESCREVER FOR FUNCAO ID IF IGUAL II INSTRUCOES LER MAIN MAIOR MAIORI MENOR MENORI MOD MUL NOME NOT NUM OR PA PF PV RETURN SOMA STRING SUB VARPrograma : Main FuncoesMain : MAIN CA Declaracoes Instrucoes CFFuncoes : Funcao FuncoesFuncoes : Funcao : FUNCAO NOME CA Declaracoes Instrucoes RETURN Exp PV CFDeclaracoes : DECLARACOES CA Decls CFDecls : Decl DeclsDecls : Decl : VAR ID PVDecl : VAR ID IGUAL Exp PVInstrucoes : INSTRUCOES CA Insts CFInsts : Inst InstsInsts : Inst : ID IGUAL Exp PVIFor : ID IGUAL ExpInst : LER ID PVInst : ESCREVER Frase PVInst : CALL Funcao PVInst : RETURN Exp PVInst : FOR PA Inst Logica PV IFor PF DO CA Insts CFInst : IF PA Logica PF CA Insts CFInst : IF PA Logica PF CA Insts CF ELSE CA Insts CFFrase : STRINGFrase : ExpLogica : Logica AND CondLogica : Logica OR CondLogica : NOT CondLogica : CondCond : Cond MAIOR ExpCond : Cond MENOR ExpCond : Cond MAIORI ExpCond : Cond MENORI ExpCond : Cond II ExpCond : Cond DIF ExpCond : ExpExp : Exp SOMA TermoExp : Exp SUB TermoExp : TermoTermo : Termo MUL FatorTermo : Termo DIV FatorTermo : Termo MOD FatorTermo : FatorFator : '(' Logica ')'Fator : NUMFator : ID"
    
_lr_action_items = {'MAIN':([0,],[3,]),'$end':([1,2,4,5,8,17,92,],[0,-4,-1,-4,-3,-2,-5,]),'FUNCAO':([2,5,17,28,92,],[6,6,-2,6,-5,]),'CA':([3,9,11,14,90,109,111,],[7,12,15,18,102,112,113,]),'NOME':([6,],[9,]),'DECLARACOES':([7,12,],[11,11,]),'INSTRUCOES':([10,16,32,],[14,14,-6,]),'CF':([13,15,18,19,20,23,24,33,36,37,52,56,57,67,68,72,73,91,102,105,108,112,113,114,115,116,117,],[17,-8,-13,32,-8,36,-13,-7,-11,-12,-9,-16,-17,-18,-19,92,-14,-10,-13,108,-21,-13,-13,116,117,-20,-22,]),'VAR':([15,20,52,91,],[21,21,-9,-10,]),'ID':([18,21,24,26,27,29,35,38,45,50,51,53,56,57,58,59,60,61,62,65,67,68,69,73,80,81,82,83,84,85,86,87,101,102,107,108,112,113,116,117,],[25,34,25,39,47,47,47,47,47,25,47,47,-16,-17,47,47,47,47,47,47,-18,-19,47,-14,47,47,47,47,47,47,47,47,104,25,47,-21,25,25,-20,-22,]),'LER':([18,24,50,56,57,67,68,73,102,108,112,113,116,117,],[26,26,26,-16,-17,-18,-19,-14,26,-21,26,26,-20,-22,]),'ESCREVER':([18,24,50,56,57,67,68,73,102,108,112,113,116,117,],[27,27,27,-16,-17,-18,-19,-14,27,-21,27,27,-20,-22,]),'CALL':([18,24,50,56,57,67,68,73,102,108,112,113,116,117,],[28,28,28,-16,-17,-18,-19,-14,28,-21,28,28,-20,-22,]),'RETURN':([18,22,24,36,50,56,57,67,68,73,102,108,112,113,116,117,],[29,35,29,-11,29,-16,-17,-18,-19,-14,29,-21,29,29,-20,-22,]),'FOR':([18,24,50,56,57,67,68,73,102,108,112,113,116,117,],[30,30,30,-16,-17,-18,-19,-14,30,-21,30,30,-20,-22,]),'IF':([18,24,50,56,57,67,68,73,102,108,112,113,116,117,],[31,31,31,-16,-17,-18,-19,-14,31,-21,31,31,-20,-22,]),'IGUAL':([25,34,104,],[38,53,107,]),'STRING':([27,],[41,]),'(':([27,29,35,38,45,51,53,56,57,58,59,60,61,62,65,67,68,69,73,80,81,82,83,84,85,86,87,107,108,116,117,],[45,45,45,45,45,45,45,-16,-17,45,45,45,45,45,45,-18,-19,45,-14,45,45,45,45,45,45,45,45,45,-21,-20,-22,]),'NUM':([27,29,35,38,45,51,53,56,57,58,59,60,61,62,65,67,68,69,73,80,81,82,83,84,85,86,87,107,108,116,117,],[46,46,46,46,46,46,46,-16,-17,46,46,46,46,46,46,-18,-19,46,-14,46,46,46,46,46,46,46,46,46,-21,-20,-22,]),'PA':([30,31,],[50,51,]),'PV':([34,39,40,41,42,43,44,46,47,48,49,54,55,64,66,71,74,75,76,77,78,79,88,89,92,93,94,95,96,97,98,99,100,],[52,56,57,-23,-24,-38,-42,-44,-45,67,68,72,73,-28,-35,91,-36,-37,-39,-40,-41,-43,-27,101,-5,-25,-26,-29,-30,-31,-32,-33,-34,]),'SOMA':([42,43,44,46,47,49,54,55,66,71,74,75,76,77,78,79,95,96,97,98,99,100,110,],[58,-38,-42,-44,-45,58,58,58,58,58,-36,-37,-39,-40,-41,-43,58,58,58,58,58,58,58,]),'SUB':([42,43,44,46,47,49,54,55,66,71,74,75,76,77,78,79,95,96,97,98,99,100,110,],[59,-38,-42,-44,-45,59,59,59,59,59,-36,-37,-39,-40,-41,-43,59,59,59,59,59,59,59,]),'MAIOR':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,82,-35,-36,-37,-39,-40,-41,-43,82,82,82,-29,-30,-31,-32,-33,-34,]),'MENOR':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,83,-35,-36,-37,-39,-40,-41,-43,83,83,83,-29,-30,-31,-32,-33,-34,]),'MAIORI':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,84,-35,-36,-37,-39,-40,-41,-43,84,84,84,-29,-30,-31,-32,-33,-34,]),'MENORI':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,85,-35,-36,-37,-39,-40,-41,-43,85,85,85,-29,-30,-31,-32,-33,-34,]),'II':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,86,-35,-36,-37,-39,-40,-41,-43,86,86,86,-29,-30,-31,-32,-33,-34,]),'DIF':([43,44,46,47,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,87,-35,-36,-37,-39,-40,-41,-43,87,87,87,-29,-30,-31,-32,-33,-34,]),')':([43,44,46,47,63,64,66,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,79,-28,-35,-36,-37,-39,-40,-41,-43,-27,-25,-26,-29,-30,-31,-32,-33,-34,]),'AND':([43,44,46,47,63,64,66,70,74,75,76,77,78,79,88,89,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,80,-28,-35,80,-36,-37,-39,-40,-41,-43,-27,80,-25,-26,-29,-30,-31,-32,-33,-34,]),'OR':([43,44,46,47,63,64,66,70,74,75,76,77,78,79,88,89,93,94,95,96,97,98,99,100,],[-38,-42,-44,-45,81,-28,-35,81,-36,-37,-39,-40,-41,-43,-27,81,-25,-26,-29,-30,-31,-32,-33,-34,]),'PF':([43,44,46,47,64,66,70,74,75,76,77,78,79,88,93,94,95,96,97,98,99,100,103,110,],[-38,-42,-44,-45,-28,-35,90,-36,-37,-39,-40,-41,-43,-27,-25,-26,-29,-30,-31,-32,-33,-34,106,-15,]),'MUL':([43,44,46,47,74,75,76,77,78,79,],[60,-42,-44,-45,60,60,-39,-40,-41,-43,]),'DIV':([43,44,46,47,74,75,76,77,78,79,],[61,-42,-44,-45,61,61,-39,-40,-41,-43,]),'MOD':([43,44,46,47,74,75,76,77,78,79,],[62,-42,-44,-45,62,62,-39,-40,-41,-43,]),'NOT':([45,51,56,57,67,68,69,73,108,116,117,],[65,65,-16,-17,-18,-19,65,-14,-21,-20,-22,]),'DO':([106,],[109,]),'ELSE':([108,],[111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Main':([0,],[2,]),'Funcoes':([2,5,],[4,8,]),'Funcao':([2,5,28,],[5,5,48,]),'Declaracoes':([7,12,],[10,16,]),'Instrucoes':([10,16,],[13,22,]),'Decls':([15,20,],[19,33,]),'Decl':([15,20,],[20,20,]),'Insts':([18,24,102,112,113,],[23,37,105,114,115,]),'Inst':([18,24,50,102,112,113,],[24,24,69,24,24,24,]),'Frase':([27,],[40,]),'Exp':([27,29,35,38,45,51,53,65,69,80,81,82,83,84,85,86,87,107,],[42,49,54,55,66,66,71,66,66,66,66,95,96,97,98,99,100,110,]),'Termo':([27,29,35,38,45,51,53,58,59,65,69,80,81,82,83,84,85,86,87,107,],[43,43,43,43,43,43,43,74,75,43,43,43,43,43,43,43,43,43,43,43,]),'Fator':([27,29,35,38,45,51,53,58,59,60,61,62,65,69,80,81,82,83,84,85,86,87,107,],[44,44,44,44,44,44,44,44,44,76,77,78,44,44,44,44,44,44,44,44,44,44,44,]),'Logica':([45,51,69,],[63,70,89,]),'Cond':([45,51,65,69,80,81,],[64,64,88,64,93,94,]),'IFor':([101,],[103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Main Funcoes','Programa',2,'p_Programa','yacc.py',70),
  ('Main -> MAIN CA Declaracoes Instrucoes CF','Main',5,'p_Main','yacc.py',78),
  ('Funcoes -> Funcao Funcoes','Funcoes',2,'p_Funcoes_Funcao','yacc.py',86),
  ('Funcoes -> <empty>','Funcoes',0,'p_Funcoes_vazio','yacc.py',90),
  ('Funcao -> FUNCAO NOME CA Declaracoes Instrucoes RETURN Exp PV CF','Funcao',9,'p_Funcao','yacc.py',98),
  ('Declaracoes -> DECLARACOES CA Decls CF','Declaracoes',4,'p_Declaracoes','yacc.py',106),
  ('Decls -> Decl Decls','Decls',2,'p_Decls_Decl','yacc.py',114),
  ('Decls -> <empty>','Decls',0,'p_Decls_Vazio','yacc.py',118),
  ('Decl -> VAR ID PV','Decl',3,'p_Decl_Var','yacc.py',126),
  ('Decl -> VAR ID IGUAL Exp PV','Decl',5,'p_Decl_Var_Igual','yacc.py',131),
  ('Instrucoes -> INSTRUCOES CA Insts CF','Instrucoes',4,'p_Instrucoes','yacc.py',140),
  ('Insts -> Inst Insts','Insts',2,'p_Insts_Inst','yacc.py',148),
  ('Insts -> <empty>','Insts',0,'p_Insts_Vazio','yacc.py',152),
  ('Inst -> ID IGUAL Exp PV','Inst',4,'p_Inst_IGUAL','yacc.py',160),
  ('IFor -> ID IGUAL Exp','IFor',3,'p_IFor_ISP','yacc.py',164),
  ('Inst -> LER ID PV','Inst',3,'p_Inst_LER','yacc.py',168),
  ('Inst -> ESCREVER Frase PV','Inst',3,'p_Inst_ESCREVER','yacc.py',172),
  ('Inst -> CALL Funcao PV','Inst',3,'p_Inst_CALL','yacc.py',180),
  ('Inst -> RETURN Exp PV','Inst',3,'p_Inst_RETURN','yacc.py',184),
  ('Inst -> FOR PA Inst Logica PV IFor PF DO CA Insts CF','Inst',11,'p_Inst_FOR','yacc.py',188),
  ('Inst -> IF PA Logica PF CA Insts CF','Inst',7,'p_Inst_IF','yacc.py',193),
  ('Inst -> IF PA Logica PF CA Insts CF ELSE CA Insts CF','Inst',11,'p_Inst_ELSE','yacc.py',198),
  ('Frase -> STRING','Frase',1,'p_Frase_ESCREVER_STRING','yacc.py',207),
  ('Frase -> Exp','Frase',1,'p_Frase_ESCREVER_NUM','yacc.py',211),
  ('Logica -> Logica AND Cond','Logica',3,'p_Logica_AND','yacc.py',220),
  ('Logica -> Logica OR Cond','Logica',3,'p_Logica_OR','yacc.py',224),
  ('Logica -> NOT Cond','Logica',2,'p_Logica_NOT','yacc.py',228),
  ('Logica -> Cond','Logica',1,'p_Logica_Cond','yacc.py',232),
  ('Cond -> Cond MAIOR Exp','Cond',3,'p_Cond_MAIOR','yacc.py',240),
  ('Cond -> Cond MENOR Exp','Cond',3,'p_Cond_MENOR','yacc.py',244),
  ('Cond -> Cond MAIORI Exp','Cond',3,'p_Cond_MAIORI','yacc.py',248),
  ('Cond -> Cond MENORI Exp','Cond',3,'p_Cond_MENORI','yacc.py',252),
  ('Cond -> Cond II Exp','Cond',3,'p_Cond_II','yacc.py',256),
  ('Cond -> Cond DIF Exp','Cond',3,'p_Cond_DIF','yacc.py',260),
  ('Cond -> Exp','Cond',1,'p_Cond_NUM','yacc.py',264),
  ('Exp -> Exp SOMA Termo','Exp',3,'p_Exp_SOMA','yacc.py',272),
  ('Exp -> Exp SUB Termo','Exp',3,'p_Exp_SUB','yacc.py',276),
  ('Exp -> Termo','Exp',1,'p_Exp','yacc.py',280),
  ('Termo -> Termo MUL Fator','Termo',3,'p_Termo_MUL','yacc.py',284),
  ('Termo -> Termo DIV Fator','Termo',3,'p_Termo_DIV','yacc.py',288),
  ('Termo -> Termo MOD Fator','Termo',3,'p_Termo_MOD','yacc.py',295),
  ('Termo -> Fator','Termo',1,'p_Termo_fator','yacc.py',302),
  ('Fator -> ( Logica )','Fator',3,'p_Fator_par','yacc.py',306),
  ('Fator -> NUM','Fator',1,'p_Fator_num','yacc.py',310),
  ('Fator -> ID','Fator',1,'p_Fator_id','yacc.py',314),
]
