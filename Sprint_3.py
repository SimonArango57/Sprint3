# Pedimos al usuario que ingrese su calificación
try:
    calificacion = int(input("Ingresa tu calificación (un número entre 0 y 100): "))

    # Verificamos que la calificación esté dentro del rango válido
    if 0 <= calificacion <= 100:
        # Usamos condicionales para determinar la letra de la calificación
        if calificacion >= 90:
            print("Tu calificación es: A")
        elif calificacion >= 80:
            print("Tu calificación es: B")
        elif calificacion >= 70:
            print("Tu calificación es: C")
        elif calificacion >= 60:
            print("Tu calificación es: D")
        else:
            print("Tu calificación es: F")
    else:
        print("La calificación ingresada no es válida. Debe estar entre 0 y 100.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")