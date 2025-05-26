'''#Creacion de tablero Opcion 2, intento de ingresar GATO Y RATON

filas = 5  #Defino filas
columnas = 5 #defino 5 columnas
tablero = [[" " for _ in range(columnas)] for _ in range(filas)] #Aqui puedo crear el tablero


#Pruebo crear posiciones para el gato y el raton 
posicion_gato = (1,1)
posicion_raton = (3,3)

#Con esto procuro que se pueda imprimir en filas
for filas in tablero:
    if posicion_gato in tablero:
        print ('G')
    elif posicion_raton in tablero:
        print ('R')
    else:
        print(' '. join(filas)) #con esto logro unir las filas'''



#Opcion Simple

tablero = [
    [' . ', ' . ', ' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ', ' . ', ' . ']
]  #Creo una lista anidada que servira como tablero. Esta lista tendra indices, el primer indice me sirve para acceder a la fina y el segundo 
#columna

'''#Para poder visualizar en la tarminal creo 
print(tablero[0])
print(tablero[1])
print(tablero[2])
print(tablero[3])
print(tablero[4])'''

'''#Busco una opcion adicional para imprimir. 
for fila in tablero:    #Asi logro imprimir de manera mas sencilla, recorre cada fila y la imprima
    print (fila)'''




'''
#Voy a convertir mi tablero inicial en Funcion para que pueda ser reimpreso y reescrito, asi por ejemplo la g pueda cambiar de posicion.
def creacion_tablero ():  #Aqui se crea un tablero en blanco nuevamente
    
    tablero = [
        [' . ', ' . ', ' . ', ' . ', ' . '],
        [' . ', ' . ', ' . ', ' . ', ' . '],
        [' . ', ' . ', ' . ', ' . ', ' . '],
        [' . ', ' . ', ' . ', ' . ', ' . '],
        [' . ', ' . ', ' . ', ' . ', ' . ']
    ]
    return tablero #Aqui hago que me entrege el tablero nuevo creado

#Defino la posicion del Raton y del Gato

tablero[0][0] = 'g'  #Agrego al gato en la esquina superior
tablero[4][4] = 'r' #Agrego al raton en la esquina inferior


#Busco una opcion adicional para imprimir. 
for fila in tablero:    #Asi logro imprimir de manera mas sencilla, recorre cada fila y la imprima
    print (fila)


#Meto aqui la funcion que crea el tablero desde CERO, asi se puede reescribir la popsicion anterior
creacion_tablero()


#Trato de hacer que el usuario pueda hacer que se muevan 

fila = int(input('ingrese la fila en la que quiere que el gato se mueva'))  #Creo una variable donde voy a almacenar la fila
columna = int(input('ingrese el numero de columna donde quiere que el gato se mueva')) #Creo otra variables donde voy a almacenar la columna

tablero[fila][columna] = 'g' #Aqui logro actualizar la posicion del gato al actualizar el tablero

for fila in tablero:    #Asi logro imprimir de manera mas sencilla, recorre cada fila y la imprima
    print (fila)
'''


'''
cantidad_columnas = 5
cantidad_filas = 5

def jugar ():
    
    fila_gato = 0  #asigno valor a estas variables
    columna_gato = 0 #Defino los parametros iniciales
    fila_raton = 4
    columna_raton = 4
    for _ in range(8): #que se haga 5 veces

        print('=================') #Para poder verlos de manera separada

        tablero = [[' . ' for _ in range(cantidad_columnas)] for _ in range(cantidad_filas)]

        #hago que el usuario mueva al gato
        eleccion_de_movimiento_para_gato = input(' w, s, d, a')   #En esta variable se almacena el movimiento que quiere ejecutar el jugador
        
        #Creo un condicional en base a la eleccion del usuario
        if eleccion_de_movimiento_para_gato == 'w':  #Si el movimiento que elige el usuario es para arriba
            fila_gato = fila_gato - 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
            tablero[fila_gato][columna_gato] = ' g ' #Solo cambia la fila


        elif eleccion_de_movimiento_para_gato == 's':  #Si el movimiento que elige el usuario es para abajo
            fila_gato = fila_gato + 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
            tablero[fila_gato][columna_gato]  = ' g ' #Solo cambia la fila

        
        elif eleccion_de_movimiento_para_gato == 'd':  #Si el usurio elige ir a la derecha
            columna_gato = columna_gato + 1
            tablero[fila_gato][columna_gato] = ' g '

        
        elif eleccion_de_movimiento_para_gato == 'a': #Si el usuario elige ir a la izquierda
            columna_gato = columna_gato -1
            tablero[fila_gato][columna_gato] = ' g '

        
        posicion_inicial_raton = tablero[fila_raton][columna_raton] = ' r '

        for i in tablero:
            print(' '.join(i)) #Esto es solo una impresion

jugar()
'''

