
def reloj_arena(m: int, s: str) -> str:
    
    if m <= 0:
        return "Error: La altura debe ser un entero positivo\n" 
    
    
    caracter = s[0] 
    resultado = []

   
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

  
    for i in range(1, m):
        num_espacios = (m - 1) - i
        num_caracteres = 2 * i + 1
        
        linea = " " * num_espacios + caracter * num_caracteres
        resultado.append(linea)

    return "\n".join(resultado) + "\n"
