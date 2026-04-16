import numpy as np
import random
from variables import (
    board_size,
    symbol_agua,
    symbol_barco,
    symbol_disparo,
    symbol_fallo,
    label_my_board,
    label_enemy_board,
    msg_tu_turno,
    msg_maquina_turno, 
    msg_impacto,
    msg_agua,
    msg_maquina_hit,
    msg_maquina_miss,
    msg_ya_disparado,
    msg_coord_invalida,
    msg_ganas,
    msg_pierdes
)
 
 
# ── Visualización ─────────────────────────────────────────────
 
def imprimir_tableros(tablero_jugador, tablero_maquina):
    """
    Imprime lado a lado el tablero propio y el tablero de seguimiento
    (disparos realizados sobre la máquina), ocultando los barcos enemigos.
    """
    # "  " = 1 char índice fila + 1 espacio separador
    cols = " ".join(str(i) for i in range(board_size))
    ancho_tablero = 2 * board_size - 1  # cada celda ocupa 1 char + 1 espacio, menos el último
 
    separador = "    "  # espacio entre los dos tableros
 
    print(f"\n  {label_my_board:<{ancho_tablero + 2}}{separador}  {label_enemy_board}")
    print(f"  {cols}{separador}  {cols}")
 
    for fila in range(board_size):
        fila_propia  = " ".join(tablero_jugador.board[fila])
        fila_enemiga = " ".join(tablero_maquina.tracking[fila])
        print(f"{fila} {fila_propia}{separador}{fila} {fila_enemiga}")
 
    print()
 
# ── Entrada del jugador ───────────────────────────────────────
 
def pedir_coordenadas():
    """
    Pide al jugador coordenadas (fila columna) y las valida.
    Devuelve (fila, columna) como enteros, o None si son inválidas.
   """
    entrada = input().strip().split() # Las coordenadas se introducen separadas por espacio, ej. "6 7"
 
    if len(entrada) != 2:
        print(msg_coord_invalida)
        return None
 
    try:
        fila, columna = int(entrada[0]), int(entrada[1])
    except ValueError:
        print(msg_coord_invalida)
        return None
 
    if not (0 <= fila < board_size and 0 <= columna < board_size):
        print(msg_coord_invalida)
        return None
 
    return fila, columna
 
 
# ── Turno del jugador ─────────────────────────────────────────
 
def turno_jugador(tablero_maquina):
    """
    Gestiona el turno completo del jugador.
    Devuelve True si acierta (le vuelve a tocar), False si falla.
    """
    print(msg_tu_turno)
    coords = pedir_coordenadas()
    if coords is None:
        return True  # coordenadas inválidas → repetir turno sin penalizar
 
    fila, columna = coords
    resultado = tablero_maquina.recibir_disparo(fila, columna)
 
    if resultado == "Ya has disparado aquí":
        print(msg_ya_disparado)
        return True  # repetir turno
 
    # Actualizar el tablero de seguimiento del jugador
    if resultado == "Agua":
        tablero_maquina.tracking[fila, columna] = symbol_fallo
        print(msg_agua)
        return False
 
    # Tocado o hundido
    tablero_maquina.tracking[fila, columna] = symbol_disparo
    print(msg_impacto)
    if resultado == "Hundido":
        print("  ⚓ ¡Barco hundido!")
        revelar_alrededor_hundido(tablero_maquina, fila, columna)
    return True  # acertó → le vuelve a tocar
 
 
# ── Turno de la máquina ───────────────────────────────────────
 
def turno_maquina(tablero_jugador, disparos_maquina):
    """
    La máquina dispara a una posición aleatoria no repetida del tablero del jugador.
    Devuelve True si acierta (le vuelve a tocar), False si falla.
    disparos_maquina: conjunto (set) con las coordenadas ya usadas.
    """
    print(msg_maquina_turno)
    while True:
        fila    = random.randint(0, board_size - 1)
        columna = random.randint(0, board_size - 1)
        if (fila, columna) not in disparos_maquina:
            break
 
    disparos_maquina.add((fila, columna))
    resultado = tablero_jugador.recibir_disparo(fila, columna)
 
    if resultado in ("Tocado", "Hundido"):
        print(msg_maquina_hit.format(fila, columna))
        if resultado == "Hundido":
            print("  ⚓ ¡La máquina ha hundido uno de tus barcos!")
            revelar_alrededor_hundido(tablero_jugador, fila, columna)
        return True   # acierta → repite
 
    print(msg_maquina_miss.format(fila, columna))
    return False
 
 
# ── Comprobación de victoria ──────────────────────────────────
 
def hay_ganador(tablero_jugador, tablero_maquina):
    """
    Devuelve 'jugador' si la máquina no tiene vidas,
    'maquina' si el jugador no tiene vidas, o None si el juego continúa.
    """
    if tablero_maquina.vidas <= 0:
        print(msg_ganas)
        return "jugador"
    if tablero_jugador.vidas <= 0:
        print(msg_pierdes)
        return "maquina"
    return None

def revelar_alrededor_hundido(tablero_maquina, fila, columna):
    """
    Cuando se hunde un barco, marca como fallo (*) todas las casillas
    de agua alrededor del barco en el tablero de seguimiento.
    """
    direcciones = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    celdas_barco = set()

    # 1. Reconstruir todas las celdas del barco hundido
    celdas_barco.add((fila, columna))

    for df, dc in direcciones:
        f, c = fila + df, columna + dc
        while 0 <= f < board_size and 0 <= c < board_size:
            if tablero_maquina.board[f, c] == symbol_disparo:
                celdas_barco.add((f, c))
                f += df
                c += dc
            else:
                break

    # 2. Revelar el perímetro alrededor de todas esas celdas
    for bf, bc in celdas_barco:
        for df in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nf, nc = bf + df, bc + dc
                if 0 <= nf < board_size and 0 <= nc < board_size:
                    if tablero_maquina.tracking[nf, nc] == symbol_agua:
                        tablero_maquina.tracking[nf, nc] = symbol_fallo
                        