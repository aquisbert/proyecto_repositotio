
#este es un juego creado a base de matrices.
import random

def reconocerLineasOblicuas(matriz):
    gano = False
    cont = 0
    for fc in range(len(matriz)):
        elem = matriz[0][0]
        if (elem != '.') and (elem == matriz[fc][fc]):
            cont+=1 
        if cont == len(matriz):
            gano = True
            for fc in range(len(matriz)):
                matriz[fc][fc] = " \ "
    cont = 0
    c = len(matriz)-1
    elem = matriz[0][len(matriz)-1]
    for f in range(len(matriz)):
        if (elem != '.') and (elem == matriz[f][c]):
            cont+=1
            c-=1
        if cont == len(matriz):
            gano = True
            c = len(matriz)-1
            for f in range(len(matriz)):
                matriz[f][c] = ' / '
                c-=1
    return gano



def reconocerLineasVerticales(matriz):
    gano = False
    cont = 0
    for c in range(len(matriz)):
        elem = matriz[0][c]
        if (elem != '.') and (gano != True):
            for f in range(len(matriz)):
                if elem == matriz[f][c]:
                    cont +=1
            if cont == len(matriz):
                for f in range(len(matriz)):
                    matriz[f][c] = '|'
                gano = True
        cont = 0
    return gano 



def reconocerLineasHorizontales(matriz):
    gano = False
    cont = 0
    for f in range(len(matriz)):
        elem = matriz[f][0]
        if (elem != '.') and (gano != True):
            for c in range(len(matriz)):
                if elem == matriz[f][c]:
                    cont +=1
            if cont == len(matriz):
                for c in range(len(matriz)):
                    matriz[f][c] = '-'
                gano = True
        cont = 0
    return gano
            



def rellenarCasillas(fila, columna, matriz, turnos):
    
    if matriz[fila-1][columna-1] == '.':
        if turnos:
            matriz[fila-1][columna-1] = 'X'
        
        else:
            matriz[fila-1][columna-1] = 'O'
    else:
        if turnos:
            
            while matriz[fila-1][columna-1] != '.' :
                print('este casillero ya esta ocupado.') 
                print()
                fila = int (input('ingrese la posicion de una fila: '))
                columna = int (input('ingrese la posicion de una columna: '))
            matriz[fila-1][columna-1] = 'X'
        else:
            while  matriz[fila-1][columna-1] != '.':
                fila = random.randint(0, len(matriz)-1)
                columna = random.randint(0,len(matriz)-1)
            matriz[fila-1][columna-1] = 'O'

def matrizVacia(matriz):
    vacio = False
    gano = False
    for f in matriz:
        for c in f:
            if c == '.':
                vacio = True
    if reconocerLineasHorizontales(matriz):
        gano = True
        vacio = False
    elif reconocerLineasVerticales(matriz):
        gano = True
        vacio = False
    elif reconocerLineasOblicuas(matriz):
        gano = True
        vacio = False
    return vacio,gano


def crearMatriz():
    matriz = []
    for f in  range(3):
        matriz.append([])
        for c in range(3):
            matriz[f].append('.')
    return matriz

def imprimirMatriz(matriz):
    for f in matriz:
        for c in f:
            print(c, end='  ')
        print()
        

#prog principal
matriz = crearMatriz()
turnos = True
vacia, gano = matrizVacia(matriz)
while vacia:
    if turnos:
        fila = int(input('ingrese la posicion de una fila: '))
        columna = int(input('ingrese la posicion de una columna: '))
        if (fila <= len(matriz)) and (columna <= len(matriz)):
            print()
            rellenarCasillas(fila, columna, matriz, turnos)
            
            

        else:
            while (fila > len(matriz)) and (columna > len(matriz)):
                print('la posicion ingresada excede las posiciones disponibles')
                fila = int(input('ingrese la posicion de una fila: '))
                columna = int(input('ingrese la posicion de una columna: '))
                print()
            rellenarCasillas(fila, columna, matriz, turnos)
        vacia, gano = matrizVacia(matriz)
        if vacia == False:
            print('EL JUEGO TERMINO')

        turnos = False

    else:
        fila = random.randint(0,len(matriz)-1)
        columna = random.randint(0,len(matriz)-1)
        rellenarCasillas(fila, columna, matriz, turnos)
        vacia, gano = matrizVacia(matriz)
        if vacia == False:
            print('EL JUEGO TERMINO')
        
        turnos = True
    imprimirMatriz(matriz)
    print()
    print('------------')
    

if (gano == True) and (turnos == True): 
    print('PERDISTE !!')
elif (gano == True) and (turnos == False):
    print('GANASTE !!')
else:
    print(' EMPATE !! ')