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


# Función para verificar si hay un ganador en alguna fila
def revisar_filas(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "_":
            return fila[0]  # Retorna "X" o "O" si hay un ganador
    return None  # No hay ganadores en las filas

# Función para verificar si hay un ganador en alguna columna
def revisar_columnas(tablero):
    for indice_columna in range(3):
        if tablero[0][indice_columna] == tablero[1][indice_columna] == tablero[2][indice_columna] and tablero[0][indice_columna] != "_":
            return tablero[0][indice_columna]  # Retorna "X" o "O" si hay un ganador
    return None  # No hay ganadores en las columnas

# Función para verificar si hay un ganador en alguna diagonal
def revisar_diagonales(tablero):
    # Revisar la diagonal principal (esquina superior izquierda a esquina inferior derecha)
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "_":
        return tablero[0][0]  # Retorna "X" o "O" si hay un ganador
    # Revisar la diagonal inversa (esquina superior derecha a esquina inferior izquierda)
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "_":
        return tablero[0][2]  # Retorna "X" o "O" si hay un ganador
    return None  # No hay ganadores en las diagonales

# Tablero de ejemplo con filas ganadoras
tablero_con_filas_ganadoras = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]

# Revisar si hay un ganador en filas, columnas o diagonales
ganador_filas = revisar_filas(tablero_con_filas_ganadoras)
ganador_columnas = revisar_columnas(board_winner_columns)
ganador_diagonales = revisar_diagonales(board_winner_diagonal)

# Mostrar los resultados
print("Ganador en las filas:", ganador_filas)
print("Ganador en las columnas:", ganador_columnas)
print("Ganador en las diagonales:", ganador_diagonales)




