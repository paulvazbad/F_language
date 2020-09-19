import ply.lex as lex
import ply.yacc as yacc
import sys
import os
import numpy as np
from SymbolTable import SymbolTable
from execute_f import execute
#from LexDefinition import *

"""
Paul Vazquez A00819877
"""
fileName = 'variables_simples.cpp'


## ---------------- SymbolTable ---------------

SymbolTable = SymbolTable()
lista_var = []
value= None
## ---------------- Cuadruple ---------------
pila_operandos = []
pila_operadores = []
pila_saltos = []
contador_T = 0

contador_cuadruplos = 0
cuadruplos = []

func_id = ""
line_number = -1


def debug(ele):
	output=False
	if(output==True):
		print(ele)

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

def print_cuadruplos():
	f = open("cuadruplos.txt", "w")
	f.write("")
	f.close()
	f = open("cuadruplos.txt", "a")
	for index,element in enumerate(cuadruplos):
		debug(str(index)+" --> "+str(element))
		f.write(str(index)+" --> "+str(element)+"\n")
	f.close()


def fill(dir1,cont):
	debug("Relleno el espacio en la direccion: " + str(dir1)+" con "+str(cont))
	global cuadruplos
	position_fill = cuadruplos[dir1]
	# Last position
	cuadruplos[dir1][-1] = str(cont)


## ---------------- MATRIX ---------------

def  initialize_list(n):
	for i in range(0,n):
		return [0]*n


def recursive_generation(depth,lista,stack_dimensions):
    if(depth>0):
        number_elements= stack_dimensions.pop(0)
        new_lista = initialize_list(number_elements)
        for index,ele in enumerate(lista):
            lista[index] = new_lista
        lista = lista[0]
        depth= depth-1
        recursive_generation(depth,lista,stack_dimensions)
    return lista


def print_lista_arrays():
	for index,ele in enumerate(list_arrays):
		debug("Lista en la posicion " + str(index))
		debug(ele)


def is_array(id):
	ele = SymbolTable.lookup(id)
	if(ele is None):
		raise Exception('variable {} not previously declared '.format(id))
	if(ele.tipo[0] =="["):
		return True
	return False

list_arrays = []

stack_dimension = []
global_dimension = 0
tamano = 1
list_indexes = []

stack_list_indexes = []
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
	r'(/\*(.|\n)*?\*/)|(//.*)'
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
	r'"((?!").)*"'
	return t

#en caso de error
def t_error(t):
	debug('Error de lexico: '+str(t))
	t.lexer.skip(1)


##----------------PARSER-----------------------
def p_PROGRAMA(p):
	'''
	PROGRAMA : VAR FUNC M
	'''
	# Generar cuadruplo de fin de programa
	global cuadruplos
	# Generar cuadruplo RETURN
	local_cuad = []
	local_cuad.append("END")
	cuadruplos.append(local_cuad)
	#
	debug("END ")

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
	global stack_dimension
	global tamano
	global stack_list_indexes
	dimension = 0
	list_indexes=[]
	if(len(stack_dimension)>0):
		dimension = stack_dimension.pop()
		list_indexes = stack_list_indexes.pop()
	if(dimension>0):
		##declaration of n-dimensional array
		debug("n-dimentional_array")
		debug("--------------------------")
		debug("tamano " + str(tamano))
		debug('dimension' + str(dimension))	
		
		debug("indexes" + str(list_indexes))
		debug("id:" + str(p[3]))
		debug("--------------------------")
		
		if(size==5):
			id = p[3]
			tipo = p[2]
		else:
			id = p[2]
			tipo = p[1]
	

		##declare in SymbolTable
		position_in_lista_arrays = len(list_arrays)
		SymbolTable.insert(id=id,tipo='['+p[2],attributes=position_in_lista_arrays)
		##initialize in lista_arrays
		lista_local=[None]
		list_indexes = list(map(int, list_indexes))
		list_arrays.append(recursive_generation(int(dimension),lista_local,list_indexes))
	else:
		if(size == 4):
			tipo = p[1]
		#debug("tipo " + p[1])
		elif(size ==5):
			tipo = p[2]
		for element in lista_var:
			SymbolTable.insert(id=element, tipo=tipo, attributes=0.0)
		lista_var.clear()
	tamano = 1
	list_indexes = []

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
	#debug("size en declare" + str(size))
	if(size == 2):
		#debug('En declare' + str(p[1]))
		element = p[1]
		lista_var.append(element)
	elif(size == 4):
		element = p[3]
		lista_var.append(element)


