import ply.lex as lex
import ply.yacc as yacc
import sys
import os
from SymbolTable import SymbolTable
#from LexDefinition import *

"""
Paul Vazquez A00819877
"""
fileName = 'operations.cpp'


## ---------------- SymbolTable ---------------

SymbolTable = SymbolTable()
lista_var = []
value= None
## ---------------- Cuadruple ---------------
pila_operandos = []
pila_operadores = []
pila_saltos = []
contador_saltos = 0
contador_T = 0

contador_cuadruplos = 0
cuadruplos = []

def get_value(value):
	if(is_number(value)):
		return value
	element = SymbolTable.lookup(value)
	if element is None:
		raise Exception('variable {} not previously declared '.format(value))
	return element.value


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
	except TypeError:
		return False




## ---------------- LEXER ---------------

tokens = (
	#SPECIAL CHARACTERS
	"OPEN_BRACES", #{
	"CLOSING_BRACES",#}
	"COMA",#,
	"SEMICOLON", #;
	"OPEN_PARENTH", #(
	"CLOSING_PARENTH", #)
	"OPEN_BRACKET",#[
	"CLOSING_BRACKET",#]
	"COMMENT", #//

	#COMPARATION OPERATORS
	"EQUAL_EQUAL", #==
	"NOT_EQUAL",#!=
	"BIGGER_THAN",#>
	"LOWER_THAN",#<

	##ARITHMETIC OPERATORS
	"EQUAL",#=
	"PLUS",#+
	"MINUS",#-
	"MULTIPLY",#*
	"DIVISION",#/
	"PLUSPLUS", #++
	"MINUSMINUS",#--

	##BOOLEAN OPERATORS
	"OR",#||
	"AND",#&&
	"NOT",#!

	##RESERVED WORDS
	"ID",#id
	"PRINT",#print
	"READ",#read
	"IF",#if
	"ELSE",#else
	"WHILE",#while
	"DO",#do
	"FOR",#for
	"FUNCTION",#function
	"MAIN", #main

	##NUMERIC TYPES
	"INT", #int
	"DOUBLE", #double
	"CONSTANT", #digito+
	#string
	"STRING",#"(.)*"
)

precedence = (
    ('left', 'PLUS', 'MINUS'),
)
#ignorar espacios
t_ignore  = '\t | \n '

def t_COMMENT(t):
	r'\#.*'
	pass
	# No return value. Token discarded
def t_OPEN_BRACES(t):
	r'{'
	return t

def t_CLOSING_BRACES(t):
	r'}'
	return t

def t_COMA(t):
	r'\,'
	return t

def t_SEMICOLON(t):
	r'\;'
	return t

def t_OPEN_PARENTH(t):
	r'\('
	return t

def t_CLOSING_PARENTH(t):
	r'\)'
	return t

def t_OPEN_BRACKET(t):
	r'\['
	return t

def t_CLOSING_BRACKET(t):
	r'\]'
	return t

#COMPARATION
def t_EQUAL_EQUAL(t):
	r'=='
	return t

def t_NOT_EQUAL(t):
	r'!='
	return t

def t_BIGGER_THAN(t):
	r'>'
	return t

def t_LOWER_THAN(t):
	r'<'
	return t

#ARITMETHIC

def t_EQUAL(t):
	r'\='
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_MINUSMINUS(t):
	r'\-\-'
	return t

def t_PLUS(t):
	r'\+'
	return t

def t_MINUS(t):
	r'\-'
	return t

def t_MULTIPLY(t):
	r'\*'
	return t

def t_DIVISION(t):
	r'\/'
	return t

#BOOLEAN OPERATOR

def t_OR(t):
	r'\|\|'
	return t

def t_AND(t):
	r'&&'
	return t

def t_NOT(t):
	r'!'
	return t

#RESERVED WORDS

def t_PRINT(t):
	r'print'
	return t

def t_READ(t):
	r'read'
	return t

def t_IF(t):
	r'if'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_DO(t):
	r'\bdo\b'
	return t

def t_FOR(t):
	r'for'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_MAIN(t):
	r'main'
	return t

##NUMERIC TYPES
def t_INT(t):
	r'int'
	return t

def t_DOUBLE(t):
	r'double'
	return t

def t_CONSTANT(t):
	r'[-+]?[0-9]+[.]?[0-9]*'
	return t

def t_ID(t):
	r'(([a-z]+[A-Z]*[0-9]*)+)'
	return t

def t_STRING(t):
	r'"(.)*"'
	return t

#en caso de error
def t_error(t):
	print('Error de lexico: '+str(t))
	t.lexer.skip(1)


##----------------PARSER-----------------------
def p_PROGRAMA(p):
	'''
	PROGRAMA : VAR FUNC M
	'''


def p_VAR(p):
	'''
	VAR : TIPO DECLARE SEMICOLON
		| TIPO MAT SEMICOLON
		| VAR TIPO DECLARE SEMICOLON
		| VAR TIPO MAT SEMICOLON
		|
	'''
	tipo=""
	size  = len(p)
	global lista_var
	if(size == 4):
		tipo = p[1]
		#print("tipo " + p[1])
	elif(size ==5):
		tipo = p[2]
	for element in lista_var:
		SymbolTable.insert(id=element, tipo=tipo, attributes="")
	lista_var.clear()

