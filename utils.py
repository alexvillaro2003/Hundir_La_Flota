import numpy as np
import random
import time

def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero


def crear_barco(eslora):
    casilla_0 = (random.randint(0,9), random.randint(0,9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal

    return barco

def colocacion_valida(barco, tablero):
    for casilla in barco:
        if casilla[0] > 9 or casilla[1] > 9:
            return False
        
        if tablero[casilla] != "_":
            return False
    return True

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(tablero):

    x = int((input("¿A qué fila disparas?")))
    y = int((input("¿A qué columna disparas?")))

    casilla = (x,y)

    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero

def disparar_maquina(tablero):

    x = random.randint(0,9)
    y = random.randint(0,9)

    casilla = (x,y)

    if [casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero

def turnos(tablero_jugador, tablero_maquina):

    turno = (input("¿Quién tiene el primer turno? J(jugador) o M(máquina)?")).lower()

    while not verificar_victoria(tablero_jugador) and not verificar_victoria(tablero_maquina):
        if turno == "j":
            print("Dispara el jugador...")
            tablero_jugador = disparar(tablero_jugador)

            if verificar_victoria(tablero_maquina):
                    return "¡El jugador gana!"
            
            turno = "m"

            return tablero_maquina

        elif turno == "m":
            print("Dispara la máquina...")
            
            time.sleep(2)

            tablero_maquina = disparar_maquina(tablero_maquina)

            if verificar_victoria(tablero_jugador):
                    return "La máquina gana"

            time.sleep(2)
            
            turno = "j"

            return print(tablero_jugador)

        else:
            print("Turno inválido")
            return turnos(tablero_jugador, tablero_maquina)

def verificar_victoria(tablero):
    return not np.any(tablero == "O")

def colocar_barcos(tablero):
    dict_barcos = {}
    esloras = [2, 2, 2, 3, 3, 4]  
    
    for i, eslora in enumerate(esloras):
        barco = crear_barco(eslora)
        while not colocacion_valida(barco, tablero):
            barco = crear_barco(eslora)  
        
        dict_barcos[f'b{i+1}'] = barco  
        colocar_barco(barco, tablero) 
    
    return dict_barcos, tablero

def iniciar_partida():
    
    tablero_jugador = crear_tablero(10)
    tablero_maquina = crear_tablero(10)

    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    print("TABLERO JUGADOR:")
    
    
    print(tablero_jugador)
    
    print("************************************************")
    
    time.sleep(2)
    
    print("TABLERO MÁQUINA:")

    time.sleep(2)
    
    print(tablero_maquina)

    

    turnos(tablero_jugador, tablero_maquina)

