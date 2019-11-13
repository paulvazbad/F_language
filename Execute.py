#from compile_run import is_number,is_array,get_value

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
	except TypeError:
		return False
        
##definicion de la funcion execute
def execute(SymbolTable,cuadruplos,list_arrays):
    avail = {}
    print("--------------------- EXECUTION----------------------")
    OP_CODE = ""
    PC = 0
    OP_CODE =   cuadruplos[PC][0]
    call_stack = []
    while(OP_CODE is not "END"):
        OP_CODE = cuadruplos[PC][0]
        print(PC)
        PC  = process_command(SymbolTable,list_arrays,cuadruplos[PC], avail,call_stack,PC)
        
    SymbolTable.print()
    print(avail)

def process_command(SymbolTable,list_arrays,cuadruplo, avail,call_stack,PC):
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
        process_command_expression(SymbolTable,list_arrays,cuadruplo, avail,call_stack,PC)
        #Increment PC
        PC = PC + 1
    return PC


def process_command_expression(SymbolTable,list_arrays,cuadruplo, avail,call_stack,PC):
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


def get_value(ID,SymbolTable,avail):
    print("LOOKING FOR " + str(ID))
    if(is_number(ID)):
        return float(ID)
    # Check if it starts with a  [
    if(ID[0]=="["):
        print("ES MATRIX")
        return 11111
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