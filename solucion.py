import sys
# La función debe recibir la lista de líneas de entrada para manejar todas las validaciones.
# Se espera que 'entrada' sea una lista de cadenas, donde entrada[0] es la altura (m) 
# y entrada[1] es el carácter (s), si existen.
def reloj_arena(entrada: list[str]) -> str:
    """
    Lee una lista de líneas de entrada (se esperan 2: altura y caracter) y dibuja 
    un reloj de arena centrado en ASCII o imprime un error.

    :param entrada: Una lista de cadenas, donde entrada[0] es la altura (m) 
                    y entrada[1] es el carácter (s).
    :return: Una cadena (string) que contiene la figura o el mensaje de error.
    """
    
    # --- 1. VALIDACIÓN DE CANTIDAD DE ENTRADAS ---
    # Debe haber al menos dos elementos en la lista.
    if len(entrada) < 2:
        return "Error: Se esperan 2 lineas de entrada (altura, caracter)"

    # Obtener las entradas
    altura_str = entrada[0]
    caracter_line = entrada[1]
    
    # --- 2. VALIDACIÓN DEL CARÁCTER (s) ---
    # La segunda línea no puede ser vacía (strip() ya se hizo si se lee sys.stdin)
    if not caracter_line:
        return "Error: El caracter no puede ser vacío"

    # Tomar solo el primer carácter
    s = caracter_line[0]

    # --- 3. VALIDACIÓN DE LA ALTURA (m) ---
    
    # a) Debe ser un número entero
    try:
        m = int(altura_str)
    except ValueError:
        return "Error: La altura debe ser un numero entero"

    # b) Debe ser un entero positivo (> 0)
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    # --- 4. GENERACIÓN DEL RELOJ DE ARENA ---

    resultado = []
    
    # m es un entero positivo válido. s es un carácter válido.

    # --- A. PARTE SUPERIOR (Triángulo Decreciente) ---
    # Bucle desde i=0 hasta i=m-1
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        
        linea = " " * num_espacios + s * num_caracteres
        resultado.append(linea)

    # --- B. PARTE INFERIOR (Triángulo Creciente) ---
    # Bucle desde i=1 hasta i=m-1
    for i in range(1, m):
        num_espacios = (m - 1) - i
        num_caracteres = 2 * i + 1
        
        linea = " " * num_espacios + s * num_caracteres
        resultado.append(linea)

    # Unir todas las líneas con saltos de línea y devolver
    return "\n".join(resultado)
