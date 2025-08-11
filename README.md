# Aprendizaje_Autonomo_2
Piedra, Papel o Tijera (Python)
Juego clásico entre usuario y computadora programado en Python 3.
Versión simple: validación básica, comparación de jugadas y opción de repetir partida.

#Requisitos
-Python 3.8+
-No requiere librerías externas (usa random de la biblioteca estándar)

#Funcionalidades implementadas
-Menú por consola (acepta 1/2/3 o piedra/papel/tijera)
-Elección aleatoria de la PC con random.choice()
-Lógica de resultado: empate / gana jugador / gana PC
-Pregunta para jugar otra vez (s / n)

#Diagramas de flujo
-Flujo principal
-Comparación de jugadas

#Explicación breve del código
-opciones: lista con las jugadas válidas (["piedra", "papel", "tijera"]).
-entrada: texto que escribe el usuario; se limpia y normaliza a minúsculas.
-elec_user: elección final del jugador en texto (a partir de 1/2/3 o palabra).
-elec_pc: elección aleatoria de la computadora con random.choice(opciones).

Comparación:
  -Si son iguales → Empate
  -Reglas: piedra > tijera, tijera > papel, papel > piedra
  -Si no se cumple la regla del jugador → gana la PC

#Autor
Glemer Jair Estupiñán Valencia