'''
#Ahora toca que yo pueda tambien mover al raton en turnos
cantidad_columnas = 5
cantidad_filas = 5
fila_gato = 0  #asigno valor a estas variables
columna_gato = 0 #Defino los parametros iniciales
fila_raton = 4
columna_raton = 4
for _ in range(8): #que se haga 5 veces

    print('==================') #Para poder verlos de manera separada

    tablero = [[' . ' for _ in range(cantidad_columnas)] for _ in range(cantidad_filas)]

    #hago que el usuario mueva al gato
    eleccion_de_movimiento_para_gato = input('Turno del gato w, s, d, a')   #En esta variable se almacena el movimiento que quiere ejecutar el jugador
    
    #Creo un condicional en base a la eleccion del usuario
    if eleccion_de_movimiento_para_gato == 'w':  #Si el movimiento que elige el usuario es para arriba
        fila_gato = fila_gato - 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
        tablero[fila_gato][columna_gato] = ' g ' #Solo cambia la fila


    elif eleccion_de_movimiento_para_gato == 's':  #Si el movimiento que elige el usuario es para abajo
        fila_gato = fila_gato + 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
        tablero[fila_gato][columna_gato]  = ' g ' #Solo cambia la fila

    
    elif eleccion_de_movimiento_para_gato == 'd':  #Si el usurio elige ir a la derecha
        columna_gato = columna_gato + 1
        tablero[fila_gato][columna_gato] = ' g '

    
    elif eleccion_de_movimiento_para_gato == 'a': #Si el usuario elige ir a la izquierda
        columna_gato = columna_gato -1
        tablero[fila_gato][columna_gato] = ' g '

    else: #caso en el cual no se agrego una letra valida
        print('elija una opcion valida')

    
    #Movimiento del raton
    eleccion_de_movimiento_para_raton = input(' Turno del raton w, s, d, a')  #Crear una variable para que se guarde la eleccion del usuario    
    
    #Condicionales de acuerdo a la eleccion
    if eleccion_de_movimiento_para_raton == 'w':
        fila_raton = fila_raton - 1  #Para que se pueda modificar la posicion inicial le resto la fila
        tablero[fila_raton][columna_raton] = ' r '
    
    elif eleccion_de_movimiento_para_raton == 's':
        fila_raton = fila_raton + 1  #Se le suma 1 para que se mueva hacia abajo en la fila
        tablero[fila_raton][columna_raton] = ' r '

    elif eleccion_de_movimiento_para_raton == 'd':
        columna_raton = columna_raton + 1
        tablero[fila_raton][columna_raton] = ' r '

    elif eleccion_de_movimiento_para_raton == 'a':
        columna_raton = columna_raton - 1 
        tablero[fila_raton][columna_raton] = ' r '

    else: #Cuando no se selecciono una opcion valida
        print('elija una opcion valida')
    

    for i in tablero:
        print(' '.join(i)) #Esto es solo una impresion 
'''


#Ahora hay que determinar un ganador
cantidad_columnas = 5
cantidad_filas = 5
fila_gato = 0  #asigno valor a estas variables
columna_gato = 0 #Defino los parametros iniciales
fila_raton = 4
columna_raton = 4

#Tablero de inicio
tablero = [[' . ' for _ in range(cantidad_columnas)] for _ in range(cantidad_filas)]

