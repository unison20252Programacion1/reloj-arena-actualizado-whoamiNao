import sys
from solucion import reloj_arena

def main():
    """
    data: lista de líneas leídas desde la entrada estándar o ingresadas por el usuario
          donde cada elemento de la lista es un string     
    """

    # IF que permite leer desde la entrada estándar o pedir datos al usuario
    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        # Se lee toda la entrada, se elimina el espacio/salto de línea al final, 
        # y se divide en líneas.
        data = sys.stdin.read().strip().splitlines() 

    # 1. Validar que se recibieron dos líneas (Esta validación es correcta)
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    m_str = data[0].strip() # Primera línea: altura máxima (como texto)
    s = data[1]             # Segunda línea: carácter (o cadena) para la figura

    # 2. Validar que el caracter no sea vacío (necesario según las restricciones)
    if not s:
        # Nota: La muestra de error para este caso no pide un \n, así que no lo añadimos.
        print("Error: El caracter no puede ser vacío")
        return

    m = 0 # Inicializar m para el scope del try/except
    
    # 3. Intentar convertir la altura a entero
    try:
        # TODO: Convertir m_str a entero y asignarlo a m
        m = int(m_str) 
    except ValueError:
        # TODO: imprimir "Error: La altura debe ser un numero entero" y salir
        # Nota: Este error del main.py NO lleva \n, porque print() lo añade automáticamente.
        print("Error: La altura debe ser un numero entero") 
        return

    # 4. Llamar a la función y manejar la salida
    # TODO: llamar a la función reloj_arena con los parámetros m y s.
    resultado = reloj_arena(m, s)
    
    # **Clave de la Solución de Formato:**
    # La función reloj_arena ahora devuelve un string que YA incluye el salto de línea al final 
    # (tanto para el error de m<=0 como para la figura).
    # Por lo tanto, debemos asegurarnos de que el 'print' NO añada otro salto de línea.
    print(resultado, end="") 

if __name__ == "__main__":
    main()
