import numpy as np
import random

cartas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
tableroCartas = np.zeros((6, 6))
tableroJuego = []


#Inicializa el tablero de juego y el auxiliar
def iniciarTablero(tableroCartas):
    random.shuffle(cartas)
    for i in range(6):
        for j in range(6):
            carta = cartas.pop()
            tableroCartas[i][j] = carta
    #print(tableroCartas)
    for i in range(6):
        tableroJuego.append(['*','*','*','*','*','*'])
        #print(['*','*','*','*','*','*'])

#Imprimir el tablero de juego
def printTablero(tablero):
    print('    0 '+ ' 1 ' + ' 2 ' + ' 3 ' + ' 4 ' + ' 5 ')
    for i in range(6):
        print(' ' + str(i), end=' ')
        for j in range(6):
            print(' '+ tablero[i][j],end=' ')
        print('\n')
        

def mainJuego(tableroJuego,tableroCartas):
    
    print("Bienvenido al juego")
    puntajeJugador1 = 0
    puntajeJugador2 = 0
    puntajeTotal=0
    
    while(puntajeTotal<18 or salida!=0):
    
        salida = input("Quieres seguir jugando (0 para salir) ?")
        print(salida)
        puntajeTotal = puntajeJugador1+puntajeJugador2
#main
iniciarTablero(tableroCartas)
printTablero(tableroJuego)
mainJuego(tableroJuego,tableroCartas)
