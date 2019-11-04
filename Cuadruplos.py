def cuadruplo(pila_operandos,contador,operator):
    op_1 = pila_operandos.pop()
    op_2 = pila_operandos.pop()
    res = 'T_' + str(contador)
    if(operator=='*'):
        print('* ' + str(op_1+ ' ') + str(op_2+ ' ') + str(res))
        pila_operandos.append(res)
        contador=contador+1
    elif(operator=='/'):
        print('/ ' + str(op_1+ ' ') + str(op_2+ ' ') + str(res))
        pila_operandos.append(res)
        contador=contador+1
    else:
        print("Unknown operator")
    
    return contador, pila_operandos