def p_ASSIGN(p):
	'''
	ASSIGN : ID EQUAL EA
			| MAT EQUAL EA
	'''
	global lista_var
	global cuadruplos
	global stack_dimension	
	global stack_list_indexes
	dimension = 0	
	if(len(stack_dimension)>0):
		dimension = stack_dimension.pop()
	#Cuadruplo de asignacion
	ea = pila_operandos.pop()
	local_cuad = []
	local_cuad.append('=')
	local_cuad.append(str(ea))
	local_cuad.append('$')
	debug("ASSIGN" + p[1]+" " +  str(dimension))

	## And is of type mat
	is_arr = is_array(p[1])
	if(dimension>0 and  is_arr):
		debug("ASSIGN TO MAT")
		debug(stack_list_indexes)
		list_indexes = stack_list_indexes.pop()
		
		indexes = '-'.join([str(elem) for elem in list_indexes]) 
		local_cuad.append('['+p[1]+'-'+indexes)
		dimension=0
	else:
		lista_var.append(p[1])
		local_cuad.append(p[1])
		debug('= ' + str(ea) +' $ ' + str(p[1]))
	cuadruplos.append(local_cuad)
	p[0] = p[1]

def p_FUNC(p):
	'''
	FUNC :  FUNCTION AUX_FUNC SET_ID OPEN_PARENTH CLOSING_PARENTH DECLARE_FUNC OPEN_BRACES S CLOSING_BRACES RETURN IF_AUX3
		|  FUNC AUX_FUNC FUNCTION SET_ID OPEN_PARENTH CLOSING_PARENTH OPEN_BRACES DECLARE_FUNC S CLOSING_BRACES  RETURN IF_AUX3
		|  empty
	'''


def p_SET_ID(p):
	'''
	SET_ID : ID
	'''
	global func_id
	debug("set_function_id")
	func_id = p[1]

def p_DECLARE_FUNC(p):
	'''
	DECLARE_FUNC : empty
	'''
	global func_id
	global line_number
	debug("REgister new function")
	debug('FUnc id' + func_id)
	debug("line_number" + str(line_number))
	SymbolTable.insert(id=func_id, tipo="void", attributes=line_number)

def p_RETURN(p):
	'''
	RETURN  : empty
	'''
	global cuadruplos
	# Generar cuadruplo RETURN
	local_cuad = []
	local_cuad.append("RETURN")
	cuadruplos.append(local_cuad)
	#
	debug("RETURN " + "____")

def p_AUX_FUNC(p):
	'''
	AUX_FUNC : empty
	'''
	global pila_operandos
	global cuadruplos
	global pila_saltos
	global line_number
	

	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTO")
	local_cuad.append("___")
	cuadruplos.append(local_cuad)
	#
	contador_cuadruplos = len(cuadruplos)
	pila_saltos.append(contador_cuadruplos-1)
	debug("GOTO " + "____")
	line_number = contador_cuadruplos
	p[0]= contador_cuadruplos


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
	global cuadruplos
	local_cuad = []
	local_cuad.append("PRINT")
	debug("EEEEEEEEEEEEEEEEEEEEEE")
	debug(p[3])
	debug("AAAAAAAAAA")
	local_cuad.append(p[3])
	cuadruplos.append(local_cuad)


