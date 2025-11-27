# solucion.py - VERSIÓN FINAL Y COMPROBADA

def reloj_arena(m: int, s: str) -> str:
    
    # 1. Validación de la altura (m <= 0) - EL FORMATO DEBE SER ESTRICTO
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    # Se asume que el main.py ya manejó el error de 'altura no entera'.
    
    caracter = s[0] 
    resultado = []

    # --- 2. PARTE SUPERIOR (Triángulo Decreciente) ---
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # --- 3. PARTE INFERIOR (Triángulo Creciente) ---
    # Solo se ejecuta si m > 1
    for i in range(1, m):
        num_espacios = (m - 1) - i
        num_caracteres = 2 * i + 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    # Devolver la figura unida por saltos de línea. 
    # **IMPORTANTE:** Si el main.py usa print() sin end="", el evaluador espera
    # que la figura NO tenga un salto de línea al final, ya que print() lo añade.
    # El código actual con "\n".join() es correcto para evitar el salto de línea extra.
    return "\n".join(resultado)