def p_DECLARE(p):
	'''
	DECLARE : ID
			| DECLARE COMA ID
			| ASSIGN
			| DECLARE COMA ASSIGN
	'''
	size = len(p)
	global value
	global lista_var
	#print("size en declare" + str(size))
	if(size == 2):
		#print('En declare' + str(p[1]))
		element = p[1]
		lista_var.append(element)
	elif(size == 4):
		element = p[3]
		lista_var.append(element)


def p_ASSIGN(p):
	'''
	ASSIGN : ID EQUAL EA
	'''
	global lista_var
	lista_var.append(p[1])
	#Cuadruplo de asignacion
	ea = pila_operandos.pop()
	print('= ' + str(ea) +' $ ' + str(p[1]))
	p[0] = p[1]

def p_FUNC(p):
	'''
	FUNC : FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES
		| FUNC FUNCTION ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES
		|
	'''

def p_M(p):
	'''
	M    : MAIN OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES S CLOSING_BRACES
	'''
def p_TIPO(p):
	'''
	TIPO : INT
		| DOUBLE
	'''
	if(p[1]=="int"):
		p[0]="int"
	else:
		p[0]="double"



##----------------------STATEMENTS----------------------
def p_S(p):
	'''
	S : STATEMENTS
	| S STATEMENTS
	|
	'''
def p_STATEMENTS(p):
	'''
	STATEMENTS : VAR 
			| IDSTAT
			| PRINTSTAT
			| READSTAT
			| IFSTAT
			| WHILESTAT
			| DOSTAT
			| FORSTAT
			| FUNCSTAT
			| INC_STAT
			| 
	'''

def p_IDSTAT(p):
	'''
	IDSTAT : ASSIGN SEMICOLON
		
	'''

def p_PRINTSTAT(p):
	'''
	PRINTSTAT : PRINT OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON
			| PRINT OPEN_PARENTH STRING CLOSING_PARENTH SEMICOLON
	'''

def p_READSTAT(p):
	'''
	READSTAT : READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON
	'''

def p_IFSTAT(p):
	'''
	IFSTAT : IF OPEN_PARENTH EL CLOSING_PARENTH IN_S
		| IF OPEN_PARENTH EL CLOSING_PARENTH IN_S ELSE IN_S
	'''
	size = len(p)
	global contador_saltos
	global pila_operandos
	if(size == 8):
		#There is an else
		dir_1 = pila_saltos.pop()
		print("GOTO " + "____")
		pila_saltos.append(contador_saltos-1)
		# fill(dir1,cont)
	dir = pila_saltos.pop()
	# fill(dir,cont)

def p_WHILESTAT(p):
	'''
	WHILESTAT : WHILE OPEN_PARENTH EL CLOSING_PARENTH IN_S
	'''

def p_DOSTAT(p):
	'''
	DOSTAT : DO IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON
	'''

def p_FORSTAT(p):
	'''
	FORSTAT : FOR OPEN_PARENTH ID EQUAL EA SEMICOLON EL SEMICOLON ID EQUAL EA CLOSING_PARENTH IN_S
	'''


def p_FUNCSTAT(p):
	'''
	FUNCSTAT : ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON
	'''

def p_INC_STAT(p):
	'''
	INC_STAT : ID PLUSPLUS SEMICOLON
			| ID MINUSMINUS SEMICOLON
	'''

def p_IN_S(p):
	'''
	IN_S : OPEN_BRACES S CLOSING_BRACES
	'''