def p_READSTAT(p):
	'''
	READSTAT : READ OPEN_PARENTH EA CLOSING_PARENTH SEMICOLON
	'''
	global cuadruplos
	local_cuad = []
	local_cuad.append("READ")
	local_cuad.append(p[3])
	cuadruplos.append(local_cuad)

def p_IFSTAT(p):
	'''
	IFSTAT : IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S IF_AUX3
		| IF OPEN_PARENTH EL CLOSING_PARENTH IF_AUX1 IN_S ELSE IF_AUX2 IN_S IF_AUX3
	'''


def p_IF_AUX1(p):
	'''
	IF_AUX1 : empty
	'''
	global pila_operandos
	global cuadruplos
	global pila_saltos
	
	Result_Logic = pila_operandos.pop()
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTOF")
	local_cuad.append(str(Result_Logic))
	local_cuad.append("___")
	cuadruplos.append(local_cuad)
	#
	contador_cuadruplos = len(cuadruplos)
	pila_saltos.append(contador_cuadruplos-1)
	debug("GOTO " + str(Result_Logic) + "____")


def p_IF_AUX2(p):
	'''
	IF_AUX2 : empty
	'''
	global pila_operandos
	global cuadruplos
	global pila_saltos
	dir_1 = pila_saltos.pop()
	cuadruplos.append(["GOTO","___"])
	debug("GOTO " + "____")
	contador_cuadruplos = len(cuadruplos)
	pila_saltos.append(contador_cuadruplos-1)
	fill(dir_1,contador_cuadruplos)

def p_IF_AUX3(p):
	'''
	IF_AUX3 : empty
	'''
	global pila_operandos
	global cuadruplos
	global pila_saltos
	dir_1 = pila_saltos.pop()
	contador_cuadruplos = len(cuadruplos)
	fill(dir_1,contador_cuadruplos)


def p_empty(p):
     'empty :'
     pass

def p_WHILESTAT(p):
	'''
	WHILESTAT : WHILE WHILE_AUX_1 OPEN_PARENTH EL CLOSING_PARENTH WHILE_AUX_2 IN_S
	'''
	global pila_saltos
	global cuadruplos
	dir1 = pila_saltos.pop()
	dir2= pila_saltos.pop()
	global cuadruplos
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTO")
	local_cuad.append(str(dir2))
	cuadruplos.append(local_cuad)
	#
	fill(dir1,len(cuadruplos))


def p_WHILE_AUX_1(p):
	'''
	WHILE_AUX_1 : empty
	'''
	global pila_saltos
	global cuadruplos
	pila_saltos.append(len(cuadruplos))



def p_WHILE_AUX_2(p):
	'''
	WHILE_AUX_2 : empty
	'''
	global pila_operandos
	global cuadruplos
	Result_Logic = pila_operandos.pop()
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTOF")
	local_cuad.append(str(Result_Logic))
	local_cuad.append("___")
	cuadruplos.append(local_cuad)
	#
	contador_cuadruplos = len(cuadruplos)
	pila_saltos.append(contador_cuadruplos-1)
	debug("GOTOF " + str(Result_Logic) + "____")

def p_DOSTAT(p):
	'''
	DOSTAT : DO WHILE_AUX_1 IN_S WHILE OPEN_PARENTH EL CLOSING_PARENTH SEMICOLON
	'''
	global pila_operandos
	global cuadruplos
	Result_Logic = pila_operandos.pop()
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTOT")
	local_cuad.append(str(Result_Logic))
	local_cuad.append("___")
	cuadruplos.append(local_cuad)
	#
	debug("GOTOT " + str(Result_Logic) + "____")
	contador_cuadruplos = len(cuadruplos)

	fill(contador_cuadruplos-1,pila_saltos.pop())


