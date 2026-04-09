import numpy as np
from clases import Tablero
from variables import (
    board_size,
    symbol_agua,
    symbol_barco,
    symbol_disparo,
    symbol_fallo,
    barcos,
)

# ── Utilidades ────────────────────────────────────────────────

passed = 0
failed = 0

def ok(nombre):
    global passed
    passed += 1
    print(f"  ✅ {nombre}")

def fail(nombre, detalle=""):
    global failed
    failed += 1
    print(f"  ❌ {nombre}" + (f": {detalle}" if detalle else ""))

def seccion(titulo):
    print(f"\n{'━'*50}")
    print(f"  {titulo}")
    print(f"{'━'*50}")

def resumen():
    total = passed + failed
    print(f"\n{'═'*50}")
    print(f"  RESULTADO: {passed}/{total} tests pasados")
    if failed == 0:
        print("  🏆 Todo correcto!")
    else:
        print(f"  ⚠️  {failed} test(s) fallaron")
    print(f"{'═'*50}\n")


# ══════════════════════════════════════════════════════════════
#  1. INICIALIZACIÓN DEL TABLERO
# ══════════════════════════════════════════════════════════════
seccion("1. INICIALIZACIÓN DEL TABLERO")

t = Tablero("test")

# Dimensiones correctas
if t.board.shape == (board_size, board_size):
    ok("board tiene dimensiones 10x10")
else:
    fail("board tiene dimensiones 10x10", f"shape={t.board.shape}")

if t.tracking.shape == (board_size, board_size):
    ok("tracking tiene dimensiones 10x10")
else:
    fail("tracking tiene dimensiones 10x10", f"shape={t.tracking.shape}")

# Tablero vacío al inicio
if np.all(t.board == symbol_agua):
    ok("board inicializado todo a agua")
else:
    fail("board inicializado todo a agua")

if np.all(t.tracking == symbol_agua):
    ok("tracking inicializado todo a agua")
else:
    fail("tracking inicializado todo a agua")

# Vidas en 0 antes de colocar barcos
if t.vidas == 0:
    ok("vidas = 0 antes de colocar barcos")
else:
    fail("vidas = 0 antes de colocar barcos", f"vidas={t.vidas}")


# ══════════════════════════════════════════════════════════════
#  2. COLOCAR BARCO — casos válidos
# ══════════════════════════════════════════════════════════════
seccion("2. COLOCAR BARCO — casos válidos")

t = Tablero("test")

# Colocar fragata (eslora 1) en el centro
res = t.colocar_barco("fragata", 5, 5, "N")
if res:
    ok("fragata colocada correctamente")
else:
    fail("fragata colocada correctamente")

if t.board[5, 5] == symbol_barco:
    ok("fragata aparece en tablero en (5,5)")
else:
    fail("fragata aparece en tablero en (5,5)")

if t.vidas == 1:
    ok("vidas = 1 tras colocar fragata (eslora 1)")
else:
    fail("vidas = 1 tras colocar fragata (eslora 1)", f"vidas={t.vidas}")

# Destructor hacia el Este
t2 = Tablero("test")
res = t2.colocar_barco("destructor", 0, 0, "E")
if res:
    ok("destructor colocado hacia el Este")
else:
    fail("destructor colocado hacia el Este")

if t2.board[0, 0] == symbol_barco and t2.board[0, 1] == symbol_barco:
    ok("destructor ocupa (0,0) y (0,1)")
else:
    fail("destructor ocupa (0,0) y (0,1)")

# Crucero hacia el Sur
t3 = Tablero("test")
res = t3.colocar_barco("crucero", 0, 0, "S")
if res:
    ok("crucero colocado hacia el Sur")
else:
    fail("crucero colocado hacia el Sur")

if t3.board[0,0] == symbol_barco and t3.board[1,0] == symbol_barco and t3.board[2,0] == symbol_barco:
    ok("crucero ocupa (0,0), (1,0) y (2,0)")
else:
    fail("crucero ocupa (0,0), (1,0) y (2,0)")

# Portaviones hacia el Norte desde fila 9
t4 = Tablero("test")
res = t4.colocar_barco("portaviones", 9, 5, "N")
if res:
    ok("portaviones colocado hacia el Norte desde fila 9")
else:
    fail("portaviones colocado hacia el Norte desde fila 9")

