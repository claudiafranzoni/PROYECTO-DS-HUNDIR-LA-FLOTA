import variables as var

def jugar():
    print(var.msg_bienvenida)
    print(var.msg_instrucciones)

    # Prueba: esto lo borraré
    print("--- El tablero es de:", var.board_size, "x", var.board_size, "---")

    # Bucle de prueba para cuando los demás suban su parte:
    jugando = True
    while jugando:
        entrada = input("\nIntroduce fila y columna (ej: 3 4) o 'salir': ")

        if entrada.lower() == "salir":
            print("¡Hasta la próxima!")
            jugando = False
        else:
            try:
                # Separo los números
                coords = entrada.split()
                fila = int(coords[0])
                col  = int(coords[1])

                # Compruebo si se sale del tablero usando la variable de Claudia:
                if fila >= var.board_size or col >= var.board_size or fila < 0 or col < 0:
                    print(var.msg_coord_invalida)
                else:
                    print(f"Disparando a ({fila}, {col})... AGUA")
            
            except:
                print("Error: Introduce dos números (0-9) separados por un espacio.")

if __name__ == "__main__":
    jugar()