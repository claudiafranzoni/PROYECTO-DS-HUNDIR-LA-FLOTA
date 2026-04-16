import variables as var
from clases import Tablero
import funciones as fun

def jugar(): # 1) Bienvenida e instrucciones del juego
    print(var.msg_bienvenida)
    print(var.msg_instrucciones)

    # 2) Inicialización de tableros con la variable board_size y clase Tablero
    tablero_jugador = Tablero(player_id = "Jugador")
    tablero_maquina = Tablero(player_id = "Maquina")

    # Colocación automática de la flota
    tablero_jugador.colocar_flota_aleatoria()
    tablero_maquina.colocar_flota_aleatoria()

    disparos_maquina = set() # Set con las coordenadas ya usadas, para que no se puedan repetir

    # 3) Bucle principal
    while not fun.hay_ganador(tablero_jugador, tablero_maquina):
                
        # --- TURNO JUGADOR ---
        fun.imprimir_tableros(tablero_jugador, tablero_maquina)
        while fun.turno_jugador(tablero_maquina):
            fun.imprimir_tableros(tablero_jugador, tablero_maquina)
        if fun.hay_ganador(tablero_jugador, tablero_maquina):
            break

        # --- TURNO MÁQUINA ---
        while fun.turno_maquina(tablero_jugador, disparos_maquina):
            fun.imprimir_tableros(tablero_jugador, tablero_maquina)
        if fun.hay_ganador(tablero_jugador, tablero_maquina):
            break
   

if __name__ == "__main__": # Activar el juego solo con el "run"
    jugar()