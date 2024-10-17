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


# Método o función para verificar si las combinaciones de usuario son una combinación ganadora
def verify_winner(table):
    pass

# None inicialmente pero debe evaluar cada matriz declarada en la parte superior.
print(verify_winner(None))
