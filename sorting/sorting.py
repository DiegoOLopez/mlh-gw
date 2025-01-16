import random

def generar_lista_aleatoria(tamano, minimo, maximo):
    """Genera una lista aleatoria de tamaño especificado."""
    return [random.randint(minimo, maximo) for _ in range(tamano)]

def bubble_sort(lista):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    n = len(lista)
    for i in range(n):
        # Últimos elementos ya están ordenados, no es necesario verificarlos
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambia si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Generar lista aleatoria
tamano_lista = 10  # Cambia el tamaño si lo deseas
lista = generar_lista_aleatoria(tamano_lista, 1, 100)
print("Lista original:", lista)

# Ordenar lista
bubble_sort(lista)
print("Lista ordenada:", lista)
