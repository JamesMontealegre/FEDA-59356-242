# Combinaciones de juego 
# X = Movimientos jugador uno
# O = Movimientos jugador dos
# _ = Masilla en blanco, no hay movimientos.

board_no_winner = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_rows = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]
board_winner_columns = [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
board_winner_diagonal = [["X", "O", "_"], ["_", "X", "O"], ["_", "_", "X"]]
board_tie = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_in_progress = [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]


# Función para revisar si hay un ganador en las filas
def revisar_ganador_filas(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "_":
            return fila[0]  
    return None

# Función para revisar si hay un ganador en las columnas
def revisar_ganador_columnas(tablero):
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != "_":
            return tablero[0][col] r
    return None 

# Función para revisar si hay un ganador en las diagonales
def revisar_ganador_diagonales(tablero):
    # Diagonal principal (de izquierda a derecha)
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "_":
        return tablero[0][0]  
    # Diagonal secundaria (de derecha a izquierda)
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "_":
        return tablero[0][2] 
    return None  

# Ejemplo de uso con el tablero "tablero_ganador_filas"
tablero_ganador_filas = [["X", "X", "X"], ["O", "O", ""], ["", "", ""]]

# Revisar si hay un ganador por filas, columnas o diagonales
ganador_filas = revisar_ganador_filas(tablero_ganador_filas)
ganador_columnas = revisar_ganador_columnas(tablero_ganador_columnas)
ganador_diagonales = revisar_ganador_diagonales(tablero_ganador_diagonal)

# Imprimir resultados
print("Ganador en filas:", ganador_filas)
print("Ganador en columnas:", ganador_columnas)
print("Ganador en diagonales:", ganador_diagonales)


