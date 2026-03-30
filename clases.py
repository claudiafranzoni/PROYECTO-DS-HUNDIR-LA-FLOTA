class Tablero:

tablero = np.full((10,10), " ")
print(tablero)

def crear_tablero(lado = 10, agua = " "):
    tablero = np.full((lado, lado), agua)
    return tablero


#def coloca_barco(posicion_x, posicion_y):

#def recibe_disparo(poscion_x, posicion_y):

