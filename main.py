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
    while tablero_jugador.vidas > 0 and tablero_maquina.vidas > 0:
        
        # Mostramos los tableros
        fun.imprimir_tableros(tablero_jugador, tablero_maquina)
        
        # --- TURNO JUGADOR ---
        print(var.msg_tu_turno)
        repite_jugador = True
        while repite_jugador and tablero_maquina.vidas > 0:
            repite_jugador = fun.turno_jugador(tablero_maquina)
            if tablero_maquina.vidas == 0: break

        # --- TURNO MÁQUINA ---
        if tablero_maquina.vidas > 0:
            print(var.msg_maquina_turno)
            repite_maquina = True
            while repite_maquina and tablero_jugador.vidas > 0:
                repite_maquina = fun.turno_maquina(tablero_jugador, disparos_maquina)
                if tablero_jugador.vidas == 0: 
                    break

    # 4) Final
    if tablero_jugador.vidas <= 0:
        print(var.msg_pierdes)
    else:
        print(var.msg_ganas)

if __name__ == "__main__": # Activar el juego solo con el "run"
    jugar()