def p_FORSTAT(p):
	'''
	FORSTAT : FOR OPEN_PARENTH ASSIGN SEMICOLON WHILE_AUX_1 EL SEMICOLON WHILE_AUX_2 ASSIGN FOR_INCREMENT CLOSING_PARENTH  IN_S
	'''
	global pila_saltos
	global cuadruplos
	# Meter la asignacion
	debug("METO EN FOR ANTES DE LOS SALTOS")
	for each in p[10][::-1]:
		debug(each)
		cuadruplos.append(each)
	dir1 = pila_saltos.pop()
	dir2= pila_saltos.pop()
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("GOTO")
	local_cuad.append(str(dir2))
	cuadruplos.append(local_cuad)
	#
	fill(dir1,len(cuadruplos))


def p_FOR_INCREMENT(p):
	'''
	FOR_INCREMENT : empty
	'''
	global cuadruplos
	local_cuad = []
	while(cuadruplos[-1][0]!="GOTOF"):
		local_cuad.append(cuadruplos.pop())
	p[0] = local_cuad

def p_FUNCSTAT(p):
	'''
	FUNCSTAT : ID OPEN_PARENTH CLOSING_PARENTH SEMICOLON
	'''
	global pila_saltos
	global cuadruplos
	id = p[1]
	# Generar cuadruplo
	local_cuad = []
	local_cuad.append("CALL")
	# Sacar line_number de la funcion de la SymbolTable
	result = SymbolTable.lookup(id=id)
	if(result==None):
		raise Exception('function "{}" not previously declared '.format(id))
	debug(result)
	local_cuad.append(result.attributes)
	cuadruplos.append(local_cuad)
	#



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
	global cuadruplos
	local_cuad = []
	debug("--------------------EVALUO EA----------------")
	#debug(pila_operandos)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		# Check if operands in SymbolTable
		res = 'T_' + str(contador_T)
		if(p[2]=='+'):
			local_cuad.append('+')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			contador_T=contador_T+1
			pila_operandos.append(res)
		elif(p[2]=='-'):
			local_cuad.append('-')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			debug('- ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		else:
			debug("Unknown operator")
		cuadruplos.append(local_cuad)
	else:
		debug("REgerso el resultado")
		debug(p[1])
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
	dimension = 0
	global stack_dimension
	global stack_list_indexes
	size = len(p)
	if(size == 2):
		element = SymbolTable.lookup(p[1])
		if(element is not None):
			#debug("Variable " +p[1])
			if(len(stack_dimension)>0) and is_array(p[1]):
				dimension = stack_dimension.pop()
			if (dimension>1):
				#Is matrix
				list_indexes = stack_list_indexes.pop()
				debug("indexes" + str(list_indexes))
				debug(p[1])
				#special format
				indexes = '-'.join([str(elem) for elem in list_indexes]) 
				pila_operandos.append('['+element.id+'-'+indexes)
				dimension = 0
			else:
				#normal variable
				pila_operandos.append(element.id)
		elif(is_number(p[1])):
			pila_operandos.append(float(p[1]))
		else:
			#No existe
			#debug("Constant " + p[1])
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
	global cuadruplos
	local_cuad = []
	size = len(p)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		res = 'T_' + str(contador_T)
		if(p[2]=='*'):
			local_cuad.append('*')
			local_cuad.append(op_1)
			local_cuad.append(op_2)
			local_cuad.append(res)
			#debug('* ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		elif(p[2]=='/'):
			local_cuad.append('/')
			local_cuad.append(op_1)
			local_cuad.append(op_2)
			local_cuad.append(res)
			#debug('/ ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		else:
			debug("Unknown operator")
		cuadruplos.append(local_cuad)
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
	global cuadruplos
	local_cuad = []
	#debug(pila_operandos)
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		res = 'T_' + str(contador_T)
		if(p[2]=='||'):
			local_cuad.append('||')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('|| ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
			cuadruplos.append(local_cuad)
		else:
			debug("Unknown operator")
	
	
	

def p_TL(p):
	'''
	TL : FL
	| TL AND FL
	'''
	size= len(p)
	global contador_T
	global pila_operandos
	global cuadruplos
	local_cuad = []
	if(size==4):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		res = 'T_' + str(contador_T)
		if(p[2]=='&&'):
			local_cuad.append('&&')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('&& ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
			cuadruplos.append(local_cuad)
		else:
			debug("Unknown operator")

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
	global cuadruplos
	local_cuad = []
	if(size==4 and p[1]!='('):
		op_1 = pila_operandos.pop()
		op_2 = pila_operandos.pop()
		res = 'T_' + str(contador_T)
		if(p[2]=='!='):
			local_cuad.append('!=')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('!= ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		elif(p[2]=='=='):
			local_cuad.append('==')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('== ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		elif(p[2]=='>'):
			local_cuad.append('>')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('> ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		elif(p[2]=='<'):
			local_cuad.append('<')
			local_cuad.append(str(op_1))
			local_cuad.append(str(op_2))
			local_cuad.append(str(res))
			#debug('< ' + str(op_1)+ ' ' + str(op_2)+ ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		else:
			debug("Unknown operator")
		cuadruplos.append(local_cuad)


def p_NL(p):
	'''
	NL : NOT EL
	'''
	size = len(p)
	global contador_T
	global pila_operandos
	global cuadruplos
	local_cuad = []
	if(size==3):
		# case !(EA)
		op_1 = pila_operandos.pop()
		res = 'T_' + str(contador_T)
		if(p[1]=='!'):
			local_cuad.append('!')
			local_cuad.append(str(op_1))
			local_cuad.append('$')
			local_cuad.append(str(res))
			debug('! ' + str(op_1)+ ' $ ' + ' ' + str(res))
			pila_operandos.append(res)
			contador_T=contador_T+1
		cuadruplos.append(local_cuad)

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
	global global_dimension
	global stack_dimension
	global stack_list_indexes
	global list_indexes
	p[0] = p[1]
	stack_dimension.append(global_dimension)
	debug("append to stack_list_indexes" + str(list_indexes))
	stack_list_indexes.append(list_indexes)
	global_dimension = 0
	list_indexes = []

def p_MAT_BRACKET(p):
	'''
	MAT_BRACKET : OPEN_BRACKET EA CLOSING_BRACKET
				| MAT_BRACKET OPEN_BRACKET EA CLOSING_BRACKET
	'''
	global global_dimension
	global tamano
	global list_indexes
	global pila_operandos
	global_dimension = global_dimension+1
	size = len(p)
	debug("EVALUO ADENTRO DE BRACKET")
	debug(pila_operandos)
	debug("YA PASO")
	if(size == 4):
		debug(p[2])
		list_indexes.append(pila_operandos.pop())
		if(is_number(p[2])):
			tamano = tamano * int(p[2])
	else:
		debug(p[3])
		list_indexes.append(pila_operandos.pop())
		if(is_number(p[3])):	
			tamano = tamano * int(p[3])



#error en gramatica
def p_error(p):
	raise Exception("Error en la GRAMATICA")

##----------------------MAIN----------------------
def printAtttributes(p):
	debug("------")
	debug(len(p))
	for each in p:
		debug(each)
	debug("------")


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
			debug(result)
		debug("-----------")

def tryParserOnFile(lexer,parser,args):
	global fileName
	if(len(args)>1):
		fileName = args[1]
	with open(fileName, 'r') as file:
		data = file.read()
		#debug(data)
		data = data.replace('\n', '')
		parser.parse(data)
		debug("-----------")
		debug("Gramatica y Sintaxis correcta")
		debug("-----------")

if __name__ =="__main__":
	args = sys.argv
	os.listdir()
	count = 0
	lexer = lex.lex()
	parser = yacc.yacc(start="PROGRAMA")
	tryLexer(lexer)
	tryParserOnFile(lexer,parser,args)
	print_cuadruplos()
	#SymbolTable.print()

	print_lista_arrays()
	## acceder a un elemento
	debug(str(stack_dimension))
	debug("---------------------EXECUTION-----------------")
	##Program Execution
	execute(SymbolTable=SymbolTable,cuadruplos=cuadruplos, list_arrays_local=list_arrays)