# solucion.py

def reloj_arena(m: int, s: str) -> str:
    """
    Genera un reloj de arena centrado en ASCII.
    Asume que el main.py ya validó:
    1. Que hay 2 líneas de entrada.
    2. Que el caracter 's' no está vacío.
    3. Que 'm' es un número entero.
    
    :param m: Altura de la parte superior del reloj (número entero).
    :param s: Cadena de caracteres, cuyo primer caracter se usará para la figura.
    :return: Una cadena (string) que contiene la figura o el mensaje de error.
    """
    
    # Manejar la validación que, según el TODO, debe ir en esta función: m > 0
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    # Ya que el main.py pasó 's' como string, usamos s[0] para asegurar que sea un solo carácter.
    caracter = s[0]
    resultado = []

    # --- 1. PARTE SUPERIOR (Triángulo Decreciente) ---
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # --- 2. PARTE INFERIOR (Triángulo Creciente) ---
    for i in range(1, m):
        num_espacios = (m - 1) - i
        num_caracteres = 2 * i + 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # Devolver la figura unida por saltos de línea.
    # El main.py debe usar print(resultado, end="") para evitar el salto de línea final.
    return "\n".join(resultado)