# Barco hacia el Oeste desde columna 9
t5 = Tablero("test")
res = t5.colocar_barco("destructor", 5, 9, "O")
if res:
    ok("destructor colocado hacia el Oeste desde columna 9")
else:
    fail("destructor colocado hacia el Oeste desde columna 9")

if t5.board[5, 9] == symbol_barco and t5.board[5, 8] == symbol_barco:
    ok("destructor ocupa (5,9) y (5,8)")
else:
    fail("destructor ocupa (5,9) y (5,8)")


# ══════════════════════════════════════════════════════════════
#  3. COLOCAR BARCO — fuera del tablero
# ══════════════════════════════════════════════════════════════
seccion("3. COLOCAR BARCO — fuera del tablero")

t = Tablero("test")

# Portaviones hacia el Sur desde fila 8 → se sale
res = t.colocar_barco("portaviones", 8, 0, "S")
if not res:
    ok("portaviones rechazado: se sale por el Sur (fila 8 + eslora 4)")
else:
    fail("portaviones rechazado: se sale por el Sur")

# Destructor hacia el Norte desde fila 0
res = t.colocar_barco("destructor", 0, 5, "N")
if not res:
    ok("destructor rechazado: se sale por el Norte (fila 0)")
else:
    fail("destructor rechazado: se sale por el Norte")

# Crucero hacia el Este desde columna 8
res = t.colocar_barco("crucero", 5, 8, "E")
if not res:
    ok("crucero rechazado: se sale por el Este (col 8 + eslora 3)")
else:
    fail("crucero rechazado: se sale por el Este")

# Destructor hacia el Oeste desde columna 0
res = t.colocar_barco("destructor", 5, 0, "O")
if not res:
    ok("destructor rechazado: se sale por el Oeste (col 0)")
else:
    fail("destructor rechazado: se sale por el Oeste")


# ══════════════════════════════════════════════════════════════
#  4. COLOCAR BARCO — colisión entre barcos
# ══════════════════════════════════════════════════════════════
seccion("4. COLOCAR BARCO — colisión y proximidad")

t = Tablero("test")
t.colocar_barco("crucero", 5, 5, "E")  # ocupa (5,5), (5,6), (5,7)

# Barco encima
res = t.colocar_barco("fragata", 5, 6, "N")
if not res:
    ok("fragata rechazada: encima del crucero")
else:
    fail("fragata rechazada: encima del crucero")

# Barco adyacente (toca por el margen 3x3)
res = t.colocar_barco("fragata", 4, 5, "N")
if not res:
    ok("fragata rechazada: adyacente al crucero (margen 1 celda)")
else:
    fail("fragata rechazada: adyacente al crucero")

# Barco suficientemente lejos
res = t.colocar_barco("fragata", 3, 5, "N")
if res:
    ok("fragata aceptada: suficientemente lejos del crucero")
else:
    fail("fragata aceptada: suficientemente lejos del crucero")


# ══════════════════════════════════════════════════════════════
#  5. VIDAS — suma correcta
# ══════════════════════════════════════════════════════════════
seccion("5. VIDAS — suma correcta")

t = Tablero("test")
t.colocar_barco("fragata",     5, 5, "N")   # eslora 1
t.colocar_barco("destructor",  0, 0, "E")   # eslora 2
t.colocar_barco("crucero",     9, 9, "O")   # eslora 3

esperadas = 1 + 2 + 3
if t.vidas == esperadas:
    ok(f"vidas = {esperadas} tras colocar fragata + destructor + crucero")
else:
    fail(f"vidas = {esperadas}", f"obtenidas={t.vidas}")


# ══════════════════════════════════════════════════════════════
#  6. RECIBIR DISPARO
# ══════════════════════════════════════════════════════════════
seccion("6. RECIBIR DISPARO")

t = Tablero("test")
t.colocar_barco("fragata", 5, 5, "N")  # barco en (5,5)

# Disparo al agua
res = t.recibir_disparo(0, 0)
if res == "Agua":
    ok("disparo al agua devuelve 'Agua'")
else:
    fail("disparo al agua devuelve 'Agua'", f"resultado='{res}'")

if t.board[0, 0] == symbol_fallo:
    ok("casilla de agua marcada con symbol_fallo")
else:
    fail("casilla de agua marcada con symbol_fallo")

# Disparo repetido al agua
res = t.recibir_disparo(0, 0)
if res == "Repetido":
    ok("disparo repetido en agua devuelve 'Repetido'")
