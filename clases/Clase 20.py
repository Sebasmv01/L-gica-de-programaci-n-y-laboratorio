# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:07:54 2020

@author: berserk
"""

import numpy as np

def displayInicialTriqui():
    for i in range(0,3):
        for j in range(0,3):
            print("|_",end="")
        print("|")

def displayTriqui(matriz):
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i,j]==1:
                print("|X", end="")
            else:
                if matriz[i,j]==10:
                    print("|O",end="")

                else:
                    print("|_",end="")
        print("|") #PIPELINE

        
def estadoDelJuego(matriz)->int:
    #devuelve 1 si gana la X
    if 3 in np.sum(matriz, axis=0) or 3 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==3 or np.sum(np.diagonal(np.fliplr(matriz)))==3:
        salida = 1
    else:
        #devuelve 2 si gana la Y
       if 30 in np.sum(matriz, axis=0) or 30 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==30 or np.sum(np.diagonal(np.fliplr(matriz)))==30:
        salida = 2
       else:
            #devuelve 3 si no hay ganador
            if np.sum(matriz)==45 or np.sum(matriz)==54:
                salida = 3
            else:
                #devuelve 4 si el juego no ha terminado
                salida = 4
    return salida
    
def jugarTriqui():
    turno=True
    displayInicialTriqui()
    matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
    estado=4
    while(estado==4): # iterador provisional
        tupla= tuple(input("Ingrese la casilla a jugar, ej: la casilla superior derecha es 1,3: "))
        x=int(tupla[0])-1 #lavado (modificar que el numero quede entre 0 y 2 por rango)
        y=int(tupla[2])-1
        if x>=0 and x<=2 and y>=0 and y<=2:
            if matriz[x,y]==0:
                if turno:
                    matriz[x,y]=1 #numpay registra como juego de la X
                else:
                    matriz[x,y]=10 #numpay registra como juego del O
                estado = estadoDelJuego(matriz)
                displayTriqui(matriz)
                turno=not(turno)
            else:
                print ("La casilla ya esta ocupada")
        else:
            print ('Movimiento no aprobado, debe ser de 3x3.')
    if estado == 1:
        print("El jugador X ha ganado!")
    else:
        if estado == 2:
            print ("El jugador O ha ganado!")
        else:
            print ("Nadie Ha Ganado, es un Empate")
            