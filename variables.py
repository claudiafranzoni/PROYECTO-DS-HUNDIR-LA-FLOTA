# =============================================================
#  variables.py — Constantes del juego "Hundir la Flota"
#  Autora : Claudia (Scrum Master)
# =============================================================
 
# ── Dimensiones del tablero ───────────────────────────────────
board_size = 10          # Tablero de 10 x 10 celdas
 
# ── Flota de barcos ───────────────────────────────────────────
barcos = {
    "fragata":     {"eslora": 1, "cantidad": 4},   # 4 × 1 celda
    "destructor":  {"eslora": 2, "cantidad": 3},   # 3 × 2 celdas
    "crucero":     {"eslora": 3, "cantidad": 2},   # 2 × 3 celdas
    "portaviones": {"eslora": 4, "cantidad": 1},   # 1 × 4 celdas
}
 
# Número total de celdas con barco por jugador (= vidas)
total_barcos_celdas = sum(
    datos["eslora"] * datos["cantidad"]
    for datos in barcos.values()
)  # → 4*1 + 3*2 + 2*3 + 1*4 = 20
 
# ── Símbolos del tablero ──────────────────────────────────────
symbol_agua    = "~"   # Agua sin disparar
symbol_barco   = "O"   # Barco intacto (tablero propio)
symbol_disparo = "X"   # Disparo que impactó un barco
symbol_fallo   = "*"   # Disparo que cayó en agua
 
# Diccionario agrupado (útil para mostrar la leyenda)
symbols = {
    "agua":    symbol_agua,
    "barco":   symbol_barco,
    "impacto": symbol_disparo,
    "fallado": symbol_fallo,
}
 
# ── Orientaciones para colocar barcos ────────────────────────
# Indica hacia dónde crece el barco desde la celda inicial
# N = hacia arriba      --> la fila disminuye
# S = hacia abajo       --> la fila aumenta
# E = hacia la derecha  --> la columna aumenta
# O = hacia la izquierda --> la columna disminuye
orientations = ["N", "S", "E", "O"]
 
# Desplazamiento (fila, columna) por orientación
# Martha usará esto en place_ships() para colocar cada celda del barco
orientation_delta = {
    "N": (-1,  0),
    "S": ( 1,  0),
    "E": ( 0,  1),
    "O": ( 0, -1),
}
 
# ── Mensajes del juego ────────────────────────────────────────
msg_bienvenida = """
╔══════════════════════════════════════════╗
║        ⚓  HUNDIR LA FLOTA  ⚓          ║
╚══════════════════════════════════════════╝
¡Bienvenido! Destruye toda la flota enemiga
antes de que la máquina hunda la tuya.
"""
 
msg_instrucciones = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INSTRUCCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • El tablero es de 10 x 10 (filas 0-9, columnas 0-9).
  • Introduce coordenadas como: fila columna  (ej. 3 7)
  • Si aciertas, vuelves a disparar.
  • Si fallas, dispara la máquina.
  • Gana quien hunda toda la flota rival.
 
  FLOTA (cada jugador):
    Fragata     (x4) ── eslora 1
    Destructor  (x3) ── eslora 2
    Crucero     (x2) ── eslora 3
    Portaviones (x1) ── eslora 4
 
  SIMBOLOGÍA DEL TABLERO:
    ~  Agua sin disparar
    O  Barco intacto (solo tu tablero)
    X  Impacto en barco
    *  Disparo fallado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
 
msg_tu_turno       = "\n🎯 Tu turno — introduce coordenadas (fila columna):"
msg_maquina_turno  = "\n🤖 Turno de la máquina..."
msg_impacto        = "💥 ¡IMPACTO!"
msg_agua           = "💧 Agua. Turno para la máquina."
msg_maquina_hit    = "🤖 ¡La máquina ha acertado en ({}, {})!"
msg_maquina_miss   = "🤖 La máquina ha fallado en ({}, {})."
msg_ya_disparado   = "⚠️  Ya disparaste en esas coordenadas. Elige otras."
msg_coord_invalida = "⚠️  Coordenadas inválidas. Usa números entre 0 y 9."
msg_ganas          = "\n🏆 ¡Enhorabuena! Has hundido toda la flota enemiga. ¡GANASTE!"
msg_pierdes        = "\n💀 La máquina ha hundido tu flota. ¡Has perdido!"
 
# ── Etiquetas de los tableros al imprimir ─────────────────────
label_my_board    = "═══  MI TABLERO  ═══"
label_enemy_board = "═══  TABLERO ENEMIGO  ═══"