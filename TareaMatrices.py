# ANDREA MONDRAGON SAA

# Definición de los tableros creando un diccionario

tableros = {

# "X" representa al jugador 1.
# "O" representa al jugador 2.
# "_" representa un espacio vacío en el tablero.

    "sin_ganador": [["X", "O", "X"], ["O", "_", "X"], ["X", "O", "O"]],
    # No tiene un ganador, pero hay espacios vacíos, lo que indica que el juego puede continuar pero que no necesariamente está activo.
    "ganador_filas": [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]],
    # El jugador 1 o ("X") ha ganado al completar la primera fila con sus tres símbolos.
    "ganador_columnas": [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]],
    # El jugador 2 o ("O") ha ganado al completar la primera columna con sus tres símbolos.
    "ganador_diagonal": [["X", "O", "_"], ["", "X", "O"], ["_", "_", "X"]],
    # El jugador 1 o ("X") ha ganado al completar la diagonal principal (de arriba a la izquierda a abajo a la derecha)
    "empate": [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]],
    # Hay un empate, todos los espacios están ocupados y pero no hay un ganador.
    "en_progreso": [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]
    # Como hay espacios vacíos, el juego aún no ha terminado.
}

def verificar_estado(tablero):
    # Se comprueba en el tablero las filas, columnas y diagonales en una sola estructura.
    combinaciones = (
        tablero +                          # Filas
        [[tablero[j][i] for j in range(3)] for i in range(3)] +  # Columnas
        [[tablero[i][i] for i in range(3)],   # Diagonal principal
         [tablero[i][2 - i] for i in range(3)]]  # Diagonal secundaria
    )

    # Se itera sobre todas las combinaciones (filas, columnas, diagonales) para verificar si hay un ganador.
    # Y se le pone una condición para comprobar si los tres elementos de la combinación son iguales y diferentes de _. Si es así, se retorna el ganador.
    for combinacion in combinaciones:
        if combinacion[0] == combinacion[1] == combinacion[2] != "_":
            return f"Ganador: {combinacion[0]}"

    # Usamos la función any() para comprobar si hay algún espacio vacío (_) en el tablero.
    # Si hay alguno, retorna "juego en progreso".
    if any("_" in fila for fila in tablero):
        return "Juego en progreso"
    
    # Si no hay ganador ni espacios vacíos, se retorna "Empate".
    return "Empate"

# Ejecutamos la función para cada tablero
# nombre: se asigna el nombre del estado (ej: "sin_ganador").
# tablero: se asigna el tablero correspondiente (ej: [[“X”, “O”, “X”], ...]).
for nombre, tablero in tableros.items():
    print(f"{nombre}: {verificar_estado(tablero)}")