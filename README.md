[README.md](https://github.com/user-attachments/files/26721197/README.md)
# ⚓ Hundir la Flota

Este proyecto es el resultado del trabajo conjunto del Grupo 4 durante el Bootcamp de Data Science. En donde la tarea principal es llevar el clásico juego de Hundir la Flota a Python, repartiendo responsabilidades, resolviendo problemas en equipo y aprendiendo a integrar distintos módulos en un juego funcional.

---

## 👥 Equipo — Grupo 4

| Nombre  | Rol            | Responsabilidad                                                        |
|---------|----------------|------------------------------------------------------------------------|
| Claudia | Scrum Master   | `variables.py` — constantes, símbolos y mensajes del juego · `README.md` |
| Martha  | Developer 1    | `clases.py` — clase `Tablero`: colocar barcos, recibir disparos, gestión de vidas |
| Isaac   | Developer 2    | `funciones.py` — visualización de tableros, turnos, validación de entrada, comprobación de victoria |
| María   | Developer 3    | `main.py` — bucle `while True` e integración final de todos los módulos |

---

## 📁 Estructura del proyecto

```
hundir_la_flota/
├── main.py          → Punto de entrada: bucle principal del juego
├── clases.py        → Clase Tablero (colocar_barco, recibir_disparo, barco_hundido)
├── funciones.py     → Funciones auxiliares (turnos, visualización, victoria)
└── variables.py     → Constantes: board_size, barcos, símbolos, mensajes
```

> Todos los archivos deben estar en la **misma carpeta** para que los imports funcionen.

---

## ▶️ Cómo ejecutar

### 1. Requisitos previos

- Python
- Librería **NumPy**

Instalar NumPy si no lo tienes:

```bash
pip install numpy
```

### 2. Lanzar el juego

Desde la terminal, entra en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

> Si tu sistema tiene Python 2 y Python 3 instalados, usa `python3 main.py`

### 3. Cómo introducir coordenadas

Cuando el juego te pida un disparo, escribe la **fila** y la **columna** separadas por un espacio y pulsa Enter:

```
🎯 Tu turno — introduce coordenadas (fila columna):
3 7
```

Las coordenadas van de **0 a 9** tanto en filas como en columnas.

---

## 🎮 Reglas del juego

1. Hay dos jugadores: **tú** y la **máquina**.
2. El tablero es de **10 × 10** posiciones.
3. Los barcos se colocan **aleatoriamente** al inicio de cada partida.
4. Se juega **por turnos**, empiezas tú.
5. Si **aciertas** un disparo, vuelves a disparar.
6. Si **fallas**, dispara la máquina a una posición aleatoria.
7. La máquina **nunca repite** coordenada.
8. Gana quien **hunda toda la flota rival** primero.

---

## 🚢 Flota (cada jugador)

| Barco        | Eslora | Cantidad | Celdas totales |
|--------------|:------:|:--------:|:--------------:|
| Fragata      | 1      | × 4      | 4              |
| Destructor   | 2      | × 3      | 6              |
| Crucero      | 3      | × 2      | 6              |
| Portaviones  | 4      | × 1      | 4              |
| **Total**    |        |          | **20 celdas**  |

Los barcos se colocan con orientación **N, S, E u O** (Norte, Sur, Este, Oeste) desde una celda de inicio aleatoria. No pueden tocarse entre sí ni salirse del tablero.

---

## 🗺️ Simbología del tablero

Al jugar verás dos tableros impresos en pantalla: el tuyo (con tus barcos) y el del enemigo (solo con tus disparos).

| Símbolo | Significado                                    |
|:-------:|------------------------------------------------|
| `~`     | Agua — celda sin disparar                      |
| `O`     | Barco intacto (visible solo en tu tablero)     |
| `X`     | Impacto — disparo que acertó en un barco       |
| `*`     | Fallo — disparo que cayó en agua               |

Ejemplo de tableros durante una partida:

```
  ═══  MI TABLERO  ═══        ═══  TABLERO ENEMIGO  ═══
  0 1 2 3 4 5 6 7 8 9        0 1 2 3 4 5 6 7 8 9
0 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~      0 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
1 ~ O O O ~ ~ ~ ~ ~ ~      1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~      2 ~ ~ X ~ ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ O ~ ~ ~ ~ ~      3 ~ ~ ~ ~ ~ * ~ ~ ~ ~
4 ~ ~ ~ ~ O ~ ~ ~ ~ ~      4 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
```

---

## 🔗 Dependencias entre archivos

```
variables.py
      ↑ importado por
clases.py ──────┐
funciones.py ───┼──→  main.py
```

`main.py` es el único punto de entrada. Importa y coordina todos los módulos.

---

## 📦 Dependencias externas

| Librería | Uso                                      | Instalación         |
|----------|------------------------------------------|---------------------|
| `numpy`  | Arrays 10×10 para los tableros           | `pip install numpy` |
| `random` | Disparos aleatorios de la máquina        | Incluida en Python  |
