
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAleftPLUSMINUSAND BIGGER_THAN CLOSING_BRACES CLOSING_BRACKET CLOSING_PARENTH COMA COMMENT CONSTANT DIVISION DO DOUBLE ELSE EQUAL EQUAL_EQUAL FOR FUNCTION ID IF INT LOWER_THAN MAIN MINUS MINUSMINUS MULTIPLY NOT NOT_EQUAL OPEN_BRACES OPEN_BRACKET OPEN_PARENTH OR PLUS PLUSPLUS PRINT READ SEMICOLON STRING WHILE\n\tPROGRAMA : VAR FUNC M\n\t\n\tVAR : TIPO DECLARE SEMICOLON\n\t\t| TIPO MAT SEMICOLON\n\t\t| VAR TIPO DECLARE SEMICOLON\n\t\t| VAR TIPO MAT SEMICOLON\n\t\t|\n\t\n\tDECLARE : ID\n\t\t\t| DECLARE COMA ID\n\t\t\t| ASSIGN\n\t\t\t| DECLARE COMA ASSIGN\n\t\n\tASSIGN : ID EQUAL EA\n\t\n\tFUNC : FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES\n\t\t| FUNC FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES\n\t\t|\n\t\n\tM    : MAIN OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES\n\t\n\tTIPO : INT\n\t\t| DOUBLE\n\t\n\tS : STATEMENTS\n\t| S STATEMENTS\n\t|\n\t\n\tSTATEMENTS : VAR \n\t\t\t| IDSTAT\n\t\t\t| PRINTSTAT\n\t\t\t| READSTAT\n\t\t\t| IFSTAT\n\t\t\t| WHILESTAT\n\t\t\t| DOSTAT\n\t\t\t| FORSTAT\n\t\t\t| FUNCSTAT\n\t\t\t| INC_STAT\n\t\t\t| \n\t\n\tIDSTAT : ASSIGN SEMICOLON\n\t\t\n\t\n\tPRINTSTAT : PRINT OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON\n\t\t\t| PRINT OPEN_PARENTH STRING CLOSING_PARENTH SEMICOLON\n\t\n\tREADSTAT : READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON\n\t\n\tIFSTAT : IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S IF_AUX3\n\t\t| IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S ELSE IF_AUX2 IN_S IF_AUX3\n\t\n\tIF_AUX1 : empty\n\t\n\tIF_AUX2 : empty\n\t\n\tIF_AUX3 : empty\n\tempty :\n\tWHILESTAT : WHILE WHILE_AUX_1 OPEN_PARENTH EL CLOSING_PARENTH WHILE_AUX_2 IN_S\n\t\n\tWHILE_AUX_1 : empty\n\t\n\tWHILE_AUX_2 : empty\n\t\n\tDOSTAT : DO WHILE_AUX_1 IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON\n\t\n\tFORSTAT : FOR OPEN_PARENTH ASSIGN SEMICOLON WHILE_AUX_1 EL SEMICOLON WHILE_AUX_2 ASSIGN CLOSING_PARENTH  IN_S\n\t\n\tFUNCSTAT : ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON\n\t\n\tINC_STAT : ID PLUSPLUS SEMICOLON\n\t\t\t| ID MINUSMINUS SEMICOLON\n\t\n\tIN_S : OPEN_BRACES S CLOSING_BRACES\n\t\n\tEA : TA\n\t| EA PLUS TA\n\t| EA MINUS TA\n\t\n\tFA  : CONSTANT\n\t\t| ID\n\t\t| MAT\n\t\t| OPEN_PARENTH EA CLOSING_PARENTH\n\t\n\tTA : FA\n\t| TA MULTIPLY FA\n\t| TA DIVISION FA\n\t\n\tEL : TL\n\t| EL OR TL\n\t\n\tTL : FL\n\t| TL AND FL\n\t\n\tFL : NL OPERATORS NL\n\t| EA OPERATORS EA\n\t| NL\n\t| OPEN_PARENTH EL CLOSING_PARENTH\n\t\n\tNL : NOT EL\n\t\n\tOPERATORS : NOT_EQUAL\n\t\t\t| LOWER_THAN\n\t\t\t| BIGGER_THAN\n\t\t\t| EQUAL_EQUAL\n\t\n\tMAT : ID MAT_BRACKET\n\t\n\tMAT_BRACKET : OPEN_BRACKET CONSTANT CLOSING_BRACKET\n\t\t\t\t| MAT_BRACKET OPEN_BRACKET CONSTANT CLOSING_BRACKET\n\t\t\t\t| OPEN_BRACKET ID CLOSING_BRACKET\n\t\t\t\t| MAT_BRACKET OPEN_BRACKET ID CLOSING_BRACKET\n\t'
    
