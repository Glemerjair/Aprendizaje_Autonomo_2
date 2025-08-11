
# Librería random:
# Sirve para generar valores aleatorios, en este juego se usa para que
# la computadora elija piedra, papel o tijera de forma impredecible.

import random  

# Lista de opciones válidas del juego
opciones = ["piedra", "papel", "tijera"]

while True:
    # Mostrar menú de opciones al jugador
    print("\nElige tu opción:")
    print("  1) piedra")
    print("  2) papel")
    print("  3) tijera")

    entrada = input("→ ")  # Variable 'entrada': guarda la opción que el usuario escribe
    entrada = entrada.strip().lower()  # Limpia espacios y convierte a minúsculas

    # Variable 'elec_user': guarda la elección final del jugador en texto
    if entrada == "1":
        elec_user = "piedra"
    elif entrada == "2":
        elec_user = "papel"
    elif entrada == "3":
        elec_user = "tijera"
    elif entrada in opciones:
        elec_user = entrada
    else:
        print("Opción no válida. Escribe 1, 2, 3 o piedra/papel/tijera.")
        continue  # Vuelve a pedir la opción si no es válida

    # Variable 'elec_pc': elección aleatoria de la computadora
    elec_pc = random.choice(opciones)

    # Mostrar elecciones
    print(f"Tú elegiste: {elec_user}")
    print(f"La computadora eligió: {elec_pc}")

    # Determinar el resultado
    if elec_user == elec_pc:
        print("Empate.")
    elif (elec_user == "piedra" and elec_pc == "tijera") or \
            (elec_user == "tijera" and elec_pc == "papel") or \
            (elec_user == "papel" and elec_pc == "piedra"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

    # Variable 'seguir': indica si el usuario quiere continuar jugando
    seguir = input("¿Jugar otra vez? (s/n): ").strip().lower()
    if seguir not in ("s", "si", "sí"):
        print("Gracias por jugar.")
        break
