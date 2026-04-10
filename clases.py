import numpy as np
import random
from variables import (
    symbol_agua,
    symbol_fallo,
    symbol_barco,
    symbol_disparo,
    orientations,
    orientation_delta,
    board_size,
    barcos
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

        # --- 1. Comprobar si cabe dentro del tablero ---Para Norte y Sur, la columna no cambia, por eso se comprueba
        # que la fila esté en el rango eslora - 1, En Este y Oeste, lo que se comprueba es que la columna, sea menor que la matriz (self.size)
        if orientacion == "N":
            if fila - (eslora - 1) < 0: 
                print(f" No se puede colocar {tipo_barco}: se sale del tablero.")                  
                return False                                
        elif orientacion == "S":                          
            if fila + (eslora - 1) >= self.size: 
                print(f" No se puede colocar {tipo_barco}: se sale del tablero.")         
                return False
        elif orientacion == "E":
            if columna + (eslora - 1) >= self.size:
                print(f" No se puede colocar {tipo_barco}: se sale del tablero.")
                return False
        elif orientacion == "O":
            if columna - (eslora - 1) < 0:
                print(f" No se puede colocar {tipo_barco}: se sale del tablero.")
                return False

        # --- 2. Comprobar que no pisa otro barco --- Para N y S, solo cambia la fila y en E y O solo cambia la columna
        posiciones = []

        for i in range(eslora):
            if orientacion == "N":
                f, c = fila - i, columna         
            elif orientacion == "S":                
                f, c = fila + i, columna
            elif orientacion == "E":
                f, c = fila, columna + i
            elif orientacion == "O":
                f, c = fila, columna - i

             # Comprobar el área alrededor (3x3)

            for df in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nf, nc = f + df, c + dc

                    if 0 <= nf < self.size and 0 <= nc < self.size:
                        if self.board[nf, nc] == symbol_barco:
                            print(f" No se puede colocar {tipo_barco}: toca otro barco en ({nf}, {nc}).")
                            return False

            posiciones.append((f, c)) # se guardan las posiciones si todas cumplen. Una vez guardadas, coloca el barco

        # --- 3. Colocar el barco ---
        for f, c in posiciones:
            self.board[f, c] = symbol_barco
        self.vidas += eslora
        
        # --- 4. Imprimir el tablero después de colocar ---
        # print(self.board)

        return True
    
    def colocar_flota_aleatoria(self):
        
        for tipo, datos in barcos.items():
            eslora = datos["eslora"]
            cantidad = datos["cantidad"]

            for x in range(cantidad):
                colocado = False

                while not colocado:
                    fila = np.random.randint(0, self.size)
                    columna = np.random.randint(0, self.size)
                    orientacion = np.random.choice(orientations)

<<<<<<< Updated upstream
                colocado = self.colocar_barco(tipo, fila, columna, orientacion)
=======
                    colocado = self.colocar_barco(tipo, fila, columna, orientacion)
>>>>>>> Stashed changes

    
    
    def recibir_disparo(self, fila, columna):
    
        casilla = self.board[fila, columna]

    # --- 1. Ya disparado antes ---

        if casilla == symbol_fallo or casilla == symbol_disparo:
            return "Ya has disparado aquí"

    # --- 2. Agua ---
        if casilla == symbol_agua:
            self.board[fila, columna] = symbol_fallo
            return "Agua"

    # --- 3. Barco tocado ---
        if casilla == symbol_barco:
            self.board[fila, columna] = symbol_disparo
            self.vidas -= 1   # restamos una vida

        # Comprobamos si ha hundido el barco, o solo lo ha tocado:
        if self.barco_hundido(fila, columna):
            return "Hundido"
        else:
            return "Tocado"
        
    def barco_hundido(self, fila, columna):
        """
        Comprueba si el barco al que pertenece esta casilla está completamente hundido.
        Busca en las 4 direcciones hasta que encuentre agua o el borde.
        Si encuentra alguna parte del barco sin disparar, NO está hundido.
        """

        # Direcciones: arriba, abajo, derecha, izquierda
        direcciones = [(-1,0), (1,0), (0,1), (0,-1)]

        for df, dc in direcciones:
            f, c = fila + df, columna + dc

            while 0 <= f < self.size and 0 <= c < self.size:
                if self.board[f, c] == symbol_barco:
                    return False  # queda parte sin tocar

                if self.board[f, c] == symbol_agua or self.board[f, c] == symbol_fallo:
                    break  # ya no es parte del barco

                f += df
                c += dc

        print("Tocado y hundido")
<<<<<<< Updated upstream
        True
=======
        return True
>>>>>>> Stashed changes

