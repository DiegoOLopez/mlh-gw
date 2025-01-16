def generador_aleatorio(semilla, minimo, maximo):
    # Generar un número pseudoaleatorio
    semilla = (semilla * 37 + 89) % 1000  # Fórmula 
    # Ajustar el número al rango deseado
    aleatorio = minimo + (semilla % (maximo - minimo + 1))
    return aleatorio, semilla

# Ejemplo de uso
semilla_inicial = 42  # Semilla inicial
minimo = 1
maximo = 10

# Generar varios números aleatorios
for _ in range(5):
    numero_aleatorio, semilla_inicial = generador_aleatorio(semilla_inicial, minimo, maximo)
    print("Número aleatorio generado:", numero_aleatorio)