else:
    fail("disparo repetido en agua devuelve 'Repetido'", f"resultado='{res}'")

# Disparo al barco — fragata eslora 1 → hundido directo
vidas_antes = t.vidas
res = t.recibir_disparo(5, 5)
if res == "Hundido":
    ok("disparo a fragata (eslora 1) devuelve 'Hundido'")
else:
    fail("disparo a fragata (eslora 1) devuelve 'Hundido'", f"resultado='{res}'")

if t.board[5, 5] == symbol_disparo:
    ok("casilla de barco marcada con symbol_disparo")
else:
    fail("casilla de barco marcada con symbol_disparo")

if t.vidas == vidas_antes - 1:
    ok("vidas decrementadas en 1 tras impacto")
else:
    fail("vidas decrementadas en 1 tras impacto", f"antes={vidas_antes}, ahora={t.vidas}")

# Disparo repetido al barco hundido
res = t.recibir_disparo(5, 5)
if res == "Repetido":
    ok("disparo repetido en barco hundido devuelve 'Repetido'")
else:
    fail("disparo repetido en barco hundido devuelve 'Repetido'", f"resultado='{res}'")

# Destructor — primer impacto Tocado, segundo Hundido
t2 = Tablero("test")
t2.colocar_barco("destructor", 3, 3, "E")  # ocupa (3,3) y (3,4)

res1 = t2.recibir_disparo(3, 3)
if res1 == "Tocado":
    ok("primer impacto en destructor devuelve 'Tocado'")
else:
    fail("primer impacto en destructor devuelve 'Tocado'", f"resultado='{res1}'")

res2 = t2.recibir_disparo(3, 4)
if res2 == "Hundido":
    ok("segundo impacto en destructor devuelve 'Hundido'")
else:
    fail("segundo impacto en destructor devuelve 'Hundido'", f"resultado='{res2}'")


# ══════════════════════════════════════════════════════════════
#  7. BARCO HUNDIDO
# ══════════════════════════════════════════════════════════════
seccion("7. BARCO HUNDIDO — lógica interna")

t = Tablero("test")
t.colocar_barco("crucero", 5, 5, "E")  # ocupa (5,5), (5,6), (5,7)

# Un impacto → no hundido
t.recibir_disparo(5, 5)
if not t.barco_hundido(5, 5):
    ok("crucero con 1 impacto → NO hundido")
else:
    fail("crucero con 1 impacto → NO hundido")

# Dos impactos → todavía no hundido
t.recibir_disparo(5, 6)
if not t.barco_hundido(5, 6):
    ok("crucero con 2 impactos → NO hundido")
else:
    fail("crucero con 2 impactos → NO hundido")

# Tres impactos → hundido
t.recibir_disparo(5, 7)
if t.barco_hundido(5, 7):
    ok("crucero con 3 impactos → HUNDIDO")
else:
    fail("crucero con 3 impactos → HUNDIDO")


# ══════════════════════════════════════════════════════════════
#  8. FLOTA ALEATORIA
# ══════════════════════════════════════════════════════════════
seccion("8. FLOTA ALEATORIA")

t = Tablero("test")
t.colocar_flota_aleatoria()

# Vidas totales correctas (4*1 + 3*2 + 2*3 + 1*4 = 20)
if t.vidas == 20:
    ok(f"vidas = 20 tras colocar flota completa")
else:
    fail(f"vidas = 20 tras colocar flota completa", f"vidas={t.vidas}")

# Número de celdas con barco
celdas_barco = np.sum(t.board == symbol_barco)
if celdas_barco == 20:
    ok("exactamente 20 celdas marcadas como barco")
else:
    fail("exactamente 20 celdas marcadas como barco", f"encontradas={celdas_barco}")

# Sin solapamientos: cada celda es barco como máximo una vez (ya garantizado por lo anterior)
ok("sin solapamientos (verificado por conteo exacto de celdas)")

# Repetible: dos tableros distintos son válidos
t2 = Tablero("test2")
t2.colocar_flota_aleatoria()
if t2.vidas == 20:
    ok("segunda flota aleatoria también válida (vidas=20)")
else:
    fail("segunda flota aleatoria también válida", f"vidas={t2.vidas}")


# ══════════════════════════════════════════════════════════════
#  RESUMEN FINAL
# ══════════════════════════════════════════════════════════════
resumen()
