
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CA CALL CF DECLARACOES DIF DIV DO ELSE ESCREVER FOR FUNCAO ID IF IGUAL II INSTRUCOES LER MAIN MAIOR MAIORI MENOR MENORI MOD MUL NOT NUM OR PA PF PV SOMA STRING SUB VARPrograma : Main FuncoesMain : MAIN CA Declaracoes Instrucoes CFFuncoes : Funcao FuncoesFuncoes : Funcao : FUNCAO ID CA Insts CFDeclaracoes : DECLARACOES CA Decls CFDecls : Decl DeclsDecls : Decl : VAR ID PVDecl : VAR ID IGUAL Exp PVInstrucoes : INSTRUCOES CA Insts CFInsts : Inst InstsInsts : Inst : ID IGUAL Exp PVIFor : ID IGUAL ExpInst : LER ID PVInst : ESCREVER Frase PVInst : CALL ID PVInst : FOR PA Inst Logica PV IFor PF DO CA Insts CFInst : IF PA Logica PF CA Insts CFInst : IF PA Logica PF CA Insts CF ELSE CA Insts CFFrase : STRINGFrase : ExpLogica : Logica AND CondLogica : Logica OR CondLogica : NOT CondLogica : CondCond : Cond MAIOR ExpCond : Cond MENOR ExpCond : Cond MAIORI ExpCond : Cond MENORI ExpCond : Cond II ExpCond : Cond DIF ExpCond : ExpExp : Exp SOMA TermoExp : Exp SUB TermoExp : TermoTermo : Termo MUL FatorTermo : Termo DIV FatorTermo : Termo MOD FatorTermo : FatorFator : '(' Logica ')'Fator : NUMFator : ID"
    
