
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAleftPLUSMINUSAND BIGGER_THAN CLOSING_BRACES CLOSING_BRACKET CLOSING_PARENTH COMA COMMENT CONSTANT DIVISION DO DOUBLE ELSE EQUAL EQUAL_EQUAL FOR FUNCTION ID IF INT LOWER_THAN MAIN MINUS MINUSMINUS MULTIPLY NOT NOT_EQUAL OPEN_BRACES OPEN_BRACKET OPEN_PARENTH OR PLUS PLUSPLUS PRINT READ SEMICOLON STRING WHILE\n\tPROGRAMA : VAR FUNC M\n\t\n\tVAR : TIPO DECLARE SEMICOLON\n\t\t| TIPO MAT SEMICOLON\n\t\t| VAR TIPO DECLARE SEMICOLON\n\t\t| VAR TIPO MAT SEMICOLON\n\t\t|\n\t\n\tDECLARE : ID\n\t\t\t| DECLARE COMA ID\n\t\t\t| ASSIGN\n\t\t\t| DECLARE COMA ASSIGN\n\t\n\tASSIGN : ID EQUAL EA\n\t\t\t| MAT EQUAL EA\n\t\n\tFUNC :  FUNCTION AUX_FUNC SET_ID OPEN_PARENTH CLOSING_PARENTH DECLARE_FUNC OPEN_BRACES S CLOSING_BRACES RETURN IF_AUX3\n\t\t|  FUNC AUX_FUNC FUNCTION SET_ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES DECLARE_FUNC S CLOSING_BRACES  RETURN IF_AUX3\n\t\t|  empty\n\t\n\tSET_ID : ID\n\t\n\tDECLARE_FUNC : empty\n\t\n\tRETURN  : empty\n\t\n\tAUX_FUNC : empty\n\t\n\tM    : MAIN OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES\n\t\n\tTIPO : INT\n\t\t| DOUBLE\n\t\n\tS : STATEMENTS\n\t| S STATEMENTS\n\t|\n\t\n\tSTATEMENTS : VAR \n\t\t\t| IDSTAT\n\t\t\t| PRINTSTAT\n\t\t\t| READSTAT\n\t\t\t| IFSTAT\n\t\t\t| WHILESTAT\n\t\t\t| DOSTAT\n\t\t\t| FORSTAT\n\t\t\t| FUNCSTAT\n\t\t\t| INC_STAT\n\t\t\t| \n\t\n\tIDSTAT : ASSIGN SEMICOLON\n\t\t\n\t\n\tPRINTSTAT : PRINT OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON\n\t\t\t| PRINT OPEN_PARENTH STRING CLOSING_PARENTH SEMICOLON\n\t\n\tREADSTAT : READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON\n\t\n\tIFSTAT : IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S IF_AUX3\n\t\t| IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S ELSE IF_AUX2 IN_S IF_AUX3\n\t\n\tIF_AUX1 : empty\n\t\n\tIF_AUX2 : empty\n\t\n\tIF_AUX3 : empty\n\tempty :\n\tWHILESTAT : WHILE WHILE_AUX_1 OPEN_PARENTH EL CLOSING_PARENTH WHILE_AUX_2 IN_S\n\t\n\tWHILE_AUX_1 : empty\n\t\n\tWHILE_AUX_2 : empty\n\t\n\tDOSTAT : DO WHILE_AUX_1 IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON\n\t\n\tFORSTAT : FOR OPEN_PARENTH ASSIGN SEMICOLON WHILE_AUX_1 EL SEMICOLON WHILE_AUX_2 ASSIGN CLOSING_PARENTH  IN_S\n\t\n\tFUNCSTAT : ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON\n\t\n\tINC_STAT : ID PLUSPLUS SEMICOLON\n\t\t\t| ID MINUSMINUS SEMICOLON\n\t\n\tIN_S : OPEN_BRACES S CLOSING_BRACES\n\t\n\tEA : TA\n\t| EA PLUS TA\n\t| EA MINUS TA\n\t\n\tFA  : CONSTANT\n\t\t| ID\n\t\t| MAT\n\t\t| OPEN_PARENTH EA CLOSING_PARENTH\n\t\n\tTA : FA\n\t| TA MULTIPLY FA\n\t| TA DIVISION FA\n\t\n\tEL : TL\n\t| EL OR TL\n\t\n\tTL : FL\n\t| TL AND FL\n\t\n\tFL : NL OPERATORS NL\n\t| EA OPERATORS EA\n\t| NL\n\t| OPEN_PARENTH EL CLOSING_PARENTH\n\t\n\tNL : NOT EL\n\t\n\tOPERATORS : NOT_EQUAL\n\t\t\t| LOWER_THAN\n\t\t\t| BIGGER_THAN\n\t\t\t| EQUAL_EQUAL\n\t\n\tMAT : ID MAT_BRACKET\n\t\n\tMAT_BRACKET : OPEN_BRACKET EA CLOSING_BRACKET\n\t\t\t\t| MAT_BRACKET OPEN_BRACKET EA CLOSING_BRACKET\n\t'
    
