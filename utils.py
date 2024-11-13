import numpy as np
import random
import time

def crear_tablero(tamaño):
    return np.full((tamaño, tamaño), "_")

def crear_barco(eslora):
    casilla_0 = (random.randint(0, 9), random.randint(0, 9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0] + 1, casilla[1])
        else:
            casilla = (casilla[0], casilla[1] + 1)
        barco.append(casilla)

    return barco

def colocacion_valida(barco, tablero):
    for casilla in barco:
        if casilla[0] > 9 or casilla[1] > 9 or tablero[casilla] != "_":
            return False
    return True

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(tablero_oculto, tablero_real):
    x = int(input("¿A qué fila disparas? (0-9): "))
    y = int(input("¿A qué columna disparas? (0-9): "))

    casilla = (x, y)

    if tablero_real[casilla] == "O":
        print("¡Tocado!")
        tablero_oculto[casilla] = "X"
        tablero_real[casilla] = "X"
    elif tablero_oculto[casilla] not in ["X", "A"]:
        print("¡Agua!")
        tablero_oculto[casilla] = "A"

    return tablero_oculto, tablero_real

def disparar_maquina(tablero_jugador):
    x, y = random.randint(0, 9), random.randint(0, 9)
    casilla = (x, y)

    print(f"La máquina dispara a la casilla {casilla}")

    if tablero_jugador[casilla] == "O":
        print("¡La máquina tocó un barco!")
        tablero_jugador[casilla] = "X"
    elif tablero_jugador[casilla] not in ["X", "A"]:
        print("¡La máquina falló!")
        tablero_jugador[casilla] = "A"

    return tablero_jugador

def verificar_victoria(tablero):
    """Verifica si quedan barcos en el tablero."""
    return not np.any(tablero == "O")

def colocar_barcos(tablero):
    dict_barcos = {}
    esloras = [2, 2, 2, 3, 3, 4]

    for i, eslora in enumerate(esloras):
        barco = crear_barco(eslora)
        while not colocacion_valida(barco, tablero):
            barco = crear_barco(eslora)

        dict_barcos[f'b{i + 1}'] = barco
        colocar_barco(barco, tablero)

    return dict_barcos, tablero

def iniciar_partida():
    
    tablero_jugador = crear_tablero(10)
    tablero_maquina_real = crear_tablero(10)
    tablero_maquina_oculto = crear_tablero(10)

    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina_real)

    turnos(tablero_jugador, tablero_maquina_real, tablero_maquina_oculto)

def turnos(tablero_jugador, tablero_maquina_real, tablero_maquina_oculto):
    turno = input("¿Quién tiene el primer turno? J (jugador) o M (máquina): ").lower()

    while not verificar_victoria(tablero_jugador) and not verificar_victoria(tablero_maquina_real):
        if turno == "j":
            print("\n=== Tu turno ===")
            print("\nTu tablero:")
            print(tablero_jugador)
            print("\nTablero de la máquina (disparos):")
            print(tablero_maquina_oculto)

            tablero_maquina_oculto, tablero_maquina_real = disparar(tablero_maquina_oculto, tablero_maquina_real)

            if verificar_victoria(tablero_maquina_real):
                print("\n¡Felicidades, has ganado! ¡Todos los barcos de la máquina han sido hundidos!")
                return

            turno = "m"

        elif turno == "m":
            print("\n=== Turno de la máquina ===")
            time.sleep(2)
            tablero_jugador = disparar_maquina(tablero_jugador)

            print("\nTu tablero actualizado:")
            print(tablero_jugador)

            if verificar_victoria(tablero_jugador):
                print("\n¡La máquina gana! ¡Todos tus barcos han sido hundidos!")
                return

            turno = "j"

        else:
            print("Turno inválido, por favor ingresa 'J' o 'M'.")
            turno = input("¿Quién tiene el primer turno? J (jugador) o M (máquina): ").lower()

    print("\n¡Fin del juego!")