posicion_gato = tablero[fila_gato][columna_gato]
tablero[fila_gato][columna_gato]= ' g '

posicion_raton = tablero[fila_raton][columna_raton]
tablero[fila_raton][columna_raton] = ' r '

for i in tablero:
    print(' '.join(i))

for turnos in range(10): #que se haga 5 veces

    print('==================') #Para poder verlos de manera separada

    tablero = [[' . ' for _ in range(cantidad_columnas)] for _ in range(cantidad_filas)]

    #hago que el usuario mueva al gato
    eleccion_de_movimiento_para_gato = input('Movimiento Gato  w, s, d, a: ')   #En esta variable se almacena el movimiento que quiere ejecutar el jugador
    
    #Creo un condicional en base a la eleccion del usuario
    if eleccion_de_movimiento_para_gato == 'w':  #Si el movimiento que elige el usuario es para arriba
        fila_gato = fila_gato - 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
        posicion_gato = tablero[fila_gato][columna_gato] #Para que se guarde en esta variable las coordenadas de la posicion 
        tablero[fila_gato][columna_gato] = ' g '

    elif eleccion_de_movimiento_para_gato == 's':  #Si el movimiento que elige el usuario es para abajo
        fila_gato = fila_gato + 1 #Esto para ver si soluciona el hecho que no se actualiza la posicion
        posicion_gato = tablero[fila_gato][columna_gato] 
        tablero[fila_gato][columna_gato] = ' g '
    
    elif eleccion_de_movimiento_para_gato == 'd':  #Si el usurio elige ir a la derecha
        columna_gato = columna_gato + 1
        posicion_gato = tablero[fila_gato][columna_gato]
        tablero[fila_gato][columna_gato] = ' g '

    
    elif eleccion_de_movimiento_para_gato == 'a': #Si el usuario elige ir a la izquierda
        columna_gato = columna_gato -1
        posicion_gato = tablero[fila_gato][columna_gato]
        tablero[fila_gato][columna_gato] = ' g '
    else: #caso en el cual no se agrego una letra valida
        print('elija una opcion valida')


    #Esto me ayuda a finalizar el juego
    if posicion_gato == posicion_raton:
        print('Gano el gato')
        break                            #Rompe el for de arriba
    if turnos == 10:                     #LA variable turnos esta relacionado con el for de arriba
        print('Gano el raton')
    

    #Movimiento del raton
    eleccion_de_movimiento_para_raton = input('Movimiento del raton w, s, d, a:  ')  #Crear una variable para que se guarde la eleccion del usuario    
    
    #Condicionales de acuerdo a la eleccion
    if eleccion_de_movimiento_para_raton == 'w':
        fila_raton = fila_raton - 1  #Para que se pueda modificar la posicion inicial le resto la fila
        posicion_raton = tablero[fila_raton][columna_raton]  #Separo esto para que al final se puedan comparar posiciones
        tablero[fila_raton][columna_raton] = ' r ' #Aqui para que realmente imprima la r
    
    elif eleccion_de_movimiento_para_raton == 's':
        fila_raton = fila_raton + 1  #Se le suma 1 para que se mueva hacia abajo en la fila
        posicion_raton = tablero[fila_raton][columna_raton] 
        tablero[fila_raton][columna_raton] = ' r '

    elif eleccion_de_movimiento_para_raton == 'd':
        columna_raton = columna_raton + 1
        posicion_raton = tablero[fila_raton][columna_raton]
        tablero[fila_raton][columna_raton] = ' r '

    elif eleccion_de_movimiento_para_raton == 'a':
        columna_raton = columna_raton - 1 
        posicion_raton = tablero[fila_raton][columna_raton]
        tablero[fila_raton][columna_raton] = ' r '

    else: #Cuando no se selecciono una opcion valida
        print('elija una opcion valida')
    
    
    for i in tablero:
        print(' '.join(i)) #Esto es solo una impresion al final del turno del raton

    #Esto me ayuda a finalizar el juego
    if posicion_gato == posicion_raton:
        print('Gano el gato')
        break   #rompe el for de arriba
    if turnos == 10:   #Los turnos del for
        print('Gano el raton')
    
