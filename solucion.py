
def reloj_arena(m: int, s: str) -> str:
    """
    Genera un reloj de arena centrado en ASCII.

    Asume que el main.py ya validó:
    - Cantidad de líneas de entrada.
    - Que 's' no está vacío y es el carácter de relleno.
    - Que 'm' es un número entero.
    
    Se encarga de:
    - Validar que m > 0.
    - Construir la figura.
    """
    
    # 1. VALIDACIÓN: m <= 0 
    # Añadimos \n al final para pasar el test de error de formato estricto (visto en la imagen).
    if m <= 0:
        return "Error: La altura debe ser un entero positivo\n" 

    caracter = s[0] 
    resultado = []

    # --- 2. PARTE SUPERIOR (Triángulo Decreciente) ---
    # Genera m líneas, de ancho 2*m-1 a 1.
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # --- 3. PARTE INFERIOR (Triángulo Creciente) ---
    # Genera m-1 líneas, de ancho 3 a 2*m-1.
    for i in range(1, m):
        num_espacios = (m - 1) - i
        num_caracteres = 2 * i + 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # Devolver la figura unida por saltos de línea. 
    # **Añadimos un SALTO DE LÍNEA FINAL** (mismo problema de formato que el error de validación)
    # Si el 'main.py' usa print() sin end="", la única forma de que el evaluador espere 
    # un \n al final es si lo incluyes en tu cadena.
    return "\n".join(resultado) + "\n"