_lr_action_items = {'ID':([3,4,5,6,7,18,19,20,22,23,24,25,26,37,39,47,48,49,50,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,91,92,93,94,96,98,100,101,103,109,110,113,118,120,124,126,128,131,133,134,135,137,138,140,141,142,143,145,146,155,158,159,160,162,163,165,166,170,172,173,],[9,-16,-17,9,15,29,30,32,-3,-2,40,-5,-4,32,52,32,32,32,32,64,64,64,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,64,64,-19,32,32,107,-43,-32,32,64,-49,-48,32,64,32,32,-47,-41,64,32,32,-70,-73,-72,-71,32,-34,-33,-35,32,-50,32,-44,-41,-41,-42,-36,-40,107,-45,-41,-37,-46,]),'OR':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,114,115,116,125,129,139,147,148,149,152,153,154,157,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,-61,131,-63,-67,131,131,131,-64,-68,-62,-65,-66,131,131,]),'STRING':([91,],[104,]),'CLOSING_BRACES':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,-6,-6,89,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,99,-6,-19,-32,119,-49,-48,-6,-47,145,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'COMA':([9,10,12,14,21,32,33,34,35,36,38,40,41,45,46,57,58,59,60,61,62,63,],[-7,-9,24,24,-74,-55,-56,-51,-11,-58,-54,-8,-10,-77,-75,-59,-60,-53,-52,-57,-78,-76,]),'WHILE':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,111,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,76,76,76,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,76,76,-19,-32,76,-49,-48,76,127,-47,76,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'PLUS':([21,32,33,34,35,36,38,45,46,51,57,58,59,60,61,62,63,105,106,117,130,153,],[-74,-55,-56,-51,50,-58,-54,-77,-75,50,-59,-60,-53,-52,-57,-78,-76,50,50,50,50,50,]),'ELSE':([145,158,],[-50,164,]),'NOT_EQUAL':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,115,116,117,130,139,147,148,149,152,153,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,-61,-63,133,133,133,-69,-64,-68,-62,-65,-66,]),'EQUAL':([9,40,64,107,],[20,20,20,20,]),'MULTIPLY':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,],[-74,-55,-56,47,-58,-54,-77,-75,-59,-60,47,47,-57,-78,-76,]),'EQUAL_EQUAL':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,115,116,117,130,139,147,148,149,152,153,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,-61,-63,134,134,134,-69,-64,-68,-62,-65,-66,]),'MINUSMINUS':([64,],[86,]),'OPEN_PARENTH':([15,16,20,29,37,47,48,49,50,64,69,72,75,76,83,91,92,94,95,98,109,113,118,124,127,128,131,133,134,135,137,138,143,146,],[27,28,37,44,37,37,37,37,37,87,91,92,93,-41,98,37,37,-43,109,113,113,113,113,-41,146,113,113,-70,-73,-72,-71,37,113,113,]),'PLUSPLUS':([64,],[88,]),'MAIN':([0,2,8,22,23,25,26,89,119,],[-6,-14,16,-3,-2,-5,-4,-12,-13,]),'CONSTANT':([19,20,37,39,47,48,49,50,91,92,94,98,109,113,118,124,128,131,133,134,135,137,138,143,146,],[31,38,38,53,38,38,38,38,38,38,-43,38,38,38,38,-41,38,38,-70,-73,-72,-71,38,38,38,]),'DO':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,82,82,82,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,82,82,-19,-32,82,-49,-48,82,-47,82,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'SEMICOLON':([9,10,11,12,13,14,21,32,33,34,35,36,38,40,41,45,46,57,58,59,60,61,62,63,80,86,88,102,108,112,115,116,121,122,123,139,147,148,149,152,153,154,161,],[-7,-9,22,23,25,26,-74,-55,-56,-51,-11,-58,-54,-8,-10,-77,-75,-59,-60,-53,-52,-57,-78,-76,96,101,103,120,124,-61,-63,-67,140,141,142,-69,-64,-68,-62,-65,-66,159,166,]),'PRINT':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,69,69,69,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,69,69,-19,-32,69,-49,-48,69,-47,69,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'AND':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,115,116,139,147,148,149,152,153,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,128,-63,-67,-69,-64,-68,128,-65,-66,]),'INT':([0,2,22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[4,4,-3,-2,-5,-4,4,4,4,-22,-18,-25,4,-29,-30,-23,-24,-26,-28,-27,4,4,-19,-32,4,-49,-48,4,-47,4,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'$end':([1,17,99,],[0,-1,-15,]),'OPEN_BRACKET':([9,21,32,45,46,62,63,],[19,39,19,-77,-75,-78,-76,]),'LOWER_THAN':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,115,116,117,130,139,147,148,149,152,153,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,-61,-63,137,137,137,-69,-64,-68,-62,-65,-66,]),'CLOSING_PARENTH':([21,27,28,32,33,34,35,36,38,44,45,46,51,57,58,59,60,61,62,63,87,104,105,106,112,114,115,116,125,129,130,139,147,148,149,152,153,157,169,],[-74,42,43,-55,-56,-51,-11,-58,-54,56,-77,-75,61,-59,-60,-53,-52,-57,-78,-76,102,121,122,123,-61,132,-63,-67,144,148,61,-69,-64,-68,-62,-65,-66,161,171,]),'FUNCTION':([0,2,8,22,23,25,26,89,119,],[-6,7,18,-3,-2,-5,-4,-12,-13,]),'READ':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,72,72,72,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,72,72,-19,-32,72,-49,-48,72,-47,72,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'FOR':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,75,75,75,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,75,75,-19,-32,75,-49,-48,75,-47,75,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'CLOSING_BRACKET':([30,31,52,53,],[45,46,62,63,]),'DIVISION':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,],[-74,-55,-56,48,-58,-54,-77,-75,-59,-60,48,48,-57,-78,-76,]),'BIGGER_THAN':([21,32,33,34,36,38,45,46,57,58,59,60,61,62,63,112,115,116,117,130,139,147,148,149,152,153,],[-74,-55,-56,-51,-58,-54,-77,-75,-59,-60,-53,-52,-57,-78,-76,-61,-63,135,135,135,-69,-64,-68,-62,-65,-66,]),'MINUS':([21,32,33,34,35,36,38,45,46,51,57,58,59,60,61,62,63,105,106,117,130,153,],[-74,-55,-56,-51,49,-58,-54,-77,-75,49,-59,-60,-53,-52,-57,-78,-76,49,49,49,49,49,]),'OPEN_BRACES':([42,43,56,82,94,97,132,144,150,151,155,156,164,167,168,171,],[54,55,85,-41,-43,110,-41,-41,110,-38,-44,110,-41,110,-39,110,]),'DOUBLE':([0,2,22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[5,5,-3,-2,-5,-4,5,5,5,-22,-18,-25,5,-29,-30,-23,-24,-26,-28,-27,5,5,-19,-32,5,-49,-48,5,-47,5,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),'NOT':([94,98,109,113,118,124,128,131,133,134,135,136,137,143,146,],[-43,118,118,118,118,-41,118,118,-70,-73,-72,118,-71,118,118,]),'IF':([22,23,25,26,54,55,65,66,67,68,70,71,73,74,77,78,79,81,84,85,90,96,100,101,103,110,120,126,140,141,142,145,158,160,162,163,166,170,172,173,],[-3,-2,-5,-4,83,83,83,-22,-18,-25,-21,-29,-30,-23,-24,-26,-28,-27,83,83,-19,-32,83,-49,-48,83,-47,83,-34,-33,-35,-50,-41,-42,-36,-40,-45,-41,-37,-46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EL':([98,109,113,118,143,146,],[114,125,129,139,154,157,]),'empty':([76,82,124,132,144,158,159,164,170,],[94,94,94,151,155,163,155,168,163,]),'IF_AUX1':([132,],[150,]),'WHILE_AUX_2':([144,159,],[156,165,]),'S':([54,55,85,110,],[65,84,100,126,]),'IDSTAT':([54,55,65,84,85,100,110,126,],[66,66,66,66,66,66,66,66,]),'STATEMENTS':([54,55,65,84,85,100,110,126,],[67,67,90,90,67,90,67,90,]),'WHILESTAT':([54,55,65,84,85,100,110,126,],[78,78,78,78,78,78,78,78,]),'TA':([20,37,49,50,91,92,98,109,113,118,128,131,138,143,146,],[34,34,59,60,34,34,34,34,34,34,34,34,34,34,34,]),'IF_AUX3':([158,170,],[162,172,]),'PROGRAMA':([0,],[1,]),'TL':([98,109,113,118,131,143,146,],[112,112,112,112,149,112,112,]),'FORSTAT':([54,55,65,84,85,100,110,126,],[79,79,79,79,79,79,79,79,]),'ASSIGN':([3,6,24,54,55,65,84,85,93,100,110,126,165,],[10,10,41,80,80,80,80,80,108,80,80,80,169,]),'IFSTAT':([54,55,65,84,85,100,110,126,],[68,68,68,68,68,68,68,68,]),'DOSTAT':([54,55,65,84,85,100,110,126,],[81,81,81,81,81,81,81,81,]),'OPERATORS':([116,117,130,],[136,138,138,]),'DECLARE':([3,6,],[12,14,]),'FUNC':([2,],[8,]),'M':([8,],[17,]),'READSTAT':([54,55,65,84,85,100,110,126,],[77,77,77,77,77,77,77,77,]),'VAR':([0,54,55,65,84,85,100,110,126,],[2,70,70,70,70,70,70,70,70,]),'FUNCSTAT':([54,55,65,84,85,100,110,126,],[71,71,71,71,71,71,71,71,]),'TIPO':([0,2,54,55,65,70,84,85,100,110,126,],[3,6,3,3,3,6,3,3,3,3,3,]),'INC_STAT':([54,55,65,84,85,100,110,126,],[73,73,73,73,73,73,73,73,]),'MAT':([3,6,20,37,47,48,49,50,91,92,98,109,113,118,128,131,138,143,146,],[11,13,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'PRINTSTAT':([54,55,65,84,85,100,110,126,],[74,74,74,74,74,74,74,74,]),'FL':([98,109,113,118,128,131,143,146,],[115,115,115,115,147,115,115,115,]),'WHILE_AUX_1':([76,82,124,],[95,97,143,]),'EA':([20,37,91,92,98,109,113,118,128,131,138,143,146,],[35,51,105,106,117,117,130,117,117,117,153,117,117,]),'FA':([20,37,47,48,49,50,91,92,98,109,113,118,128,131,138,143,146,],[36,36,57,58,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'IN_S':([97,150,156,167,171,],[111,158,160,170,173,]),'NL':([98,109,113,118,128,131,136,143,146,],[116,116,116,116,116,116,152,116,116,]),'IF_AUX2':([164,],[167,]),'MAT_BRACKET':([9,32,],[21,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> VAR FUNC M','PROGRAMA',3,'p_PROGRAMA','main.py',282),
  ('VAR -> TIPO DECLARE SEMICOLON','VAR',3,'p_VAR','main.py',288),
  ('VAR -> TIPO MAT SEMICOLON','VAR',3,'p_VAR','main.py',289),
  ('VAR -> VAR TIPO DECLARE SEMICOLON','VAR',4,'p_VAR','main.py',290),
  ('VAR -> VAR TIPO MAT SEMICOLON','VAR',4,'p_VAR','main.py',291),
  ('VAR -> <empty>','VAR',0,'p_VAR','main.py',292),
  ('DECLARE -> ID','DECLARE',1,'p_DECLARE','main.py',308),
  ('DECLARE -> DECLARE COMA ID','DECLARE',3,'p_DECLARE','main.py',309),
  ('DECLARE -> ASSIGN','DECLARE',1,'p_DECLARE','main.py',310),
  ('DECLARE -> DECLARE COMA ASSIGN','DECLARE',3,'p_DECLARE','main.py',311),
  ('ASSIGN -> ID EQUAL EA','ASSIGN',3,'p_ASSIGN','main.py',328),
  ('FUNC -> FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES','FUNC',7,'p_FUNC','main.py',346),
  ('FUNC -> FUNC FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES','FUNC',8,'p_FUNC','main.py',347),
  ('FUNC -> <empty>','FUNC',0,'p_FUNC','main.py',348),
  ('M -> MAIN OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES','M',6,'p_M','main.py',353),
  ('TIPO -> INT','TIPO',1,'p_TIPO','main.py',357),
  ('TIPO -> DOUBLE','TIPO',1,'p_TIPO','main.py',358),
  ('S -> STATEMENTS','S',1,'p_S','main.py',370),
  ('S -> S STATEMENTS','S',2,'p_S','main.py',371),
  ('S -> <empty>','S',0,'p_S','main.py',372),
  ('STATEMENTS -> VAR','STATEMENTS',1,'p_STATEMENTS','main.py',376),
  ('STATEMENTS -> IDSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',377),
  ('STATEMENTS -> PRINTSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',378),
  ('STATEMENTS -> READSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',379),
  ('STATEMENTS -> IFSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',380),
  ('STATEMENTS -> WHILESTAT','STATEMENTS',1,'p_STATEMENTS','main.py',381),
  ('STATEMENTS -> DOSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',382),
  ('STATEMENTS -> FORSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',383),
  ('STATEMENTS -> FUNCSTAT','STATEMENTS',1,'p_STATEMENTS','main.py',384),
  ('STATEMENTS -> INC_STAT','STATEMENTS',1,'p_STATEMENTS','main.py',385),
  ('STATEMENTS -> <empty>','STATEMENTS',0,'p_STATEMENTS','main.py',386),
  ('IDSTAT -> ASSIGN SEMICOLON','IDSTAT',2,'p_IDSTAT','main.py',391),
  ('PRINTSTAT -> PRINT OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON','PRINTSTAT',5,'p_PRINTSTAT','main.py',397),
  ('PRINTSTAT -> PRINT OPEN_PARENTH STRING CLOSING_PARENTH SEMICOLON','PRINTSTAT',5,'p_PRINTSTAT','main.py',398),
  ('READSTAT -> READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON','READSTAT',5,'p_READSTAT','main.py',403),
  ('IFSTAT -> IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S IF_AUX3','IFSTAT',7,'p_IFSTAT','main.py',408),
  ('IFSTAT -> IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S ELSE IF_AUX2 IN_S IF_AUX3','IFSTAT',10,'p_IFSTAT','main.py',409),
  ('IF_AUX1 -> empty','IF_AUX1',1,'p_IF_AUX1','main.py',415),
  ('IF_AUX2 -> empty','IF_AUX2',1,'p_IF_AUX2','main.py',436),
  ('IF_AUX3 -> empty','IF_AUX3',1,'p_IF_AUX3','main.py',450),
  ('empty -> <empty>','empty',0,'p_empty','main.py',461),
  ('WHILESTAT -> WHILE WHILE_AUX_1 OPEN_PARENTH EL CLOSING_PARENTH WHILE_AUX_2 IN_S','WHILESTAT',7,'p_WHILESTAT','main.py',466),
  ('WHILE_AUX_1 -> empty','WHILE_AUX_1',1,'p_WHILE_AUX_1','main.py',484),
  ('WHILE_AUX_2 -> empty','WHILE_AUX_2',1,'p_WHILE_AUX_2','main.py',494),
  ('DOSTAT -> DO WHILE_AUX_1 IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON','DOSTAT',8,'p_DOSTAT','main.py',512),
  ('FORSTAT -> FOR OPEN_PARENTH ASSIGN SEMICOLON WHILE_AUX_1 EL SEMICOLON WHILE_AUX_2 ASSIGN CLOSING_PARENTH IN_S','FORSTAT',11,'p_FORSTAT','main.py',532),
  ('FUNCSTAT -> ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON','FUNCSTAT',4,'p_FUNCSTAT','main.py',549),
  ('INC_STAT -> ID PLUSPLUS SEMICOLON','INC_STAT',3,'p_INC_STAT','main.py',554),
  ('INC_STAT -> ID MINUSMINUS SEMICOLON','INC_STAT',3,'p_INC_STAT','main.py',555),
  ('IN_S -> OPEN_BRACES S CLOSING_BRACES','IN_S',3,'p_IN_S','main.py',560),
  ('EA -> TA','EA',1,'p_EA','main.py',567),
  ('EA -> EA PLUS TA','EA',3,'p_EA','main.py',568),
  ('EA -> EA MINUS TA','EA',3,'p_EA','main.py',569),
  ('FA -> CONSTANT','FA',1,'p_FA','main.py',605),
  ('FA -> ID','FA',1,'p_FA','main.py',606),
  ('FA -> MAT','FA',1,'p_FA','main.py',607),
  ('FA -> OPEN_PARENTH EA CLOSING_PARENTH','FA',3,'p_FA','main.py',608),
  ('TA -> FA','TA',1,'p_TA','main.py',628),
  ('TA -> TA MULTIPLY FA','TA',3,'p_TA','main.py',629),
  ('TA -> TA DIVISION FA','TA',3,'p_TA','main.py',630),
  ('EL -> TL','EL',1,'p_EL','main.py',666),
  ('EL -> EL OR TL','EL',3,'p_EL','main.py',667),
  ('TL -> FL','TL',1,'p_TL','main.py',696),
  ('TL -> TL AND FL','TL',3,'p_TL','main.py',697),
  ('FL -> NL OPERATORS NL','FL',3,'p_FL','main.py',722),
  ('FL -> EA OPERATORS EA','FL',3,'p_FL','main.py',723),
  ('FL -> NL','FL',1,'p_FL','main.py',724),
  ('FL -> OPEN_PARENTH EL CLOSING_PARENTH','FL',3,'p_FL','main.py',725),
  ('NL -> NOT EL','NL',2,'p_NL','main.py',776),
  ('OPERATORS -> NOT_EQUAL','OPERATORS',1,'p_OPERATORS','main.py',799),
  ('OPERATORS -> LOWER_THAN','OPERATORS',1,'p_OPERATORS','main.py',800),
  ('OPERATORS -> BIGGER_THAN','OPERATORS',1,'p_OPERATORS','main.py',801),
  ('OPERATORS -> EQUAL_EQUAL','OPERATORS',1,'p_OPERATORS','main.py',802),
  ('MAT -> ID MAT_BRACKET','MAT',2,'p_MAT','main.py',808),
  ('MAT_BRACKET -> OPEN_BRACKET CONSTANT CLOSING_BRACKET','MAT_BRACKET',3,'p_MAT_BRACKET','main.py',815),
  ('MAT_BRACKET -> MAT_BRACKET OPEN_BRACKET CONSTANT CLOSING_BRACKET','MAT_BRACKET',4,'p_MAT_BRACKET','main.py',816),
  ('MAT_BRACKET -> OPEN_BRACKET ID CLOSING_BRACKET','MAT_BRACKET',3,'p_MAT_BRACKET','main.py',817),
  ('MAT_BRACKET -> MAT_BRACKET OPEN_BRACKET ID CLOSING_BRACKET','MAT_BRACKET',4,'p_MAT_BRACKET','main.py',818),
]