##----------------------EXPRESIONES----------------------
def p_EA(p):
	'''
	EA : TA
	| EA PLUS TA
	| EA MINUS TA
	'''
	size = len(p)
	global contador_T
	global pila_operandos
	cuadruplos = True
	#print(pila_operandos)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		# Check if operands in SymbolTable

		if(cuadruplos):
			res = 'T_' + str(contador_T)
		else:
			res =0
		if(p[2]=='+'):
			if(not cuadruplos): res = op_1 + op_2
			print('+ ' + str(op_1 )+ ' ' + str(op_2)+ ' ' + str(res))
			if(cuadruplos): contador_T=contador_T+1
			pila_operandos.append(res)
		elif(p[2]=='-'):
			if(not cuadruplos): res = op_1 - op_2
			print('- ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if(cuadruplos): contador_T=contador_T+1
		else:
			print("Unknown operator")
	else:
		p[0]=p[1]

def p_FA(p):
	'''
	FA  : CONSTANT
		| ID
		| MAT
		| OPEN_PARENTH EA CLOSING_PARENTH
	'''
	#CUADRUPLOS
	global pila_operandos
	size = len(p)
	if(size == 2):
		element = SymbolTable.lookup(p[1])
		if(element is not None):
			#print("Variable " +p[1])
			pila_operandos.append(element.id)
		elif(is_number(p[1])):
			pila_operandos.append(float(p[1]))
		else:
			#No existe
			#print("Constant " + p[1])
			raise Exception("variable {} no previously declared".format(p[1]))
		p[0]=p[1]

def p_TA(p):
	'''
	TA : FA
	| TA MULTIPLY FA
	| TA DIVISION FA
	'''
	# CUADRUPLOS
	global contador_T
	global pila_operandos
	size = len(p)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		cuadruplos = True
		if(cuadruplos):
			res = 'T_' + str(contador_T)
		else:
			res = 0
		if(p[2]=='*'):
			if(not cuadruplos): res = op_1 * op_2
			print('* ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		elif(p[2]=='/'):
			if(not cuadruplos): res = op_1 / op_2
			print('/ ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		else:
			print("Unknown operator")
	else:
		p[0] = p[1]

def p_EL(p):
	'''
	EL : TL
	| EL OR TL
	'''
	size= len(p)
	global contador_T
	global pila_operandos

	#print(pila_operandos)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		cuadruplos = True
		if(cuadruplos):
			res = 'T_' + str(contador_T)
		if(p[2]=='||'):
			print('|| ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		else:
			print("Unknown operator")

	Result_Logic = pila_operandos.pop()
	print("GOTO " + str(Result_Logic) + "____")
	pila_saltos.append(contador_saltos-1)

def p_TL(p):
	'''
	TL : FL
	| TL AND FL
	'''
	size= len(p)
	global contador_T
	global pila_operandos
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		cuadruplos = True
		if(cuadruplos):
			res = 'T_' + str(contador_T)
		if(p[2]=='&&'):
			print('&& ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		else:
			print("Unknown operator")

def p_FL(p):
	'''
	FL : NL OPERATORS NL
	| EA OPERATORS EA
	| NL
	| OPEN_PARENTH EL CLOSING_PARENTH
	'''
#Puedo comparar con una expresion aritmetica?
	size= len(p)
	global contador_T
	global pila_operandos
	if(size==4 and p[1]!='('):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		cuadruplos = True
		if(cuadruplos):
			res = 'T_' + str(contador_T)
		if(p[2]=='!='):
			print('!= ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		elif(p[2]=='=='):
			print('== ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		elif(p[2]=='>'):
			print('> ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		elif(p[2]=='<'):
			print('< ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			if cuadruplos: contador_T=contador_T+1
		else:
			print("Unknown operator")


def p_NL(p):
	'''
	NL : NOT EL
	'''
	size = len(p)
	global contador_T
	global pila_operandos
	if(size==3):
		# case !(EA)
		op_1 = pila_operandos.pop()
		cuadruplos = True
		if(cuadruplos):
			res = 'T_' + str(contador_T)
		if(p[1]=='!'):
			print('! ' + str(op_1)+ ' $ ' + ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1

def p_OPERATORS(p):
	'''
	OPERATORS : NOT_EQUAL
			| LOWER_THAN
			| BIGGER_THAN
			| EQUAL_EQUAL
	'''
	p[0] = p[1]

def p_MAT(p):
	'''
	MAT : ID MAT_BRACKET
	'''
	p[0] = p[1]
	lista_var.append(p[1])

def p_MAT_BRACKET(p):
	'''
	MAT_BRACKET : OPEN_BRACKET CONSTANT CLOSING_BRACKET
				| MAT_BRACKET OPEN_BRACKET CONSTANT CLOSING_BRACKET
				| OPEN_BRACKET ID CLOSING_BRACKET
				| MAT_BRACKET OPEN_BRACKET ID CLOSING_BRACKET
	'''




#error en gramatica
def p_error(p):
	raise Exception("Error en la GRAMATICA")

##----------------------MAIN----------------------
def printAtttributes(p):
	print("------")
	print(len(p))
	for each in p:
		print(each)
	print("------")


def tryLexer(lexer):
	global fileName
	#Prueba que el lexer funcione
	output = open('output.txt','w')
	with open(fileName, 'r') as file:
		data = file.read()
		lexer.input(data)
		while True:
			tok = lexer.token()
			if not tok:
					break
			# No more input
			output.write(str(tok)+'\n')
	output.close()

def tryParser(lexer,parser):
#Probar oraciones en la lista de oraciones
	fileS =(
		"function perro(){}main(){}",
		"function nada(){a = 3;} main(){}"
	)
	for sentence in fileS:
		print ("\n" + sentence)
		result = parser.parse(sentence)
		if(result):
			print(result)
		print("-----------")

def tryParserOnFile(lexer,parser):
	global fileName
	with open(fileName, 'r') as file:
		data = file.read()
		#print(data)
		data = data.replace('\n', '')
		parser.parse(data)
		print("-----------")
		print("Gramatica y Sintaxis correcta")
		print("-----------")

if __name__ =="__main__":
	os.listdir()
	count = 0
	lexer = lex.lex()
	parser = yacc.yacc(start="PROGRAMA")
	tryLexer(lexer)
	tryParserOnFile(lexer,parser)
	SymbolTable.print()
	print("PILA DE OPERANDOS")