_lr_action_items = {'OPEN_BRACKET':([12,25,40,46,55,65,79,109,],[23,43,23,23,-80,-81,23,23,]),'EQUAL_EQUAL':([25,34,35,37,38,40,55,60,61,62,63,64,65,117,119,120,121,133,141,154,155,158,159,160,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,138,-66,-68,138,138,-74,-73,-67,-70,-69,-71,]),'MAIN':([0,1,7,9,22,26,32,33,124,146,147,162,163,164,170,176,],[-6,-46,16,-15,-3,-2,-5,-4,-46,-46,-18,-46,-13,-45,-46,-14,]),'ELSE':([153,169,],[-55,174,]),'SEMICOLON':([10,11,12,13,19,20,25,34,35,37,38,39,40,42,45,46,55,60,61,62,63,64,65,68,96,97,108,114,117,119,120,126,127,141,144,154,155,158,159,160,167,173,],[22,-9,-7,26,32,33,-79,-61,-63,-59,-56,-12,-60,-11,-10,-8,-80,-62,-64,-65,-57,-58,-81,90,112,113,128,131,-72,-66,-68,149,150,-74,161,-73,-67,-70,-69,-71,172,178,]),'PLUS':([25,34,35,37,38,39,40,41,42,50,55,56,60,61,62,63,64,65,107,121,122,133,160,],[-79,-61,-63,-59,-56,53,-60,53,53,53,-80,53,-62,-64,-65,-57,-58,-81,53,53,53,53,53,]),'OPEN_BRACES':([48,57,66,67,78,88,92,95,135,148,156,157,165,166,174,179,180,183,],[58,-46,89,-17,-46,103,-48,111,-46,-46,-43,111,111,-49,-46,111,-44,111,]),'COMA':([11,12,13,20,25,34,35,37,38,39,40,42,45,46,55,60,61,62,63,64,65,],[-9,-7,27,27,-79,-61,-63,-59,-56,-12,-60,-11,-10,-8,-80,-62,-64,-65,-57,-58,-81,]),'DOUBLE':([0,1,22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[4,4,-3,-2,-5,-4,4,-17,-33,-27,-34,-35,-28,-32,-31,4,-29,-23,-30,4,4,-37,-24,-46,4,4,-54,-53,4,4,-52,4,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'PRINT':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,76,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,76,76,-37,-24,-46,76,76,-54,-53,76,76,-52,76,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'OPEN_PARENTH':([16,21,23,24,28,29,36,43,49,51,52,53,54,73,76,77,79,84,85,91,92,93,99,100,105,115,118,128,129,134,136,138,139,140,142,143,151,152,],[30,36,36,36,47,-16,36,36,59,36,36,36,36,-46,93,94,98,99,100,105,-48,36,115,36,115,115,115,-46,152,115,-76,-78,-77,-75,115,36,115,115,]),'NOT_EQUAL':([25,34,35,37,38,40,55,60,61,62,63,64,65,117,119,120,121,133,141,154,155,158,159,160,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,140,-66,-68,140,140,-74,-73,-67,-70,-69,-71,]),'FOR':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,77,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,77,77,-37,-24,-46,77,77,-54,-53,77,77,-52,77,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'AND':([25,34,35,37,38,40,55,60,61,62,63,64,65,117,119,120,141,154,155,158,159,160,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,-72,142,-68,-74,-73,142,-70,-69,-71,]),'INT':([0,1,22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[3,3,-3,-2,-5,-4,3,-17,-33,-27,-34,-35,-28,-32,-31,3,-29,-23,-30,3,3,-37,-24,-46,3,3,-54,-53,3,3,-52,3,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'MINUSMINUS':([79,],[96,]),'NOT':([92,99,105,115,118,128,134,136,137,138,139,140,142,151,152,],[-48,118,118,118,118,-46,118,-76,118,-78,-77,-75,118,118,118,]),'BIGGER_THAN':([25,34,35,37,38,40,55,60,61,62,63,64,65,117,119,120,121,133,141,154,155,158,159,160,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,139,-66,-68,139,139,-74,-73,-67,-70,-69,-71,]),'DO':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,78,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,78,78,-37,-24,-46,78,78,-54,-53,78,78,-52,78,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'FUNCTION':([0,1,7,9,15,17,22,26,32,33,124,146,147,162,163,164,170,176,],[-6,6,-46,-15,-19,31,-3,-2,-5,-4,-46,-46,-18,-46,-13,-45,-46,-14,]),'PLUSPLUS':([79,],[97,]),'ID':([3,4,5,6,8,14,15,21,22,23,24,26,27,31,32,33,36,43,51,52,53,54,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,92,93,94,99,100,102,103,104,105,111,112,113,115,118,123,128,130,131,134,136,138,139,140,142,143,145,149,150,151,152,153,161,164,166,169,171,172,175,177,178,182,184,185,],[-21,-22,12,-46,12,29,-19,40,-3,40,40,-2,46,29,-5,-4,40,40,40,40,40,40,79,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,79,79,-37,-48,40,109,40,40,-24,-46,79,40,79,-54,-53,40,40,79,-46,79,-52,40,-76,-78,-77,-75,40,40,79,-39,-38,40,40,-55,-40,-45,-49,-46,-47,-46,-41,109,-50,-46,-42,-51,]),'LOWER_THAN':([25,34,35,37,38,40,55,60,61,62,63,64,65,117,119,120,121,133,141,154,155,158,159,160,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,136,-66,-68,136,136,-74,-73,-67,-70,-69,-71,]),'OR':([25,34,35,37,38,40,55,60,61,62,63,64,65,116,117,119,120,125,132,141,154,155,158,159,160,167,168,],[-79,-61,-63,-59,-56,-60,-80,-62,-64,-65,-57,-58,-81,134,-72,-66,-68,134,134,134,-73,-67,-70,-69,-71,134,134,]),'STRING':([93,],[106,]),'EQUAL':([10,12,19,25,44,46,55,65,79,109,],[21,24,21,-79,21,24,-80,-81,24,24,]),'CLOSING_PARENTH':([25,30,34,35,37,38,39,40,42,47,50,55,59,60,61,62,63,64,65,98,106,107,116,117,119,120,122,125,132,133,141,154,155,158,159,160,168,181,],[-79,48,-61,-63,-59,-56,-12,-60,-11,57,60,-80,88,-62,-64,-65,-57,-58,-81,114,126,127,135,-72,-66,-68,144,148,154,60,-74,-73,-67,-70,-69,-71,173,183,]),'CLOSING_BRACES':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,-6,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,101,-6,-37,-24,-46,124,-6,-54,-53,-6,153,-52,162,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'DIVISION':([25,34,35,37,38,40,55,60,61,62,63,64,65,],[-79,-61,-63,-59,52,-60,-80,-62,-64,-65,52,52,-81,]),'CONSTANT':([21,23,24,36,43,51,52,53,54,92,93,99,100,105,115,118,128,134,136,138,139,140,142,143,151,152,],[37,37,37,37,37,37,37,37,37,-48,37,37,37,37,37,37,-46,37,-76,-78,-77,-75,37,37,37,37,]),'MINUS':([25,34,35,37,38,39,40,41,42,50,55,56,60,61,62,63,64,65,107,121,122,133,160,],[-79,-61,-63,-59,-56,54,-60,54,54,54,-80,54,-62,-64,-65,-57,-58,-81,54,54,54,54,54,]),'$end':([2,18,101,],[0,-1,-20,]),'IF':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,84,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,84,84,-37,-24,-46,84,84,-54,-53,84,84,-52,84,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'MULTIPLY':([25,34,35,37,38,40,55,60,61,62,63,64,65,],[-79,-61,-63,-59,51,-60,-80,-62,-64,-65,51,51,-81,]),'READ':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,85,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,85,85,-37,-24,-46,85,85,-54,-53,85,85,-52,85,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),'CLOSING_BRACKET':([25,34,35,37,38,40,41,55,56,60,61,62,63,64,65,],[-79,-61,-63,-59,-56,-60,55,-80,65,-62,-64,-65,-57,-58,-81,]),'WHILE':([22,26,32,33,58,67,69,70,71,72,74,75,80,81,82,83,86,87,89,90,102,103,104,110,111,112,113,123,130,131,145,149,150,153,161,164,169,171,175,178,182,184,185,],[-3,-2,-5,-4,73,-17,-33,-27,-34,-35,-28,-32,-31,-26,-29,-23,-30,73,73,-37,-24,-46,73,129,73,-54,-53,73,73,-52,73,-39,-38,-55,-40,-45,-46,-47,-41,-50,-46,-42,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'DOSTAT':([58,87,89,104,111,123,130,145,],[75,75,75,75,75,75,75,75,]),'IN_S':([95,157,165,179,183,],[110,169,171,182,185,]),'S':([58,89,111,123,],[87,104,130,145,]),'DECLARE_FUNC':([57,103,],[66,123,]),'FA':([21,23,24,36,43,51,52,53,54,93,99,100,105,115,118,134,142,143,151,152,],[35,35,35,35,35,61,62,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'FORSTAT':([58,87,89,104,111,123,130,145,],[69,69,69,69,69,69,69,69,]),'IF_AUX3':([146,169,170,182,],[163,175,176,184,]),'IF_AUX1':([135,],[157,]),'NL':([99,105,115,118,134,137,142,151,152,],[117,117,117,117,117,158,117,117,117,]),'EL':([99,105,115,118,151,152,],[116,125,132,141,167,168,]),'READSTAT':([58,87,89,104,111,123,130,145,],[82,82,82,82,82,82,82,82,]),'TA':([21,23,24,36,43,53,54,93,99,100,105,115,118,134,142,143,151,152,],[38,38,38,38,38,63,64,38,38,38,38,38,38,38,38,38,38,38,]),'FUNCSTAT':([58,87,89,104,111,123,130,145,],[71,71,71,71,71,71,71,71,]),'MAT_BRACKET':([12,40,46,79,109,],[25,25,25,25,25,]),'WHILE_AUX_2':([148,172,],[165,177,]),'STATEMENTS':([58,87,89,104,111,123,130,145,],[83,102,83,102,83,83,102,102,]),'SET_ID':([14,31,],[28,49,]),'OPERATORS':([117,121,133,],[137,143,143,]),'MAT':([5,8,21,23,24,27,36,43,51,52,53,54,58,87,89,93,94,99,100,104,105,111,115,118,123,130,134,142,143,145,151,152,177,],[10,19,34,34,34,44,34,34,34,34,34,34,44,44,44,34,44,34,34,44,34,44,34,34,44,44,34,34,34,44,34,34,44,]),'WHILESTAT':([58,87,89,104,111,123,130,145,],[80,80,80,80,80,80,80,80,]),'VAR':([0,58,87,89,104,111,123,130,145,],[1,81,81,81,81,81,81,81,81,]),'RETURN':([124,162,],[146,170,]),'PROGRAMA':([0,],[2,]),'TL':([99,105,115,118,134,151,152,],[119,119,119,119,155,119,119,]),'INC_STAT':([58,87,89,104,111,123,130,145,],[72,72,72,72,72,72,72,72,]),'FUNC':([1,],[7,]),'TIPO':([0,1,58,81,87,89,104,111,123,130,145,],[5,8,5,8,5,5,5,5,5,5,5,]),'ASSIGN':([5,8,27,58,87,89,94,104,111,123,130,145,177,],[11,11,45,68,68,68,108,68,68,68,68,68,181,]),'IF_AUX2':([174,],[179,]),'FL':([99,105,115,118,134,142,151,152,],[120,120,120,120,120,159,120,120,]),'AUX_FUNC':([6,7,],[14,17,]),'WHILE_AUX_1':([73,78,128,],[91,95,151,]),'M':([7,],[18,]),'EA':([21,23,24,36,43,93,99,100,105,115,118,134,142,143,151,152,],[39,41,42,50,56,107,121,122,121,133,121,121,121,160,121,121,]),'empty':([1,6,7,57,73,78,103,124,128,135,146,148,162,169,170,172,174,182,],[9,15,15,67,92,92,67,147,92,156,164,166,147,164,164,166,180,164,]),'PRINTSTAT':([58,87,89,104,111,123,130,145,],[74,74,74,74,74,74,74,74,]),'IFSTAT':([58,87,89,104,111,123,130,145,],[86,86,86,86,86,86,86,86,]),'DECLARE':([5,8,],[13,20,]),'IDSTAT':([58,87,89,104,111,123,130,145,],[70,70,70,70,70,70,70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> VAR FUNC M','PROGRAMA',3,'p_PROGRAMA','compile_run.py',326),
  ('VAR -> TIPO DECLARE SEMICOLON','VAR',3,'p_VAR','compile_run.py',339),
  ('VAR -> TIPO MAT SEMICOLON','VAR',3,'p_VAR','compile_run.py',340),
  ('VAR -> VAR TIPO DECLARE SEMICOLON','VAR',4,'p_VAR','compile_run.py',341),
  ('VAR -> VAR TIPO MAT SEMICOLON','VAR',4,'p_VAR','compile_run.py',342),
  ('VAR -> <empty>','VAR',0,'p_VAR','compile_run.py',343),
  ('DECLARE -> ID','DECLARE',1,'p_DECLARE','compile_run.py',396),
  ('DECLARE -> DECLARE COMA ID','DECLARE',3,'p_DECLARE','compile_run.py',397),
  ('DECLARE -> ASSIGN','DECLARE',1,'p_DECLARE','compile_run.py',398),
  ('DECLARE -> DECLARE COMA ASSIGN','DECLARE',3,'p_DECLARE','compile_run.py',399),
  ('ASSIGN -> ID EQUAL EA','ASSIGN',3,'p_ASSIGN','compile_run.py',416),
  ('ASSIGN -> MAT EQUAL EA','ASSIGN',3,'p_ASSIGN','compile_run.py',417),
  ('FUNC -> FUNCTION AUX_FUNC SET_ID OPEN_PARENTH CLOSING_PARENTH DECLARE_FUNC OPEN_BRACES S CLOSING_BRACES RETURN IF_AUX3','FUNC',11,'p_FUNC','compile_run.py',453),
  ('FUNC -> FUNC AUX_FUNC FUNCTION SET_ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES DECLARE_FUNC S CLOSING_BRACES RETURN IF_AUX3','FUNC',12,'p_FUNC','compile_run.py',454),
  ('FUNC -> empty','FUNC',1,'p_FUNC','compile_run.py',455),
  ('SET_ID -> ID','SET_ID',1,'p_SET_ID','compile_run.py',461),
  ('DECLARE_FUNC -> empty','DECLARE_FUNC',1,'p_DECLARE_FUNC','compile_run.py',469),
  ('RETURN -> empty','RETURN',1,'p_RETURN','compile_run.py',480),
  ('AUX_FUNC -> empty','AUX_FUNC',1,'p_AUX_FUNC','compile_run.py',492),
  ('M -> MAIN OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES','M',6,'p_M','compile_run.py',515),
  ('TIPO -> INT','TIPO',1,'p_TIPO','compile_run.py',519),
  ('TIPO -> DOUBLE','TIPO',1,'p_TIPO','compile_run.py',520),
  ('S -> STATEMENTS','S',1,'p_S','compile_run.py',532),
  ('S -> S STATEMENTS','S',2,'p_S','compile_run.py',533),
  ('S -> <empty>','S',0,'p_S','compile_run.py',534),
  ('STATEMENTS -> VAR','STATEMENTS',1,'p_STATEMENTS','compile_run.py',538),
  ('STATEMENTS -> IDSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',539),
  ('STATEMENTS -> PRINTSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',540),
  ('STATEMENTS -> READSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',541),
  ('STATEMENTS -> IFSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',542),
  ('STATEMENTS -> WHILESTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',543),
  ('STATEMENTS -> DOSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',544),
  ('STATEMENTS -> FORSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',545),
  ('STATEMENTS -> FUNCSTAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',546),
  ('STATEMENTS -> INC_STAT','STATEMENTS',1,'p_STATEMENTS','compile_run.py',547),
  ('STATEMENTS -> <empty>','STATEMENTS',0,'p_STATEMENTS','compile_run.py',548),
  ('IDSTAT -> ASSIGN SEMICOLON','IDSTAT',2,'p_IDSTAT','compile_run.py',553),
  ('PRINTSTAT -> PRINT OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON','PRINTSTAT',5,'p_PRINTSTAT','compile_run.py',559),
  ('PRINTSTAT -> PRINT OPEN_PARENTH STRING CLOSING_PARENTH SEMICOLON','PRINTSTAT',5,'p_PRINTSTAT','compile_run.py',560),
  ('READSTAT -> READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON','READSTAT',5,'p_READSTAT','compile_run.py',571),
  ('IFSTAT -> IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S IF_AUX3','IFSTAT',7,'p_IFSTAT','compile_run.py',581),
  ('IFSTAT -> IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S ELSE IF_AUX2 IN_S IF_AUX3','IFSTAT',10,'p_IFSTAT','compile_run.py',582),
  ('IF_AUX1 -> empty','IF_AUX1',1,'p_IF_AUX1','compile_run.py',588),
  ('IF_AUX2 -> empty','IF_AUX2',1,'p_IF_AUX2','compile_run.py',609),
  ('IF_AUX3 -> empty','IF_AUX3',1,'p_IF_AUX3','compile_run.py',623),
  ('empty -> <empty>','empty',0,'p_empty','compile_run.py',634),
  ('WHILESTAT -> WHILE WHILE_AUX_1 OPEN_PARENTH EL CLOSING_PARENTH WHILE_AUX_2 IN_S','WHILESTAT',7,'p_WHILESTAT','compile_run.py',639),
  ('WHILE_AUX_1 -> empty','WHILE_AUX_1',1,'p_WHILE_AUX_1','compile_run.py',657),
  ('WHILE_AUX_2 -> empty','WHILE_AUX_2',1,'p_WHILE_AUX_2','compile_run.py',667),
  ('DOSTAT -> DO WHILE_AUX_1 IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON','DOSTAT',8,'p_DOSTAT','compile_run.py',685),
  ('FORSTAT -> FOR OPEN_PARENTH ASSIGN SEMICOLON WHILE_AUX_1 EL SEMICOLON WHILE_AUX_2 ASSIGN CLOSING_PARENTH IN_S','FORSTAT',11,'p_FORSTAT','compile_run.py',705),
  ('FUNCSTAT -> ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON','FUNCSTAT',4,'p_FUNCSTAT','compile_run.py',722),
  ('INC_STAT -> ID PLUSPLUS SEMICOLON','INC_STAT',3,'p_INC_STAT','compile_run.py',743),
  ('INC_STAT -> ID MINUSMINUS SEMICOLON','INC_STAT',3,'p_INC_STAT','compile_run.py',744),
  ('IN_S -> OPEN_BRACES S CLOSING_BRACES','IN_S',3,'p_IN_S','compile_run.py',749),
  ('EA -> TA','EA',1,'p_EA','compile_run.py',756),
  ('EA -> EA PLUS TA','EA',3,'p_EA','compile_run.py',757),
  ('EA -> EA MINUS TA','EA',3,'p_EA','compile_run.py',758),
  ('FA -> CONSTANT','FA',1,'p_FA','compile_run.py',797),
  ('FA -> ID','FA',1,'p_FA','compile_run.py',798),
  ('FA -> MAT','FA',1,'p_FA','compile_run.py',799),
  ('FA -> OPEN_PARENTH EA CLOSING_PARENTH','FA',3,'p_FA','compile_run.py',800),
  ('TA -> FA','TA',1,'p_TA','compile_run.py',837),
  ('TA -> TA MULTIPLY FA','TA',3,'p_TA','compile_run.py',838),
  ('TA -> TA DIVISION FA','TA',3,'p_TA','compile_run.py',839),
  ('EL -> TL','EL',1,'p_EL','compile_run.py',875),
  ('EL -> EL OR TL','EL',3,'p_EL','compile_run.py',876),
  ('TL -> FL','TL',1,'p_TL','compile_run.py',905),
  ('TL -> TL AND FL','TL',3,'p_TL','compile_run.py',906),
  ('FL -> NL OPERATORS NL','FL',3,'p_FL','compile_run.py',931),
  ('FL -> EA OPERATORS EA','FL',3,'p_FL','compile_run.py',932),
  ('FL -> NL','FL',1,'p_FL','compile_run.py',933),
  ('FL -> OPEN_PARENTH EL CLOSING_PARENTH','FL',3,'p_FL','compile_run.py',934),
  ('NL -> NOT EL','NL',2,'p_NL','compile_run.py',985),
  ('OPERATORS -> NOT_EQUAL','OPERATORS',1,'p_OPERATORS','compile_run.py',1008),
  ('OPERATORS -> LOWER_THAN','OPERATORS',1,'p_OPERATORS','compile_run.py',1009),
  ('OPERATORS -> BIGGER_THAN','OPERATORS',1,'p_OPERATORS','compile_run.py',1010),
  ('OPERATORS -> EQUAL_EQUAL','OPERATORS',1,'p_OPERATORS','compile_run.py',1011),
  ('MAT -> ID MAT_BRACKET','MAT',2,'p_MAT','compile_run.py',1017),
  ('MAT_BRACKET -> OPEN_BRACKET EA CLOSING_BRACKET','MAT_BRACKET',3,'p_MAT_BRACKET','compile_run.py',1032),
  ('MAT_BRACKET -> MAT_BRACKET OPEN_BRACKET EA CLOSING_BRACKET','MAT_BRACKET',4,'p_MAT_BRACKET','compile_run.py',1033),
]
