import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Escribe tu elección: piedra, papel o tijera")
    
    jugador = input("Tu elección: ").lower()
    while jugador not in opciones:
        print("Elección inválida. Por favor, elige piedra, papel o tijera.")
        jugador = input("Tu elección: ").lower()

    computadora = random.choice(opciones)
    
    print(f"\nTú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Felicidades, ganaste!")
    else:
        print("La computadora gana. ¡Inténtalo de nuevo!")
        
# Ejecutar el juego
jugar_piedra_papel_tijera()
