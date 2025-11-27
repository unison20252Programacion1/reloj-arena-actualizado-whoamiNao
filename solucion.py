def reloj_arena(m: int, s: str) -> str:
    """
    Genera un reloj de arena centrado en ASCII.

    :param m: Altura de la parte superior del reloj (número entero positivo).
    :param s: Carácter de relleno (se asume que es un solo carácter válido).
    :return: Una cadena (string) que contiene la figura o el mensaje de error.
    """
    
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    resultado = []
    
    # El ancho máximo de la figura es W = 2 * m - 1
    # La cantidad de espacios y caracteres se basa en el índice de la línea (i)

    # --- 1. PARTE SUPERIOR (Triángulo Decreciente) ---
    # Desde la línea i=0 (más ancha) hasta i=m-1 (la punta).
    for i in range(m):
        # Espacios: i
        num_espacios = i
        
        # Caracteres: 2 * (m - i) - 1
        num_caracteres = 2 * (m - i) - 1
        
        # Construir la línea: [Espacios][Caracteres]
        linea = " " * num_espacios + s * num_caracteres
        resultado.append(linea)

    # --- 2. PARTE INFERIOR (Triángulo Creciente) ---
    # Desde la línea i=1 (después de la punta) hasta i=m-1 (la base más ancha).
    for i in range(1, m):
        # Espacios: (m - 1) - i
        # En la primera línea (i=1), queremos m-2 espacios.
        # En la última línea (i=m-1), queremos 0 espacios.
        num_espacios = (m - 1) - i
        
        # Caracteres: 2 * i + 1
        # En la primera línea (i=1), queremos 3 caracteres.
        # En la última línea (i=m-1), queremos 2(m-1)+1 = 2m-1 caracteres.
        num_caracteres = 2 * i + 1
        
        # Construir la línea: [Espacios][Caracteres]
        linea = " " * num_espacios + s * num_caracteres
        resultado.append(linea)

    # Unir todas las líneas con saltos de línea y devolver
    return "\n".join(resultado)