_lr_action_items = {'MAIN':([0,],[3,]),'$end':([1,2,4,5,8,24,30,],[0,-4,-1,-4,-3,-2,-5,]),'FUNCAO':([2,5,24,30,],[6,6,-2,-5,]),'CA':([3,9,11,14,83,102,104,],[7,12,15,25,94,105,106,]),'ID':([6,12,18,19,20,21,25,28,29,38,42,43,49,50,51,52,53,54,55,58,60,61,65,66,73,74,75,76,77,78,79,80,93,94,100,101,105,106,109,110,],[9,16,16,32,40,41,16,47,40,40,16,40,-16,-17,40,40,40,40,40,40,-18,40,40,-14,40,40,40,40,40,40,40,40,97,16,40,-20,16,16,-19,-21,]),'DECLARACOES':([7,],[11,]),'INSTRUCOES':([10,45,],[14,-6,]),'CF':([12,13,15,17,18,25,26,27,31,44,46,49,50,60,63,64,66,94,95,98,101,105,106,107,108,109,110,],[-13,24,-8,30,-13,-13,45,-8,-12,63,-7,-16,-17,-18,-11,-9,-14,-13,-10,101,-20,-13,-13,109,110,-19,-21,]),'LER':([12,18,25,42,49,50,60,66,94,101,105,106,109,110,],[19,19,19,19,-16,-17,-18,-14,19,-20,19,19,-19,-21,]),'ESCREVER':([12,18,25,42,49,50,60,66,94,101,105,106,109,110,],[20,20,20,20,-16,-17,-18,-14,20,-20,20,20,-19,-21,]),'CALL':([12,18,25,42,49,50,60,66,94,101,105,106,109,110,],[21,21,21,21,-16,-17,-18,-14,21,-20,21,21,-19,-21,]),'FOR':([12,18,25,42,49,50,60,66,94,101,105,106,109,110,],[22,22,22,22,-16,-17,-18,-14,22,-20,22,22,-19,-21,]),'IF':([12,18,25,42,49,50,60,66,94,101,105,106,109,110,],[23,23,23,23,-16,-17,-18,-14,23,-20,23,23,-19,-21,]),'VAR':([15,27,64,95,],[28,28,-9,-10,]),'IGUAL':([16,47,97,],[29,65,100,]),'STRING':([20,],[34,]),'(':([20,29,38,43,49,50,51,52,53,54,55,58,60,61,65,66,73,74,75,76,77,78,79,80,100,101,109,110,],[38,38,38,38,-16,-17,38,38,38,38,38,38,-18,38,38,-14,38,38,38,38,38,38,38,38,38,-20,-19,-21,]),'NUM':([20,29,38,43,49,50,51,52,53,54,55,58,60,61,65,66,73,74,75,76,77,78,79,80,100,101,109,110,],[39,39,39,39,-16,-17,39,39,39,39,39,39,-18,39,39,-14,39,39,39,39,39,39,39,39,39,-20,-19,-21,]),'PA':([22,23,],[42,43,]),'PV':([32,33,34,35,36,37,39,40,41,47,48,57,59,67,68,69,70,71,72,81,82,84,85,86,87,88,89,90,91,92,],[49,50,-22,-23,-37,-41,-43,-44,60,64,66,-27,-34,-35,-36,-38,-39,-40,-42,-26,93,95,-24,-25,-28,-29,-30,-31,-32,-33,]),'SOMA':([35,36,37,39,40,48,59,67,68,69,70,71,72,84,87,88,89,90,91,92,103,],[51,-37,-41,-43,-44,51,51,-35,-36,-38,-39,-40,-42,51,51,51,51,51,51,51,51,]),'SUB':([35,36,37,39,40,48,59,67,68,69,70,71,72,84,87,88,89,90,91,92,103,],[52,-37,-41,-43,-44,52,52,-35,-36,-38,-39,-40,-42,52,52,52,52,52,52,52,52,]),'MAIOR':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,75,-34,-35,-36,-38,-39,-40,-42,75,75,75,-28,-29,-30,-31,-32,-33,]),'MENOR':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,76,-34,-35,-36,-38,-39,-40,-42,76,76,76,-28,-29,-30,-31,-32,-33,]),'MAIORI':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,77,-34,-35,-36,-38,-39,-40,-42,77,77,77,-28,-29,-30,-31,-32,-33,]),'MENORI':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,78,-34,-35,-36,-38,-39,-40,-42,78,78,78,-28,-29,-30,-31,-32,-33,]),'II':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,79,-34,-35,-36,-38,-39,-40,-42,79,79,79,-28,-29,-30,-31,-32,-33,]),'DIF':([36,37,39,40,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,80,-34,-35,-36,-38,-39,-40,-42,80,80,80,-28,-29,-30,-31,-32,-33,]),')':([36,37,39,40,56,57,59,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,72,-27,-34,-35,-36,-38,-39,-40,-42,-26,-24,-25,-28,-29,-30,-31,-32,-33,]),'AND':([36,37,39,40,56,57,59,62,67,68,69,70,71,72,81,82,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,73,-27,-34,73,-35,-36,-38,-39,-40,-42,-26,73,-24,-25,-28,-29,-30,-31,-32,-33,]),'OR':([36,37,39,40,56,57,59,62,67,68,69,70,71,72,81,82,85,86,87,88,89,90,91,92,],[-37,-41,-43,-44,74,-27,-34,74,-35,-36,-38,-39,-40,-42,-26,74,-24,-25,-28,-29,-30,-31,-32,-33,]),'PF':([36,37,39,40,57,59,62,67,68,69,70,71,72,81,85,86,87,88,89,90,91,92,96,103,],[-37,-41,-43,-44,-27,-34,83,-35,-36,-38,-39,-40,-42,-26,-24,-25,-28,-29,-30,-31,-32,-33,99,-15,]),'MUL':([36,37,39,40,67,68,69,70,71,72,],[53,-41,-43,-44,53,53,-38,-39,-40,-42,]),'DIV':([36,37,39,40,67,68,69,70,71,72,],[54,-41,-43,-44,54,54,-38,-39,-40,-42,]),'MOD':([36,37,39,40,67,68,69,70,71,72,],[55,-41,-43,-44,55,55,-38,-39,-40,-42,]),'NOT':([38,43,49,50,60,61,66,101,109,110,],[58,58,-16,-17,-18,58,-14,-20,-19,-21,]),'DO':([99,],[102,]),'ELSE':([101,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Main':([0,],[2,]),'Funcoes':([2,5,],[4,8,]),'Funcao':([2,5,],[5,5,]),'Declaracoes':([7,],[10,]),'Instrucoes':([10,],[13,]),'Insts':([12,18,25,94,105,106,],[17,31,44,98,107,108,]),'Inst':([12,18,25,42,94,105,106,],[18,18,18,61,18,18,18,]),'Decls':([15,27,],[26,46,]),'Decl':([15,27,],[27,27,]),'Frase':([20,],[33,]),'Exp':([20,29,38,43,58,61,65,73,74,75,76,77,78,79,80,100,],[35,48,59,59,59,59,84,59,59,87,88,89,90,91,92,103,]),'Termo':([20,29,38,43,51,52,58,61,65,73,74,75,76,77,78,79,80,100,],[36,36,36,36,67,68,36,36,36,36,36,36,36,36,36,36,36,36,]),'Fator':([20,29,38,43,51,52,53,54,55,58,61,65,73,74,75,76,77,78,79,80,100,],[37,37,37,37,37,37,69,70,71,37,37,37,37,37,37,37,37,37,37,37,37,]),'Logica':([38,43,61,],[56,62,82,]),'Cond':([38,43,58,61,73,74,],[57,57,81,57,85,86,]),'IFor':([93,],[96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Main Funcoes','Programa',2,'p_Programa','yacc.py',70),
  ('Main -> MAIN CA Declaracoes Instrucoes CF','Main',5,'p_Main','yacc.py',85),
  ('Funcoes -> Funcao Funcoes','Funcoes',2,'p_Funcoes_Funcao','yacc.py',93),
  ('Funcoes -> <empty>','Funcoes',0,'p_Funcoes_vazio','yacc.py',97),
  ('Funcao -> FUNCAO ID CA Insts CF','Funcao',5,'p_Funcao','yacc.py',105),
  ('Declaracoes -> DECLARACOES CA Decls CF','Declaracoes',4,'p_Declaracoes','yacc.py',114),
  ('Decls -> Decl Decls','Decls',2,'p_Decls_Decl','yacc.py',122),
  ('Decls -> <empty>','Decls',0,'p_Decls_Vazio','yacc.py',126),
  ('Decl -> VAR ID PV','Decl',3,'p_Decl_Var','yacc.py',134),
  ('Decl -> VAR ID IGUAL Exp PV','Decl',5,'p_Decl_Var_Igual','yacc.py',139),
  ('Instrucoes -> INSTRUCOES CA Insts CF','Instrucoes',4,'p_Instrucoes','yacc.py',148),
  ('Insts -> Inst Insts','Insts',2,'p_Insts_Inst','yacc.py',156),
  ('Insts -> <empty>','Insts',0,'p_Insts_Vazio','yacc.py',160),
  ('Inst -> ID IGUAL Exp PV','Inst',4,'p_Inst_IGUAL','yacc.py',168),
  ('IFor -> ID IGUAL Exp','IFor',3,'p_IFor_ISP','yacc.py',172),
  ('Inst -> LER ID PV','Inst',3,'p_Inst_LER','yacc.py',176),
  ('Inst -> ESCREVER Frase PV','Inst',3,'p_Inst_ESCREVER','yacc.py',180),
  ('Inst -> CALL ID PV','Inst',3,'p_Inst_CALL','yacc.py',184),
  ('Inst -> FOR PA Inst Logica PV IFor PF DO CA Insts CF','Inst',11,'p_Inst_FOR','yacc.py',191),
  ('Inst -> IF PA Logica PF CA Insts CF','Inst',7,'p_Inst_IF','yacc.py',196),
  ('Inst -> IF PA Logica PF CA Insts CF ELSE CA Insts CF','Inst',11,'p_Inst_ELSE','yacc.py',201),
  ('Frase -> STRING','Frase',1,'p_Frase_ESCREVER_STRING','yacc.py',210),
  ('Frase -> Exp','Frase',1,'p_Frase_ESCREVER_NUM','yacc.py',214),
  ('Logica -> Logica AND Cond','Logica',3,'p_Logica_AND','yacc.py',223),
  ('Logica -> Logica OR Cond','Logica',3,'p_Logica_OR','yacc.py',227),
  ('Logica -> NOT Cond','Logica',2,'p_Logica_NOT','yacc.py',231),
  ('Logica -> Cond','Logica',1,'p_Logica_Cond','yacc.py',235),
  ('Cond -> Cond MAIOR Exp','Cond',3,'p_Cond_MAIOR','yacc.py',243),
  ('Cond -> Cond MENOR Exp','Cond',3,'p_Cond_MENOR','yacc.py',247),
  ('Cond -> Cond MAIORI Exp','Cond',3,'p_Cond_MAIORI','yacc.py',251),
  ('Cond -> Cond MENORI Exp','Cond',3,'p_Cond_MENORI','yacc.py',255),
  ('Cond -> Cond II Exp','Cond',3,'p_Cond_II','yacc.py',259),
  ('Cond -> Cond DIF Exp','Cond',3,'p_Cond_DIF','yacc.py',263),
  ('Cond -> Exp','Cond',1,'p_Cond_NUM','yacc.py',267),
  ('Exp -> Exp SOMA Termo','Exp',3,'p_Exp_SOMA','yacc.py',275),
  ('Exp -> Exp SUB Termo','Exp',3,'p_Exp_SUB','yacc.py',279),
  ('Exp -> Termo','Exp',1,'p_Exp','yacc.py',283),
  ('Termo -> Termo MUL Fator','Termo',3,'p_Termo_MUL','yacc.py',287),
  ('Termo -> Termo DIV Fator','Termo',3,'p_Termo_DIV','yacc.py',291),
  ('Termo -> Termo MOD Fator','Termo',3,'p_Termo_MOD','yacc.py',298),
  ('Termo -> Fator','Termo',1,'p_Termo_fator','yacc.py',305),
  ('Fator -> ( Logica )','Fator',3,'p_Fator_par','yacc.py',309),
  ('Fator -> NUM','Fator',1,'p_Fator_num','yacc.py',313),
  ('Fator -> ID','Fator',1,'p_Fator_id','yacc.py',317),
]
