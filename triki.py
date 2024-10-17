# Método o función para verificar si las combinaciones de usuario son una combinación ganadora
def verify_winner(table):
    # Verificar filas
    for row in table:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return f"Ganador: {row[0]} (fila)"

    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] and table[0][col] != "_":
            return f"Ganador: {table[0][col]} (columna)"
    
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != "_":
        return f"Ganador: {table[0][0]} (diagonal principal)"
    
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != "_":
        return f"Ganador: {table[0][2]} (diagonal secundaria)"
    
    for row in table:
        if "_" in row:
            return "El juego sigue en progreso"
    
    return "Empate"

board_no_winner = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_rows = [["X", "X", "X"], ["O", "O", ""], ["", "", ""]]
board_winner_columns = [["O", "X", ""], ["O", "X", ""], ["O", "X", "_"]]
board_winner_diagonal = [["X", "O", ""], ["", "X", "O"], ["", "", "X"]]
board_tie = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_in_progress = [["X", "O", "X"], ["", "O", ""], ["O", "X", "_"]]

print(verify_winner(board_no_winner))
print(verify_winner(board_winner_rows))
print(verify_winner(board_winner_columns))
print(verify_winner(board_winner_diagonal))
print(verify_winner(board_tie))
print(verify_winner(board_in_progress))