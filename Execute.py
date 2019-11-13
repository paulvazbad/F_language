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

def array_lookup(stack_indexes, starting_index):
    print("EN ARRAY_LOOKUP")
    last_index = stack_indexes.pop()
    lista = list_arrays[int(float(starting_index))]
    for index in stack_indexes:
        lista = lista[int(float(index))]
    print("ELEMENTO SELECCIONADO")
    print(lista[int(float(last_index))])
    return  lista[int(float(last_index))]
        
def array_set(stack_indexes, starting_index, value):
    print("EN ARRAY_LOOKUP")
    last_index = stack_indexes.pop()
    lista = list_arrays[int(float(starting_index))]
    for index in stack_indexes:
        lista = lista[int(float(index))]
    print("ELEMENTO SELECCIONADO")
    print(lista[int(float(last_index))])
    lista[int(float(last_index))] = value

##definicion de la funcion execute
def execute(SymbolTable,cuadruplos,list_arrays_local):
    global list_arrays
    list_arrays = list_arrays_local
    avail = {}
    print("--------------------- EXECUTION----------------------")
    OP_CODE = ""
    PC = 0
    OP_CODE =   cuadruplos[PC][0]
    call_stack = []
    while(OP_CODE is not "END"):
        OP_CODE = cuadruplos[PC][0]
        print(PC)
        PC  = process_command(SymbolTable,cuadruplos[PC], avail,call_stack,PC)
        
    SymbolTable.print()
    print(avail)

def process_command(SymbolTable,cuadruplo, avail,call_stack,PC):
    OP_CODE= cuadruplo[0]
    # JUMP SECTION
    if(OP_CODE == "END"):
        return
    elif(OP_CODE == "CALL"):
        #FUNCTION CALL
        call_stack.append(PC)
        PC = int(cuadruplo[1])
        print("FUNCTIONCALL")
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
        print("GOTO_FALSE")
    elif(OP_CODE == "GOTO"):
        # JUMP TO LINE
        PC = int(cuadruplo[1])
        print("GOTO")
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
        print("JUMP IF TRUE")
    elif(OP_CODE == "RETURN"):
        PC = call_stack.pop()+1
        print("RETURN")
    elif(OP_CODE == "PRINT"):
        val = get_value(cuadruplo[1],SymbolTable,avail)
        print("-----------------------CONSOLE OF PROGRAM-----------------------")
        print(str(val))
        print("----------------------------------------------------------------")
        PC = PC + 1
    elif(OP_CODE == "READ"):
        ID = cuadruplo[1]
        val = input("")
        set_value(ID,SymbolTable, avail, val)
        #Look in symbol table 
        PC = PC +1
    else:
        # OPERATION
        print("OPERATION")
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
    print(avail)
    query = SymbolTable.lookup(ID)
    if(query is not None):
        print("UPDATING" + ID +" with " + str(res))
        SymbolTable.update(ID,res)
    else:
        #Look in avail
        T = avail.get(ID)
        avail[ID] = res

def parse_matrix(ID_MAT):
    print("Matrix a parsear")
    print(ID_MAT)
    LIST_MAT= ID_MAT.split("-")
    print(LIST_MAT)
    return LIST_MAT[0], LIST_MAT[1:]

def get_value(ID,SymbolTable,avail):
    print("LOOKING FOR " + str(ID))
    if(is_number(ID)):
        return float(ID)
    # Check if it starts with a  [
    if(ID[0]=="["):
        ID, stack_indexes= parse_matrix(ID[1:])
        starting_index = get_value(ID,SymbolTable,avail)
        print(starting_index)
        ele = array_lookup(stack_indexes=stack_indexes,starting_index=starting_index)
        
        return ele
    query = SymbolTable.lookup(ID)
    if(query is not None):
        print(query.print())
        if(query.tipo == "int" or query.tipo == "double"):
            return float(query.attributes)
        return query.attributes
    else:
        #Look in avail
        T = avail.get(ID)
        if(T is not None):
            return T
        else:
            print(ID)
            raise Exception(" not found get_value")