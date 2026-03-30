import numpy as np
import random
from variables import (
    board_size,
    barcos,
    symbol_agua,
    symbol_barco,
    symbol_disparo,
    symbol_fallo,
    orientations
)

class Tablero:
    def __init__(self, player_id: str):
        """Inicializa el tablero del jugador."""
        self.player_id = player_id
        self.size = board_size
        self.board = np.full((self.size, self.size), symbol_agua)
        self.tracking = np.full((self.size, self.size), symbol_agua)
        self.vidas = 0

    def colocar_barco(self, tipo_barco, fila, columna, orientacion):
        """
        Coloca un barco en la posición indicada con orientación N, S, E u O.
        Devuelve True si se colocó correctamente, False si no cabe o choca.
        """

        eslora = barcos[tipo_barco]["eslora"]

        # --- 1. Comprobar si cabe dentro del tablero ---
        if orientacion == "N":
            if fila - (eslora - 1) < 0:                   # Para Norte y Sur, la columna no cambia, por eso se comprueba
                return False                                # que la fila esté en el rango eslora - 1
        elif orientacion == "S":                            # En Este y Oeste, lo que se comprueba es que la columna,
            if fila + (eslora - 1) >= self.size:            # sea menor que la matriz (self.size)
                return False
        elif orientacion == "E":
            if columna + (eslora - 1) >= self.size:
                return False
        elif orientacion == "O":
            if columna - (eslora - 1) < 0:
                return False

        # --- 2. Comprobar que no pisa otro barco ---
        posiciones = []

        for i in range(eslora):
            if orientacion == "N":
                f, c = fila - i, columna         # Para N y S, la columna no cambia, solo la fila
            elif orientacion == "S":                # Para E y O, la fila no cambia, solo la columna
                f, c = fila + i, columna
            elif orientacion == "E":
                f, c = fila, columna + i
            elif orientacion == "O":
                f, c = fila, columna - i

            if self.board[f, c] == symbol_barco:
                return False

            posiciones.append((f, c)) # se guardan las posiciones si todas cumplen. Una vez guardadas, coloca el barco

        # --- 3. Colocar el barco ---
        for f, c in posiciones:
            self.board[f, c] = symbol_barco
            self.vidas += eslora
        
        # --- 4. Imprimir el tablero después de colocar ---
        print(self.board)


        return True
    
    def recibir_disparo(self, fila, columna):
        casilla = self.board[fila, columna]

        # --- 1. Ya disparado antes ---

        
    def realizar_disparo(self, fila, columna):
        casilla = self.tracking[fila, columna]

        # --- 1. Ya he disparado ahí ---

        if casilla == symbol_fallo or casilla == symbol_disparo:
            return "Ya he disparado ahí"

        # --- 2. Agua ---
        if casilla == symbol_agua:
            self.tracking[fila, columna] = symbol_fallo
            return "Agua"

         # --- 3. Barco tocado ---
        if casilla == symbol_barco:
            self.tracking[fila, columna] = symbol_disparo
            self.vidas -= 1   # restamos una vida del jugador que recibe el disparo
            return "Tocado"

  
