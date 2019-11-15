import numpy as np
#from compile_run import is_number,is_array,get_value
list_arrays = []

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
	except TypeError:
		return False

def array_lookup(stack_indexes, starting_index,SymbolTable,avail):
    global list_arrays
    last_index = stack_indexes.pop()
    starting_index = get_value(starting_index,SymbolTable=SymbolTable,avail=avail)
    lista = list_arrays[int(starting_index)]
    for index in stack_indexes:
        index =  get_value(index,SymbolTable=SymbolTable,avail=avail)
        lista = lista[int(index)]
    last_index =  get_value(starting_index,SymbolTable=SymbolTable,avail=avail)
    return  lista[int(last_index)]


def array_set(list_arrays, stack_indexes, value,SymbolTable,avail):
    if(len(stack_indexes)==1):
        indice = get_value(stack_indexes[0],SymbolTable=SymbolTable,avail=avail)
        list_arrays[int(indice)] = value
    else:
        indice = get_value(stack_indexes[0],SymbolTable=SymbolTable,avail=avail)
        array_set(list_arrays[int(indice)],stack_indexes[1:],value,SymbolTable,avail)
##definicion de la funcion execute
def execute(SymbolTable,cuadruplos,list_arrays_local):
    global list_arrays
    list_arrays = np.asarray(list_arrays_local)
    avail = {}
    OP_CODE = ""
    PC = 0
    OP_CODE =   cuadruplos[PC][0]
    call_stack = []
    while(OP_CODE is not "END"):
        OP_CODE = cuadruplos[PC][0]
        PC  = process_command(SymbolTable,cuadruplos[PC], avail,call_stack,PC)
        

def process_command(SymbolTable,cuadruplo, avail,call_stack,PC):
    OP_CODE= cuadruplo[0]
    # JUMP SECTION
    if(OP_CODE == "END"):
        return
    elif(OP_CODE == "CALL"):
        #FUNCTION CALL
        call_stack.append(PC)
        PC = int(cuadruplo[1])
    elif(OP_CODE == "GOTOF"):
        #GOTO CONDITION FALSE
        T = cuadruplo[1]
        condicion = avail.get(T)
        salto = cuadruplo[2]
        #BUscar condicion en avail
        if(condicion is not None):
            if(condicion==False):
                PC = int(salto)
            else:
                PC = PC +1
        else:
            raise Exception("T not found in avail (GOTOF)")
    elif(OP_CODE == "GOTO"):
        # JUMP TO LINE
        PC = int(cuadruplo[1])
    elif(OP_CODE == "GOTOT"):
        # JUMP IF TRUE
        T = cuadruplo[1]
        condicion = avail.get(T)
        salto = cuadruplo[2]
        #BUscar condicion en avail
        if(condicion is not None):
            if(condicion==True):
                PC = int(salto)
            else:
                PC = PC +1
        else:
            raise Exception("T not found in avail (GOTO)")
    elif(OP_CODE == "RETURN"):
        PC = call_stack.pop()+1
    elif(OP_CODE == "PRINT"):
        if(cuadruplo[1]=="\"endl\""):
            print("")
        elif(cuadruplo[1][0]=="\""):
            print(cuadruplo[1][1:-1],end = '')
        else:
            val = get_value(cuadruplo[1],SymbolTable,avail)
            print(str(val),end = '')
        PC = PC + 1
    elif(OP_CODE == "READ"):
        ID = cuadruplo[1]
        val = input("")
        set_value(ID,SymbolTable, avail, val)
        #Look in symbol table 
        PC = PC +1
    else:
        # OPERATION
        process_command_expression(SymbolTable,cuadruplo, avail,call_stack,PC)
        #Increment PC
        PC = PC + 1
    return PC


def process_command_expression(SymbolTable,cuadruplo, avail,call_stack,PC):
    OP_CODE= cuadruplo[0]
    res = None
    op_2 =get_value(cuadruplo[1],SymbolTable,avail)
    #Expresiones artmeticas
    if(OP_CODE == "+"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 + op_2
    elif(OP_CODE =="-"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 - op_2
    elif(OP_CODE == "*"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 * op_2
    elif(OP_CODE == "/"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 / op_2
    elif(OP_CODE == "="):
        res = get_value(cuadruplo[1],SymbolTable,avail)
    #Expresiones logicas
    if(OP_CODE == "&&"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 and op_2
    elif(OP_CODE =="||"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 or op_2
    elif(OP_CODE == ">"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 > op_2
    elif(OP_CODE == "<"):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 < op_2
    elif(OP_CODE == "=="):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 == op_2
    elif(OP_CODE == "!="):
        op_1 =get_value(cuadruplo[2],SymbolTable,avail)
        res = op_1 != op_2
    elif(OP_CODE == "!"):
        res = not op_2

    set_value(cuadruplo[3],SymbolTable,avail,res)

def set_value(ID,SymbolTable, avail, res):
    global list_arrays
    if(ID[0]=="["):
        ID, stack_indexes= parse_matrix(ID[1:])
        starting_index = get_value(ID,SymbolTable,avail) 
        stack_indexes.insert(0,starting_index)
        array_set(list_arrays,stack_indexes,res,SymbolTable, avail)
        return
    query = SymbolTable.lookup(ID)
    if(query is not None):
        SymbolTable.update(ID,res)
    else:
        #Look in avail
        T = avail.get(ID)
        avail[ID] = res

def parse_matrix(ID_MAT):
    LIST_MAT= ID_MAT.split("-")
    return LIST_MAT[0], LIST_MAT[1:]

def get_value(ID,SymbolTable,avail):
    if(is_number(ID)):
        return float(ID)
    # Check if it starts with a  [
    if(ID[0]=="["):
        ID, stack_indexes= parse_matrix(ID[1:])
        starting_index = get_value(ID,SymbolTable,avail)
        ele = array_lookup(stack_indexes=stack_indexes,starting_index=starting_index,SymbolTable=SymbolTable, avail=avail)
        
        return ele
    query = SymbolTable.lookup(ID)
    if(query is not None):
        if(query.tipo == "int" or query.tipo == "double"):
            return float(query.attributes)
        return query.attributes
    else:
        #Look in avail
        T = avail.get(ID)
        if(T is not None):
            return T
        else:
            raise Exception(" not found get_value")
