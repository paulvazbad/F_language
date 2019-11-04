
def defineTokens():

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
    #COMPARATION OPERATORS
    "EQUAL_EQUAL", #==
    "NOT_EQUAL",#!=
    "BIGGER_THAN",#>
    "LOWER_THAN",#<
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
    "id"#letra(letra/digito)*
)
    return tokens

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
     r'('
     return t

def t_CLOSING_PARENTH(t):
     r')'
     return t

def t_OPEN_BRACKET(t):
     r'['
     return t

def t_CLOSING_BRACKET(t):
     r']'
     return t

#ARITMETHIC

def t_EQUAL(t):
     r'='
     return t
def t_PLUS(t):
     r'+'
     return t

def t_MINUS(t):
     r'-'
     return t

def t_MULTIPLY(t):
     r'*'
     return t

def t_DIVISION(t):
     r'/'
     return t

def t_PLUSPLUS(t):
     r'++'
     return t

def t_MINUSMINUS(t):
     r'--'
     return t

#BOOLEAN OPERATOR

def t_OR(t):
     r'||'
     return t

def t_AND(t):
     r'&&'
     return t


def t_NOT(t):
     r'!'
     return t

#COMPARATION 
def t_EQUALEQUAL(t):
     r'=='
     return t

def T_NOT_EQUAL(t):
     r'!='
     return t

def t_BIGGER_THAN(t):
     r'>'
     return t

def t_LOWER_THAN(t):
     r'<'
     return t

#RESERVED WORDS

def t_ID(t):
     r'([a-z]+[0-9]*)'
     return t

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
     r'do'
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
     r']'
     return t

def t_CONSTANT(t):
     r'^[-+]?[0-9]+[.]?[0-9]*'
     return t

