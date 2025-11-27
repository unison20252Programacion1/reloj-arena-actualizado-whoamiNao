# Completa las validaciones y llama a la función

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
        data = sys.stdin.read().strip().splitlines()

    # Validar que se recibieron dos líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    m_str = data[0].strip() # Primera línea: altura máxima (como texto)
    s = data[1]             # Segunda línea: carácter (o cadena) para la figura

    # Intentar convertir la altura a entero
    try:
        # TODO: Convertir m_str a entero y asignarlo a m
        pass
    except ValueError:
        # TODO: imprimir "Error: La altura debe ser un numero entero" y salir
        pass

    # TODO: llamar a la función triangulo_simetrico con los parámetros m y s
    # ERRATA: llamar a la función reloj_arena con los parámetros m y s.

if __name__ == "__main__":
    main()
